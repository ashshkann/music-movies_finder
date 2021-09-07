from django import forms

class form_music(forms.Form):
    finder_music_form = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label=False
    )

class form_movies(forms.Form):
    finder_movies_form = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label=False
    )