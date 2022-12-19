from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ResumeView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DeleteResume(generics.DestroyAPIView):
    authentication_classes = []
    queryset = Links.objects.all()
    serializer_class = ResumeSerializer


class ProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DetailProfile(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)


# class DetailProfile(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


class CreateLinks(generics.CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListLinks(generics.ListAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Links.objects.all()

    def get_queryset(self):
        return Links.objects.filter(owner=self.request.user)


class GetLinks(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Links.objects.all()
    serializer_class = LinkSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Links.objects.filter(owner=self.request.user)


class CreateWorkExperience(generics.CreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdateWorkExperience(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return WorkExperience.objects.filter(owner=self.request.user)


class CreateEducationalHistory(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdateEducationHistory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return WorkExperience.objects.filter(owner=self.request.user)


class CreateAwards(generics.CreateAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListAwards(generics.ListAPIView):
    serializer_class = AwardSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Awards.objects.all()

    def get_queryset(self):
        return Awards.objects.filter(owner=self.request.user)


class UpdateAwards(generics.RetrieveUpdateDestroyAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Awards.objects.filter(owner=self.request.user)
