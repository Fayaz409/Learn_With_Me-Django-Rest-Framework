from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api import views
from api.auth import CustomAuthToken
router=DefaultRouter()
router.register('student-api',views.StudentAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get-token/',CustomAuthToken.as_view())
]
