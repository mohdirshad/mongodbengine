from django import forms


class  Post_form(forms.Form):
	title=forms.CharField(max_length=200)
	text=forms.CharField(widget=forms.Textarea)
	tags = forms.CharField(max_length=200)
	


class Comment_form(forms.Form):
	comment=forms.CharField(widget=forms.Textarea)


