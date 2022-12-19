from rest_framework import serializers
from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateResume
        fields = ('name', 'slug')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'Image', 'Full_Name', 'Date', 'email', 'Phone', 'Gender', 'Description', 'Summary', 'Address', 'City',
            'Region', 'Country', 'Postal')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('id', 'Title', 'Website')


class WorkExperienceSerializer(serializers.ModelSerializer):
    present = models.BooleanField(default=False)

    class Meta:
        model = WorkExperience
        fields = ('id', 'Title', 'Position', 'Employer', 'Url', 'StartDate', 'EndDate', 'Website', 'Summary', 'present')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'id', 'Institute', 'Degree', 'School', 'URL', 'City', 'Country', 'StartDate', 'EndDate', 'Description')


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = ('id', 'Title', 'Issuer', 'URL', 'Date', 'Description')
