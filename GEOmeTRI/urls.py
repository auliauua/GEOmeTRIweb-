from django.contrib import admin
from django.urls import path
from home.views import datar, ruang, tokoh, soal, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('datar/', datar),
    path('ruang/', ruang),
    path('tokoh/', tokoh),
    path('soal/', soal),
]
