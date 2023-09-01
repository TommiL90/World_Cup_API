from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from teams.exceptions import (
    ImpossibleTitlesError,
    InvalidYearCupError,
    NegativeTitlesError,
)
from teams.models import Team
from teams.utils import data_processing


# Create your views here.
class TeamsView(APIView):
    def post(self, request):
        try:
            team_data = data_processing(request.data)
        except NegativeTitlesError as err:
            return Response({"error": str(err)}, 400)
        except InvalidYearCupError as err:
            return Response({"error": str(err)}, 400)
        except ImpossibleTitlesError as err:
            return Response({"error": str(err)}, 400)
  
        team = Team(**team_data)

        team.save()

        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()

        teams_dict = [model_to_dict(team) for team in teams]

        return Response(teams_dict, 200)


class TeamsDetailsView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team_dict = model_to_dict(team)

        return Response(team_dict)
    
    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        
        data = request.data

        for key, value in data.items():
            if hasattr(team, key):
                setattr(team, key, value)

        team.save()

        team_dict = model_to_dict(team)

        return Response(team_dict, 200)
    
    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        
        team.delete()

        return Response(status=204)

