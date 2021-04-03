from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from posts import views as posts_views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^posts/', include("posts.urls")),
    url(r'^$',views.homepage,name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)