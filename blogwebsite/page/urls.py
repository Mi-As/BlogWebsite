from . import views
from django.urls import path
from django.conf.urls import handler404

urlpatterns = [
    path('<slug:slug>/', views.DefaultPage.as_view(), name='default_page'),
]


