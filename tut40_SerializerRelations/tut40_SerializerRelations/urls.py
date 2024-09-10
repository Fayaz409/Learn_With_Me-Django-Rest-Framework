from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('singer-api',views.SingerViewSet)
router.register('song-api',views.SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
