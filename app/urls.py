from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name="Home"),
    path('tool/<int:num>',views.tool, name="Tool"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
