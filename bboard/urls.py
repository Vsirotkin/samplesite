from django.urls import path, re_path
from .views import by_rubric
from bboard import views

urlpatterns = [
    path('<int:rubric_id>/', by_rubric),
    path('', views.index, name='home'),
]