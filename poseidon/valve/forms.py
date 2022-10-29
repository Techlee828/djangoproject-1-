from django.forms import ModelForm

from .models import Valve


class ValveForm(ModelForm):
    class Meta:
        model = Valve
        fields = '__all__'




