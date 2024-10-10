from django.urls import path
from . import views
from .views import about, how_to_use

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('about/', about, name='about'),
    path('how-to-use/', how_to_use, name='how_to_use'),
]
