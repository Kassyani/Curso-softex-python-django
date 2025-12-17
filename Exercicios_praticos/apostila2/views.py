from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(ModelViewSet):
    serializer_class = TarefaSerializer

    def get_queryset(self):
        return Tarefa.objects.filter(deletada=False)

    @action(detail=False, methods=['get'])
    def estatisticas(self, request):
        dados = Tarefa.objects.filter(deletada=False).aggregate(
            total=Count('id'),
            concluidas=Count('id', filter=models.Q(concluida=True))
        )

        total = dados['total'] or 0
        concluidas = dados['concluidas'] or 0
        pendentes = total - concluidas
        taxa_conclusao = concluidas / total if total > 0 else 0

        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes,
            'taxa_conclusao': round(taxa_conclusao, 2)
        })

   
    @action(detail=True, methods=['patch'])
    def deletar(self, request, pk=None):
        tarefa = self.get_object()
        tarefa.deletada = True
        tarefa.save()
        return Response({'detail': 'Tarefa deletada com sucesso.'})
