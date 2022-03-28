from django.urls import path, re_path

from bboard import views

urlpatterns = [
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('', views.index, name='index'),
]
