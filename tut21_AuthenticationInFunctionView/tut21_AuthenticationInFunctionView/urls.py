from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-data/',views.student_api),
    path('student-data/<int:pk>',views.student_api)
]
