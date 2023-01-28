from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('book/', include('book_app.urls')),
    path('package/', include('package_app.urls')),
    path('services/', include('services_app.urls')),
    path('gallery/', include('gallery_app.urls')),
    path('contact/', include('contact_app.urls')),
    path('blog/', include('blog_app.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)