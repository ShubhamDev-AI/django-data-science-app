
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home_view, name='home'),
    path('performance/', include('products.urls', namespace='products')),
    path('upload/', include('csvs.urls', namespace='csvs')),
    path('customers/', include('customers.urls', namespace='customers')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
