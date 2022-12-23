from django.urls import path

from demoday.views import TeamView

urlpatterns = [
    path('', TeamView.as_view())
]