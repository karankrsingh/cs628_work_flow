from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Report, Teacher, Student, TeacherMeet
import django.db
from itertools import chain
from .forms import DocumentForm,MeetingForm

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

def schedule_meeting(request):
    #input week and roll number

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        weekid=7
        rollno=10001
        row=Student.objects.get(student_roll=rollno)
        if form.is_valid():
            newobject = TeacherMeet()
            newobject.week_id=weekid
            newobject.meet_student_roll=row
            newobject.schedule_date = form.cleaned_data['schedule_date']
            newobject.future_work = form.cleaned_data['future_work']
            newobject.save()
            return redirect('/teacher_student_view')
    else:
        form = MeetingForm()
    return render(request, 'core/schedule_meeting.html', {
        'form': form
    })



def for_teacher(request):
    # take input teacher_id and show list of students
    students = Student.objects.filter(std_teacher_id=1)
    return render(request, 'core/for_teacher.html', {'students': students})


def for_student_meeting(request):
    # take input roll_no and week number
    # weekid=request.GET['number']
    forcheck = TeacherMeet.objects.filter(week_id=request.POST.get('week_number'), meet_student_roll=10001)
    if(forcheck):
        prim = TeacherMeet.objects.get(week_id=request.POST.get('week_number'),meet_student_roll=10001)
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

    else:
        return HttpResponse("Meeting not scheduled yet")

def teacher_student_view(request):
    # input roll no of student
    details_of_meet = TeacherMeet.objects.filter(meet_student_roll=10003)
    # print(details_of_meet[1].week_id)
    counter_past=0
    counter_present=0
    counter_zero=0;
    reportquery=Report.objects.none()
    teacherquery = TeacherMeet.objects.none()

    marks_report_list=[]
    marks_teacher_list=[]

    no_marks_report_list=[]
    no_marks_teacher_list=[]

    only_scheduled_list=[]

    # print(newquery)
    # print(details_of_meet)
    for obj in details_of_meet:
        # counter_past=counter_past+1
        temp=Report.objects.filter(report_meet_id=obj.id)
        if(temp):
            # counter_present=counter_present+1
            for x in temp:
                if(x.marks):
                    marks_teacher_list.append(obj)
                    marks_report_list.append(x)
                else:
                    no_marks_teacher_list.append(obj)
                    no_marks_report_list.append(x)
        else:
            only_scheduled_list.append(obj)

    marks_report_query_add=list(chain(reportquery,marks_report_list))
    marks_teacher_query_add=list(chain(teacherquery,marks_teacher_list))

    no_marks_report_query_add=list(chain(reportquery,no_marks_report_list))
    no_marks_teacher_query_add=list(chain(teacherquery,no_marks_teacher_list))

    only_scheduled_query=list(chain(teacherquery,only_scheduled_list))
    marks_given_all=zip(marks_teacher_query_add,marks_report_query_add)
    no_marks_given_all=zip(no_marks_teacher_query_add,no_marks_report_query_add)

    return render(request,'core/teacher_student_view.html',{'a':marks_given_all,'b':no_marks_given_all,'only_scheduled':only_scheduled_query})
    # details_of_report=Report.objects.filter()



num = range(1, 11)


def week_wise_view(request):
    return render(request, 'core/week_wise_view.html', {'num': num})


def student_view(request):

    return render(request, 'core/student_view.html')

def student_graph_display(request):

    details_of_meet = TeacherMeet.objects.filter(meet_student_roll=10001)
    marks=[]
    week=[]
    for obj in details_of_meet:
        week.append(obj.week_id)
        temp = Report.objects.filter(report_meet_id=obj.id)
        if (temp):
            print(temp)
            for x in temp:
                if(x.marks):
                    marks.append(x.marks)
    zippedlist = zip(week, marks)
    return render(request, 'core/student_graph_display.html', {'zippedlist': zippedlist})