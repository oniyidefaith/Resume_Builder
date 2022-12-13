from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class ProfileView(generics.CreateAPIView):
    authentication_classes = []
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DetailProfile(generics.RetrieveUpdateAPIView):
    authentication_classes = []
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class DetailProfile(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


class CreateLinks(generics.CreateAPIView):
    authentication_classes = []
    queryset = Links.objects.all()
    serializer_class = LinkSerializer


class GetLinks(generics.RetrieveUpdateAPIView):
    authentication_classes = []
    queryset = Links.objects.all()
    serializer_class = LinkSerializer


class DeleteLinks(generics.DestroyAPIView):
    authentication_classes = []
    queryset = Links.objects.all()
    serializer_class = LinkSerializer


class CreateWorkExperience(generics.CreateAPIView):
    authentication_classes = []
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class UpdateWorkExperience(generics.RetrieveUpdateAPIView):
    authentication_classes = []
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class DeleteWorkExperience(generics.DestroyAPIView):
    authentication_classes = []
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class CreateEducationalHistory(generics.CreateAPIView):
    authentication_classes = []
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class UpdateEducationHistory(generics.RetrieveUpdateAPIView):
    authentication_classes = []
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class DeleteEducationalHistory(generics.DestroyAPIView):
    authentication_classes = []
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
