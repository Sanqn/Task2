from rest_framework import routers

from django.urls import path, include

from django.conf.urls.static import static

from django.conf import settings

from .views import WbDataViews

router = routers.DefaultRouter()
router.register('wbdata', WbDataViews, basename='wbdata')

urlpatterns = [
                  path('', include(router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
