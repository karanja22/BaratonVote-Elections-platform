from django.db import models
from .utils import calculate_cumulative_gpa, calculate_total_credits
from users.registry import Semester
from django.conf import settings
from users.registry import StudentAcademic
from .models import CandidateApplication

class DelegateApplication(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)  
    on_work_study = models.BooleanField(help_text="Are you currently in the Work-Study program?")

    application_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    eligible = models.BooleanField(default=False)
    submission_date = models.DateTimeField(auto_now_add=True)

    def is_registered_this_semester(self):
        current_semester = Semester.objects.filter(is_current=True).first()

        if not current_semester:
            return False

        return StudentAcademic.objects.filter(
            student_id=self.user.student_id,
            semester=current_semester.term_label
        ).exists()

    def check_eligibility(self):
        user = self.user
        student_id = user.student_id
        gpa = calculate_cumulative_gpa(student_id)

        is_candidate = CandidateApplication.objects.filter(user=user, application_status='approved').exists()
        is_registered = self.is_registered_this_semester()

        if (
            not is_candidate and
            not user.has_disciplinary_record and
            gpa is not None and gpa >= 2.5 and
            (is_registered or self.on_work_study)
        ):
            self.eligible = True
            self.application_status = 'approved'
        else:
            self.application_status = 'rejected'
        self.save()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Delegate Application ({self.application_status})"
