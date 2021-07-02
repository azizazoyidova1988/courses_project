from django import forms
from store.models import Commenter, Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe()
        fields = '__all__'
