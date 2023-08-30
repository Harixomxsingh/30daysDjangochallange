from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="tasks"),
    path("<int:pk>/", views.detailView, name="task"),
    path("create/", views.create_todo, name="create"),
    path("update/<int:pk>", views.update_todo, name="update"),
    path("delete/<int:pk>", views.delete_todo, name="delete"),
]
