from django import forms


class SubmitAnswerForm(forms.Form):
    answer_option = forms.CharField()
