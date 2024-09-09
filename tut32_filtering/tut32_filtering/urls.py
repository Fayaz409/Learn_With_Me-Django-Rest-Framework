from django.contrib import admin
from django.urls import path
from api import views
# Pakistan1209@#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-api/',views.StudentList.as_view())
]
