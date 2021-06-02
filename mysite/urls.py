from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.contrib.auth import urls as authurls
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django_private_chat import urls as django_private_chat_urls
from chat.views import HomeView, logout_request, login_request, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),

    path('accoutns/',include('allauth.urls')),
    path('', include(django_private_chat_urls)),
    path('',HomeView.as_view(), name='Home'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path("register/",register,name="register"),


    url('chat/', include('chat.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)