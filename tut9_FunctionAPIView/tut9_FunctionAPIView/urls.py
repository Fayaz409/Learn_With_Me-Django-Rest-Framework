from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-data/',views.hello_world),
    # path('post/',views.hello_world2),
]
