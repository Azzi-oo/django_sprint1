from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls'), name='blog'),
    path('', include('pages.urls'), name='pages'),
    path('admin/', admin.site.urls),
]
