from django.urls import path
from .views import *


urlpatterns = [
    path('create', ResumeView.as_view(), name='create-resume'),
    path('delete/<int:pk>/', DeleteResume.as_view(), name='delete'),
    path('profile', ProfileView.as_view()),
    path('profileD/<int:pk>/', DetailProfile.as_view()),
    path('links', CreateLinks.as_view()),
    path('lLinks', ListLinks.as_view()),
    path('links/<int:id>', GetLinks.as_view()),
    path('wrkExp', CreateWorkExperience.as_view()),
    path('wrkExpU/<int:id>', UpdateWorkExperience.as_view()),
    path('eduHis', CreateEducationalHistory.as_view()),
    path('eduHisU/<int:id>', UpdateEducationHistory.as_view()),
    path('createAwd', CreateAwards.as_view()),
    path('awdList', ListAwards.as_view()),
    path('awdU/<int:id>', UpdateAwards.as_view()),
]
