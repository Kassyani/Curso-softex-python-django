
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
            'concluida',
            'data_conclusao',
            'user'
        ]

    def validate(self, data):
        instance = self.instance

        
        if instance:
            prioridade = instance.prioridade
            concluida_atual = instance.concluida
            concluida_nova = data.get('concluida', concluida_atual)

            if (
                prioridade == 'alta'
                and not concluida_atual
                and concluida_nova
                and self.context['request'].method == 'PATCH'
            ):
                raise serializers.ValidationError(
                    'Tarefas de prioridade alta só podem ser concluídas via PUT.'
                )

        return data

    def update(self, instance, validated_data):
        
        concluida = validated_data.get('concluida', instance.concluida)

        if concluida and not instance.data_conclusao:
            instance.data_conclusao = date.today()

        if not concluida:
            instance.data_conclusao = None

        return super().update(instance, validated_data)
