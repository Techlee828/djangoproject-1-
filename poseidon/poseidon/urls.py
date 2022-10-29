from django.contrib import admin
from django.urls import path,include
from website.views import welcome
from valve.views import new,command,commandposeidon


urlpatterns = [
    path('', welcome),
    path('admin/', admin.site.urls),
      # sends welcome view too user
    path('welcome', welcome),
    path('new', new),
    path('command',command),
    path('commandposeidon', commandposeidon)
]
