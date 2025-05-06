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
    student_id = models.CharField(max_length=20, primary_key =True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='department_id')  # Foreign key to department
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    year_of_study = models.IntegerField()
    tribe = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    class Meta:
        db_table = 'students'
        managed = False 
