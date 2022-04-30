from django.views.generic import TemplateView


# Create your views here.
class MentoringView(TemplateView):
    template_name = "mentoring.html"

class ProblemsView(TemplateView):
    template_name = "practice_questions.html"

class MaterialsView(TemplateView):
    template_name = "interview_materials.html"
