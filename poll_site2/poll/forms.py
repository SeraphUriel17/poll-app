from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['user_id','question', 'option_one', 'option_two', 'option_three','option_four']