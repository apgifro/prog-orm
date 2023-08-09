from django.urls import path

import views

urlpatterns = [
    path('', views.FaculdadeIndexView.as_view(), name='index'),

    path("turma/", views.TurmaReadView.as_view(), name="turma_read"),
    path("aluno/", views.AlunoReadView.as_view(), name="aluno_read"),

    path("turma/criar/", views.TurmaCreateView.as_view(), name="turma_create"),
    path("aluno/criar/", views.AlunoCreateView.as_view(), name="aluno_create"),

    path("turma/atualizar/<int:pk>/", views.TurmaUpdateView.as_view(), name="turma_update"),
    path("aluno/atualizar/<int:pk>/", views.AlunoUpdateView.as_view(), name="aluno_update"),

    path("turma/excluir/<int:pk>/", views.TurmaDeleteView.as_view(), name="turma_delete"),
    path("aluno/excluir/<int:pk>/", views.AlunoDeleteView.as_view(), name="aluno_delete"),
]
