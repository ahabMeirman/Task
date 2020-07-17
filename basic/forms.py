from django import forms
from basic.models import *

class CompanyForm(forms.ModelForm):
	
	class Meta:
		model=Company
		fields=["rank", "employer", "employees", "salary"]

		widgets = {
			"rank": forms.TextInput(attrs={'class':'form-control'}),
			"employer": forms.TextInput(attrs={'class':'form-control'}),
			"employees": forms.TextInput(attrs={'class':'form-control'}),
			"salary": forms.TextInput(attrs={'class':'form-control'}),
		}