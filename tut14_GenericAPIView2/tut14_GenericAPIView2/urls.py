from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-data/',views.LCStudentAPI.as_view()),
    path('student-data/<int:pk>',views.RUDStudentRetieve.as_view())
]
