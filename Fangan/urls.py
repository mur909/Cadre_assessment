from django.urls import path
from .views import AutoGenerate,EvaluateScore,Weight

urlpatterns = [
    path('auto_generate', AutoGenerate.as_view()),
    path('evaluate_score', EvaluateScore.as_view()),

    path('Weight/<str:DB>', Weight.as_view()),

]