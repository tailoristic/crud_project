from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User

# ! CREATE AND READ


def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(name=name, email=email, password=password)
            user.save()
            form = StudentRegistration()

    else:
        form = StudentRegistration()

    students = User.objects.all()
    context = {'form': form, 'students': students}
    return render(request, 'enroll/home_page.html', context)

# ! UPDATE


def update_data(request, id):
    if request.method == 'POST':
        user_data = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=user_data)
        if form.is_valid():
            form.save()
    else:
        user_data = User.objects.get(pk=id)
        form = StudentRegistration(instance=user_data)

    context = {'form': form}
    return render(request, 'enroll/updatestudent_page.html', context)

# ! DELETE


def delete_data(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()
        return redirect('/')
