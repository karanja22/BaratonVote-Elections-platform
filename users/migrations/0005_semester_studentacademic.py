# Generated by Django 5.2 on 2025-05-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_gpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('academic_year', models.CharField(max_length=9)),
                ('term', models.SmallIntegerField()),
                ('term_label', models.CharField(max_length=50)),
                ('is_current', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'semesters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAcademic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=10)),
                ('course_title', models.CharField(max_length=255)),
                ('credit_hours', models.IntegerField()),
                ('grade', models.CharField(blank=True, max_length=2, null=True)),
                ('gpa_points', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('status', models.CharField(default='In Progress', max_length=20)),
            ],
            options={
                'db_table': 'student_academics',
                'managed': False,
            },
        ),
    ]
