from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"YOUR FULL NAME"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"YOUR EMAIL"}))
	message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"YOUR MESSAGE"}))

	def clean_email(self):
		email = self.cleaned_data.get("email")

		if not "gmail.com" in email:
			raise forms.ValidationError("ONLY GMAIL ID ACCEPTED")

		return email

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"ENTER USERNAME"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"ENTER PASSWORD"}))

class RegisterForm(forms.Form):
	firstname = forms.CharField(max_length=25,label='FIRSTNAME',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"YOUR FIRSTNAME"}))
	lastname = forms.CharField(max_length=25,label='LASTNAME',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"YOUR LASTNAME"}))
	username = forms.CharField(max_length=25,label='USERNAME',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"YOUR USERNAME"}))
	email = forms.EmailField(max_length=25,label='EMAIL-ID',widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"YOUR EMAIL"}))
	password = forms.CharField(max_length=25,label='PASSWORD',widget=forms.PasswordInput(render_value=True, attrs={"class":"form-control","placeholder":"YOUR PASSWORD"}))
	confirm_password = forms.CharField(label='CONFIRM PASSWORD',widget=forms.PasswordInput(render_value=True, attrs={"class":"form-control","placeholder":"CONFIRM YOUR PASSWORD"}))

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("USERNAME IS TAKEN")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("EMAIL IS TAKEN")
		return email

	def clean_password(self):
		password = self.cleaned_data.get("password")
		confirm_password = self.cleaned_data.get("password")

		if confirm_password != password:
			raise forms.ValidationError("PASSWORDS MUST MATCH!!")
		return password
