from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Student, Course, Instructor
from .forms import CourseForm, InstructorForm, CourseInstructorForm
from django.views.generic.edit import DeleteView

def index(request):
    all_classes = Course.objects.all()
    context = {
        'all_classes': all_classes,
    }
    return render(request, 'scheduler/index.html', context)
    #HttpResponse built into render

def detail(request, class_id):
    try: 
        course = Course.objects.get(class_id = class_id)
    except Course.DoesNotExist:
        raise Http404("That class does not exist.")
    return render(request, 'scheduler/detail.html', {'course': course})                                     

def show_courses(request):
    all_courses = Course.objects.all()
    return render(request, 'scheduler/show_courses.html', {'all_courses':all_courses})

def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        form.save()
        return redirect('show_courses')
    else:
        form = CourseForm()
        return render(request, 'scheduler/add.html',{'title':'Class Name','form':form})

def show_instructors(request):
    all_instructors = Instructor.objects.all()
    return render(request, 'scheduler/show_instructors.html',{'all_instructors':all_instructors})

def edit_instructors(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseInstructorForm(request.POST,instance=course)
        form.save()
        return redirect('show_courses')
    else:
        form = CourseInstructorForm()
        return render(request, 'scheduler/edit_instructors.html',{'form':form,'course':course})

def add_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        form.save()
        return redirect('show_instructors')
    else:
        form = InstructorForm()
        return render(request, 'scheduler/add.html',{'title':'instructor','form':form})

def delete(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.delete()
    return redirect('show_courses')