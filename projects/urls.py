from django.urls import path
from . immport views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    pahh("<int:pk>/", views.project_detail, name="project_detail"),
]