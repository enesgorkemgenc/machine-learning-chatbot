from django.urls import path
from . import views
urlpatterns = [
    path("", views.get_homepage, name="homepage"),
    path("data/", views.get_data_page, name="data-page")
]