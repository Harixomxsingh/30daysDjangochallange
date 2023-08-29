from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="tasks"),
    path("<int:pk>/", views.detailView, name="task"),
]
