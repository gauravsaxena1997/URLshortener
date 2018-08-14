from django import forms
from django.core.validators import URLValidator

from .validators import validate_url

class SubmitUrlForm(forms.Form):
	url = forms.CharField(	label='', 
							widget = forms.TextInput (
								attrs = {'placeholder':'Long URL',
										 'class':'form-control  form-control-lg' }),
							validators=[validate_url])