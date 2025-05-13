from django.urls import path
from .views import (
    CandidateApplicationCreateView,
    CandidateApplicationDetailView,
    DelegateApplicationCreateView,
    DelegateApplicationDetailView
)

urlpatterns = [
    path('candidate/apply/', CandidateApplicationCreateView.as_view(), name='candidate-apply'),
    path('candidate/details/', CandidateApplicationDetailView.as_view(), name='candidate-details'),
    path('delegate/apply/', DelegateApplicationCreateView.as_view(), name='delegate-apply'),
    path('delegate/details/', DelegateApplicationDetailView.as_view(), name='delegate-details'),
]
