from django.urls import path

from .views import TurmaReadView

urlpatterns = [
    path("turma/", TurmaReadView.as_view(), name="turma_read"),
    path("turma/criar/", TurmaCreateView.as_view(), name="turma_create"),
    # path("turma/atualizar/", TurmaUpdateView.as_view(), name="turma_update"),
    # path("turma/excluir/", TurmaDeleteView.as_view(), name="turma_delete"),
]
