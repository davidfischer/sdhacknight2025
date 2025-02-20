from django.urls import path

from . import views


urlpatterns = [
    path(
        r"",
        views.HomePageView.as_view(template_name="sdhacknight/index.html"),
        name="index",
    ),
]
