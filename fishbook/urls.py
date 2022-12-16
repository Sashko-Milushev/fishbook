from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include


from fishbook.exception_handling import page_not_found, server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fishbook.common.urls')),
    path('accounts/', include('fishbook.accounts.urls')),
    path('fish/', include('fishbook.fish.urls')),
    path('photos/', include('fishbook.photos.urls')),
    path('lakes/', include('fishbook.lakes.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = page_not_found
handler500 = server_error
