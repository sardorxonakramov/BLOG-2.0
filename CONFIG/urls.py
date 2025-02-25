from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path("", lambda request: HttpResponse("Hello, World!"), name="home"),
]

