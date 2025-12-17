# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Tarefa.objects.filter(user_id=user_id)
        return Tarefa.objects.all()

    @action(detail=False, methods=['get'])
    def contagem(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas

        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes
        })
