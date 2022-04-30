from django.urls import path

from mentoring import views

urlpatterns = [
    path("", views.MentoringView.as_view(), name="mentoring-home"),
    path("interviewing/questions/", views.ProblemsView.as_view(), name="interview-problems"),
    path("interviewing/materials/", views.MaterialsView.as_view(), name="interview-materials"),
]
