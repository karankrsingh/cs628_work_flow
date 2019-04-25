from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


from .models import Report, Teacher, Student, TeacherMeet
# from uploads.core.forms import DocumentForm

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
    # students = Student.objects.all()
    students = Student.objects.filter(std_teacher_id=1)
    return render(request, 'core/for_teacher.html', {'students': students})
#
# def for_student_meeting(request):
#     students = Students.objects.all()
#     documents = Document.objects.all()
#     return render(request, 'core/for_teacher.html', {'students': students,'documents': documents})
