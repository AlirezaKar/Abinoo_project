from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse
def test_view(request):
    return HttpResponse("🚀 Django is working on Render!")

def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
