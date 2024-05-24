from django import forms
class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

from django.forms import formset_factory
ArticleFormSet = formset_factory(ArticleForm)
formset = ArticleFormSet()
for form in formset:
    print(form)