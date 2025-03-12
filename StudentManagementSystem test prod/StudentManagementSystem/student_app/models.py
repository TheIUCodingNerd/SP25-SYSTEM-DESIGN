from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Unique Student ID
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.student_id} - {self.name}"  # ✅ Displays ID + Name in admin panel


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]  # ✅ Fixed: Choices now properly closed

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)  # Class Name
    grade_section = models.CharField(max_length=10)  # Section (e.g., A, B, C)
    score = models.FloatField()  # ✅ Fixed: 'score' now correctly defined

    def __str__(self):
        return f"{self.student.name} - {self.subject} - {self.grade_section} - {self.score}%"
