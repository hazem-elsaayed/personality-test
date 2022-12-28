from django.urls import include, path
from rest_framework import routers
from quiz.views import QuestionView, ResultsView

router = routers.DefaultRouter()
router.register(r'question', QuestionView)

urlpatterns = [
    path('', include(router.urls)),
    path('result', ResultsView.as_view({'post': 'result'}))
]