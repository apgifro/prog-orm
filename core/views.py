from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.list import ListView

from core.models import Turma, Aluno


class FaculdadeIndexView(TemplateView):
    template_name = 'index.html'


class TurmaReadView(ListView):
    model = Turma
    context_object_name = 'turmas'
    template_name = 'turma/read.html'
    ordering = ['-id']


class TurmaCreateView(SuccessMessageMixin, CreateView):
    model = Turma
    fields = ["nome", "turno"]
    template_name = 'turma/create.html'
    success_url = reverse_lazy("turma_read")
    success_message = "%(nome)s criado com sucesso!"


class TurmaUpdateView(SuccessMessageMixin, UpdateView):
    model = Turma
    fields = ["nome", "turno"]
    template_name = 'turma/update.html'
    success_url = reverse_lazy("turma_read")
    success_message = "%(nome)s atualizado com sucesso!"


class TurmaDeleteView(SuccessMessageMixin, DeleteView):
    model = Turma
    template_name = 'turma/delete.html'
    success_url = reverse_lazy("turma_read")
    success_message = "Ecluído com sucesso!"


class AlunoReadView(ListView):
    model = Aluno
    context_object_name = 'alunos'
    template_name = 'aluno/read.html'
    ordering = ['-id']


class AlunoCreateView(SuccessMessageMixin, CreateView):
    model = Aluno
    fields = ["nome", "sobrenome", "endereco", "dtnasc", "turma"]
    template_name = 'aluno/create.html'
    success_url = reverse_lazy("aluno_read")
    success_message = "%(nome)s criado com sucesso!"


class AlunoUpdateView(SuccessMessageMixin, UpdateView):
    model = Aluno
    fields = ["nome", "sobrenome", "endereco", "dtnasc", "turma"]
    template_name = 'aluno/update.html'
    success_url = reverse_lazy("aluno_read")
    success_message = "%(nome)s atualizado com sucesso!"


class AlunoDeleteView(SuccessMessageMixin, DeleteView):
    model = Aluno
    template_name = 'aluno/delete.html'
    success_url = reverse_lazy("aluno_read")
    success_message = "Excluído com sucesso!"

