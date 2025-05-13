from django.db import models
from django.conf import settings
from .utils import calculate_cumulative_gpa, calculate_total_credits

class CandidateApplication(models.Model):
    POSITION_CHOICES = [
        ('president', 'President'),
        ('deputy_president', 'Deputy President'),
        ('sec_gen', 'Secretary General'),
        ('finance', 'Finance and Labour Secretary'),
        ('academics_foreign', 'Academics & Foreign Affairs Secretary'),
        ('sports', 'Sports & Entertainment Secretary'),
        ('gender', 'Gender & Special Interest Secretary'),
        ('nursing_rep', 'Senator - School of Nursing & Health Sciences'),
        ('business_rep', 'Senator - Scholar of Business'),
        ('education_rep', 'Senator - School of Education, Humanities and Social Sciences'),
        ('science_rep', 'School of Science and Technology'),
        ('religious_rep', 'Religious Affairs Rep'),
        ('international_rep', 'International Rep'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position_applied = models.CharField(max_length=50, choices=POSITION_CHOICES)
    manifesto = models.TextField(blank=True)
    application_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    eligible = models.BooleanField(default=False)
    submission_date = models.DateTimeField(auto_now_add=True)

    def check_eligibility(self):
        user = self.user
        student_id = user.student_id
        gpa = calculate_cumulative_gpa(student_id)
        credits = calculate_total_credits(student_id)

        if self.position_applied == 'international_rep':
            if user.nationality != 'Kenyan' and 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'religious_rep':
            if user.program_name.lower().startswith('theology') and 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'nursing_rep':
            if user.department_name.lower().startswith('nursing') and 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'business_rep':
            if user.department_name.lower().startswith('business') and 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'education_rep':
            if user.department_name.lower().startswith('education') and 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'science_rep':
            if user.department_name.lower().startswith('science') and 54 <= credits < 100 and not user.student.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'sports':
            if 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'gender':
            if 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'academics_foreign':
            if 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'finance':
            if 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'sec_gen':
            if 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'deputy_president':
            if 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'

        elif self.position_applied == 'president':
            if 54 <= credits < 100 and not user.has_disciplinary_record and gpa and gpa >= 2.5:
                self.eligible = True
                self.application_status = 'approved'
            else:
                self.application_status = 'rejected'
        else:
            self.eligible = False
            self.application_status = 'rejected'

        self.save()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} for {self.get_position_applied_display()}"


