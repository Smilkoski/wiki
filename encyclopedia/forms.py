from django import forms


class SearchForm(forms.Form):
    text = forms.CharField(label='')


class EncyclopediaForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=100)

    class Meta:
        fields = ['title', 'text']

