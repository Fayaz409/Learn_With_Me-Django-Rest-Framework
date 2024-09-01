from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-info/<int:pk>',views.student_detail,name='student-info'),
    path('all-students/',views.students_all_detail,name='all-students')
]
