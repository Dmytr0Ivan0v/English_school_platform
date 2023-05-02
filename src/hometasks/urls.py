from django.urls import path
from hometasks import views

app_name = "hometask"

urlpatterns = [
    path("", views.hometasks_list, name="hometasks_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:hometask>/", views.hometask_retrieve, name="hometask_retrieve"),
]
