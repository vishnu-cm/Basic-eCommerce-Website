from msilib.sequence import AdminUISequence
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

#from apppannel import views
#from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', AdminUISequence.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)