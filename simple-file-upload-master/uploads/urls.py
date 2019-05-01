from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^teacher/', views.for_teacher, name='for_teacher'),
    url(r'^student_meeting/', views.for_student_meeting, name='for_student_meeting'),
    url(r'^admin/', admin.site.urls),
    url(r'^week/', views.week_wise_view),
    url(r'^student_view/', views.student_view, name='student_view'),
    url(r'^teacher_student_view/', views.teacher_student_view, name='teacher_student_view'),
    url(r'^graph/', views.student_graph_display),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
