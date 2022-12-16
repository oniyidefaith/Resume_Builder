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
            'Image', 'Full_Name', 'Date', 'email', 'Phone', 'Gender', 'Description', 'Summary', 'Address', 'City',
            'Region', 'Country', 'Postal')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('Title', 'Website')


class WorkExperienceSerializer(serializers.ModelSerializer):
    present = models.BooleanField(default=False)

    class Meta:
        model = WorkExperience
        fields = ('Title', 'Position', 'Employer', 'Url', 'StartDate', 'EndDate', 'Website', 'Summary', 'present')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'Institute', 'Degree', 'School', 'URL', 'City', 'Country', 'StartDate', 'EndDate', 'Description')
