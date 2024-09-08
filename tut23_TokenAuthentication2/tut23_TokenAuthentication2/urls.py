from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api import views

router=DefaultRouter()
router.register('student-api',views.StudentAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get-token/',obtain_auth_token)
]
