from django.shortcuts import render
from django.views.generic import TemplateView
from project.data.project import project_data


class ProjectView(TemplateView):
    template_name = 'project/project.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'project_data': project_data})

