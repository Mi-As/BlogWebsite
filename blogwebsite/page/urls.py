from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.DefaultPage.as_view(), name='default_page'),
]