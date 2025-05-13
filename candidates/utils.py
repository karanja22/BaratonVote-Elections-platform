from django.db.models import Sum, F
from users.registry import StudentAcademic

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
        return None  

    return round(total_weighted_gpa / total_credits, 2)

def calculate_total_credits(student_id):
    completed_courses = StudentAcademic.objects.filter(
        student_id=student_id,
        status='Completed',
        credit_hours__gt=0
    )
    return completed_courses.aggregate(total=Sum('credit_hours'))['total'] or 0