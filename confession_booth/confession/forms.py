from django import forms
from .models import AllConfessions


class WriteAConfessionForm (forms.ModelForm):
	class Meta:
		model = AllConfessions
		fields = ['confession']