from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-data/',views.StudentListCreate.as_view()),
    path('student-data/<int:pk>', views.StudentRetrieveUpdateDelete.as_view()),
]
