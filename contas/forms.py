from django.forms import ModelForm
from .models import Transacao


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['updated_at', 'descricao', 'valor', 'observacoes', 'categoria']
