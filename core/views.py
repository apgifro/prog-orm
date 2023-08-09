from django.views.generic.list import ListView

from core.models import Turma


class TurmaReadView(ListView):
    model = Turma
    context_object_name = 'turmas'
    template_name = 'turma/read.html'

