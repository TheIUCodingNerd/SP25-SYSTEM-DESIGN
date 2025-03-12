from django.shortcuts import render, redirect
from .models import Student, Grade

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        subject = request.POST['subject']
        grade_section = request.POST['grade_section']
        score = request.POST['score']

        student = Student.objects.create(name=name, contact=contact, email=email)
        Grade.objects.create(student=student, subject=subject, grade_section=grade_section, score=score)

        return redirect('student_list')

    return render(request, 'student_app/add_student.html')
