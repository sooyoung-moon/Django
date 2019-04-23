from django.urls import path
from . import views

urlpatterns =[
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='post_detail')
]