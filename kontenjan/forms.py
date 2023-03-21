from django import forms
from .models import *

# class EbeForm(forms.ModelForm):
#     class Meta:
#         model = Ebe
#         fields = ('tip', 'kodu', 'sbkodu', 'kurumadı','sehir','sayi')


# class HemsireForm(forms.ModelForm):
#     class Meta:
#         model = Hemsire
#         fields = ('tip', 'kodu', 'sbkodu', 'kurumadı','sehir','sayi')


class S2021Form(forms.ModelForm):
    class Meta:
        model = S2021
        fields = ('tip', 'kodu', 'sbkodu', 'kurumadı','punvani','sehir','sayi')


