from django.urls import path

from partleads.views import CandidateView

urlpatterns = [
    path('', CandidateView.as_view())
]