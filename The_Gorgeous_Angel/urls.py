from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin


urlpatterns = [

       
    path('admin/', admin.site.urls),
    path('adminpannel/', include('adminpannel.urls')),
    path('customer/', include('customer.urls')),
    path('customerapi/', include('customerapi.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)