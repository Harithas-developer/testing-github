from django import forms
from djangoapp.models import User


class NewUser(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('got a bot')
        return botcatcher

    class Meta():
        model = User
        exclude = ('date' ,)

