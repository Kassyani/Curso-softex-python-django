
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


    @action(detail=True, methods=['post'])
    def duplicar(self, request, pk=None):
        tarefa = self.get_object()

        tarefa.pk = None
        tarefa.concluida = False
        tarefa.data_conclusao = None
        tarefa.save()

        serializer = self.get_serializer(tarefa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['patch'], url_path='concluir-todas')
    def concluir_todas(self, request):
        tarefas = Tarefa.objects.filter(concluida=False)

        for tarefa in tarefas:
            tarefa.concluida = True
            tarefa.data_conclusao = date.today()
            tarefa.save()

        return Response(
            {'detail': f'{tarefas.count()} tarefas concluídas.'}
        )
