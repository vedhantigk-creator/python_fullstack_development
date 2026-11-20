
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import StudentForm
from .models import Student


# Student Registration
@login_required(login_url='login')
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )


# Student List
@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )


# Login
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(
            request,
            'students/login.html',
            {'error': 'Invalid Username or Password'}
        )

    return render(request, 'students/login.html')


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    total_students = Student.objects.count()

    total_departments = Student.objects.values(
        'department'
    ).distinct().count()

    context = {
        'total_students': total_students,
        'total_departments': total_departments,
    }

    return render(
        request,
        'students/dashboard.html',
        context
    )


# Logout
@login_required(login_url='login')
def logout_page(request):
    if request.method == 'POST':
        logout(request)

    return redirect('login')
