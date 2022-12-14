from django.urls import path
from .views import *


urlpatterns = [
    path('create', ResumeView.as_view(), name='create-resume'),
    path('delete/<int:pk>/', DeleteResume.as_view(), name='delete'),
    path('profile', ProfileView.as_view(), name='create-profile'),
    path('profileD/<int:pk>/', DetailProfile.as_view(), name='profile-details'),
    path('links', CreateLinks.as_view(), name='create-links'),
    path('lLinks', ListLinks.as_view(), name='list-links'),
    path('links/<int:id>', GetLinks.as_view(), name='get-links'),
    path('wrkExp', CreateWorkExperience.as_view(), name='create-work-experience'),
    path('wrkExpU/<int:id>', UpdateWorkExperience.as_view(), name='update-work-experience'),
    path('eduHis', CreateEducationalHistory.as_view(), name='create-educational-history'),
    path('eduHisU/<int:id>', UpdateEducationHistory.as_view(), name='update-educational-history'),
    path('createAwd', CreateAwards.as_view(), name='create-award'),
    path('awdList', ListAwards.as_view(), name='list-awards'),
    path('awdU/<int:id>', UpdateAwards.as_view(), name='update-awards'),
    path('certificate', CreateCertificate.as_view(), name='create-certificate'),
    path('lCertificate', ListCertificate.as_view(), name='list-certificate'),
    path('certificateU/<int:id>', UpdateCertificates.as_view(), name='update-awards'),
    path('publication', CreatePublication.as_view(), name='create-publication'),
    path('lPublication', ListPublication.as_view(), name='list-publication'),
    path('publicationU/<int:id>', UpdatePublication.as_view(), name='update-publication'),
    path('skill', CreateSkills.as_view(), name='create-skill'),
    path('lSkill', ListSkill.as_view(), name='list-skill'),
    path('skillU/<int:id>', UpdateSkill.as_view(), name='update-skill'),
    path('language', CreateLanguage.as_view(), name='create-language'),
    path('lLanguage', ListLanguage.as_view(), name='list-language'),
    path('languageU/<int:id>', UpdateLanguage.as_view(), name='update-language'),
    path('interest', CreateInterest.as_view(), name='create-interest'),
    path('lInterest', ListInterest.as_view(), name='list-interest'),
    path('interestU/<int:id>', UpdateInterest.as_view(), name='update-interest'),
    path('volunteer', CreateVolunteerView.as_view(), name='create-volunteer-experience'),
    path('lVolunteer', ListVolunteerView.as_view(), name='list-volunteer-experience'),
    path('volunteerU/<int:id>', UpdateVolunteerView.as_view(), name='update-volunteer-experience'),
    path('project', CreateProjectView.as_view(), name='create-projects'),
    path('lProject', ListProjects.as_view(), name='list-project'),
    path('projectU/<int:id>', UpdateProjectView.as_view(), name='update-projects'),
    path('reference', CreateReferenceView.as_view(), name='create-reference'),
    path('lReference', ListReference.as_view(), name='list-reference'),
    path('referenceU/<int:id>', UpdateReference.as_view(), name='update-reference'),

]

