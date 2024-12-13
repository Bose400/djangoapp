from django.db import models

# Base Model for common attributes
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True

# Teacher model
class Teacher(Person):
    hire_date = models.DateField()
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Student model
class Student(Person):
    enrollment_date = models.DateField()
    grade_level = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='subjects')

    def __str__(self):
        return self.name

# Class model
class Class(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    students = models.ManyToManyField(Student, related_name='classes')
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes_taught')

    def __str__(self):
        return f"{self.name} ({self.year})"

# Assignment model for tracking student submissions
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return self.title

# Submission model
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    submitted_date = models.DateField()
    grade = models.CharField(max_length=10, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.first_name} {self.student.last_name}"

# Attendance model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.date}"

# Exam model
class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')

    def __str__(self):
        return self.name

# Exam Result model
class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.exam.name}"

# Administrative staff model
class AdministrativeStaff(Person):
    role = models.CharField(max_length=50)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
