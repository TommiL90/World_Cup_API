from django.urls import path
from teams.views import TeamsDetailsView, TeamsView

urlpatterns = [
    path('teams/', TeamsView.as_view()),
    path('teams/<int:team_id>/', TeamsDetailsView.as_view())
]