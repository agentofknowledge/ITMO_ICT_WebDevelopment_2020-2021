from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class WarriorAPIView(APIView):
    
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

        
class ProfessionCreateView(APIView):
    
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)
        
        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()
            
        return Response({"Success": "Profession '{}' created".format(profession_saved.title)})
        

class SkillAPIView(APIView):
    
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})
        


class SkillCreateView(APIView):
    
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)
        
        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()
            
        return Response({"Success": "Skill '{}' created".format(skill_saved.title)})
        

        
