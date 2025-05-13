from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = False  
        db_table = 'schools'


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, db_column='school_id')

    class Meta:
        managed = False 
        db_table = 'departments'


class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='department_id')

    class Meta:
        managed = False 
        db_table = 'programs'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    tribe = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    admission_year = models.IntegerField(blank=True, null=True)
    year_of_study = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    department_name = models.CharField(max_length=255, blank=True, null=True)
    program_name = models.CharField(max_length=255, blank=True, null=True)
    program = models.ForeignKey('Program', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    academic_year = models.CharField(max_length=9)
    term = models.SmallIntegerField()
    term_label = models.CharField(max_length=50)
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False  
        db_table = 'semesters'

    def __str__(self):
        return self.term_label

        
class StudentAcademic(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    semester = models.CharField(max_length=50) 
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=255)
    credit_hours = models.IntegerField()
    grade = models.CharField(max_length=2, blank=True, null=True)
    gpa_points = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, default='In Progress')

    class Meta:
        managed = False
        db_table = 'student_academics'

    def __str__(self):
        return f"{self.course_code} - {self.semester}"
