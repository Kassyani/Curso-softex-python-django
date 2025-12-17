from rest_framework import serializers
from datetime import date
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = [
            'id',
            'titulo',
            'descricao',
            'prioridade',
            'prazo',
            'concluida',
            'deletada',
            'user'
        ]

    def validate_prioridade(self, value):
        prioridades_validas = ['baixa', 'media', 'alta']
        if value not in prioridades_validas:
            raise serializers.ValidationError(
                'Prioridade inválida. Use: baixa, media ou alta.'
            )
        return value

   
    def validate(self, data):
        prazo = data.get('prazo')
        concluida = data.get('concluida', False)

    
        if prazo and prazo < date.today():
            raise serializers.ValidationError(
                {'prazo': 'O prazo não pode ser no passado.'}
            )

       
        if not concluida and not prazo:
            raise serializers.ValidationError(
                {'prazo': 'Prazo é obrigatório para tarefas não concluídas.'}
            )

        return data
