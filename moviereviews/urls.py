
from django.contrib import admin
from django.urls import path,include
from movie import views as movie_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',movie_views.home, name='home'),
    path('about/',movie_views.about),
    path('news/', include('news.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
