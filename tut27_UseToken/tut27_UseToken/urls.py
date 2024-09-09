from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('student-api',views.StudentAPI)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get-token/',include('rest_framework.urls')),
    
]
