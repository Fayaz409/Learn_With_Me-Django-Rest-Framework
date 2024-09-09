from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from api import views

router=DefaultRouter()
router.register('student-api',views.StudentAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get-token/',TokenObtainPairView.as_view()),
    path('refresh-token/',TokenRefreshView.as_view()),
    path('verify-token/',TokenVerifyView.as_view())
]
