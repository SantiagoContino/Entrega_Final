from django import forms
 

class UrbanFormulario(forms.Form):
    marca= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    año= forms.IntegerField()

class CrossoverFormulario(forms.Form):
    marca= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    año= forms.IntegerField()

class DeportivoFormulario(forms.Form):
    marca= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    año= forms.IntegerField()
    