# users/utils.py
from django.db.models import Sum, F
from .models import StudentAcademic

def calculate_cumulative_gpa(student_id):
    completed_courses = StudentAcademic.objects.filter(
        student_id=student_id,
        status='Completed',
        gpa_points__isnull=False,
        credit_hours__gt=0
    ).annotate(
        weighted_gpa=F('gpa_points') * F('credit_hours')
    )

    total_weighted_gpa = completed_courses.aggregate(total=Sum('weighted_gpa'))['total'] or 0
    total_credits = completed_courses.aggregate(total=Sum('credit_hours'))['total'] or 0

    if total_credits == 0:
        return None  # Avoid division by zero

    return round(total_weighted_gpa / total_credits, 2)
