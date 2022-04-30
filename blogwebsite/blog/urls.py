from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostView.as_view(), name='post_detail'),
]