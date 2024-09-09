from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.throttling import ScopedRateThrottle
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-data/',views.StudentList.as_view()),
    # path('student-data/',views.StudentListCreate.as_view()),
    # path('student-data/',views.StudentCreate.as_view()),
    # path('student-data/<int:pk>',views.StudentRetrieve.as_view()),
    path('student-data/<int:pk>',views.StudentUpdate.as_view()),
    # path('student-data/<int:pk>',views.StudentDelete.as_view()),
]
