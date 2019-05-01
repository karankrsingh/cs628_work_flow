from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Report, Teacher, Student, TeacherMeet
import django.db

from .forms import DocumentForm

def home(request):
    return HttpResponse("<h1>hello!!!!!!!!!!</h1>")
    # documents = Document.objects.all()
    # return render(request, 'core/home.html', {'documents': documents})


#
# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'core/simple_upload.html')
#
#
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


def for_teacher(request):
    # take input teacher_id and show list of students
    students = Student.objects.filter(std_teacher_id=1)
    return render(request, 'core/for_teacher.html', {'students': students})


def for_student_meeting(request):
    # take input roll_no and week number

    prim = TeacherMeet.objects.get(week_id=7,meet_student_roll=10003)
    # docrecord = get_object_or_404(Report, report_meet_id=prim.id)
    docrecord = Report.objects.filter(report_meet_id=prim.id)

    if(docrecord):
        return render(request, 'core/for_previous_meeting.html', {'docrecord': docrecord,'record':prim})
    else:
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newobject = Report()
                newobject.report_meet_id=prim
                newobject.description=form.cleaned_data['description']
                newobject.document=form.cleaned_data['document']
                newobject.save()
                return redirect('for_student_meeting')
        else:
            form = DocumentForm()
        return render(request, 'core/for_student_meeting.html', {'record': prim,'form':form })



num = range(1, 11)


def week_wise_view(request):
    return render(request, 'core/week_wise_view.html', {'num': num})


def student_view(request):
    return render(request, 'core/student_view.html')

def student_graph_display(request):
    return render(request, 'core/student_graph_display.html')
