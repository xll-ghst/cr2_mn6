from django.urls import path
from .views import RegisterView, StatsView
urlpatterns = [
    path("stats/", StatsView.as_view(), name="monitoring-stats"),
    path("register/", RegisterView.as_view(), name="monitoring-register"),
]
