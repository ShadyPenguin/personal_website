from django.http import FileResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

class ResumeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return FileResponse(open('static/jake-sikora-resume.pdf', 'rb'), content_type='application/pdf')
