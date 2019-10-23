from django.shortcuts import render, redirect
from vote.models import Subject, Teacher

# Create your views here.
def show_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_index.html', {'subjects' : subjects})

def show_teachers(request):
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = subject.teacher_set.all()
        return render(request, 'teacher_index.html', {'subject' : subject, 'teachers' : teachers})
    except:
        return redirect('/')