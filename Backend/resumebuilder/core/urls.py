from django.urls import path
from .views import *


urlpatterns = [
    path('create', ResumeView.as_view(), name='create-resume'),
    path('profile', ProfileView.as_view()),
    path('profileD/<int:pk>/', DetailProfile.as_view()),
    path('links', CreateLinks.as_view()),
    path('linksU/<int:pk>/', GetLinks.as_view()),
    path('linksD/<int:pk>/', DeleteLinks.as_view()),
    path('wrkExp', CreateWorkExperience.as_view()),
    path('wrkExpU/<int:pk>/', UpdateWorkExperience.as_view()),
    path('wrkExpD/<int:pk>/', DeleteWorkExperience.as_view()),
    path('eduHis', CreateEducationalHistory.as_view()),
    path('eduHisU/<int:pk>/', UpdateEducationHistory.as_view()),
    path('eduHisD/<int:pk>/', DeleteEducationalHistory.as_view()),

]
