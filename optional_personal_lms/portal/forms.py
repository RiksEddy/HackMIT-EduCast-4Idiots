from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class student_signup_form(UserCreationForm):
    department=forms.CharField()
    class Meta:
        model = User
        fields = ['username','department','password1','password2']

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Password Mismatch")
        return password1

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1'],
        )
        new_profile = Profile(
            identity=user,
            department=self.cleaned_data['last_name'],
        )
        new_profile.save()
        return user


class teacher_signup_form(UserCreationForm):
    department=forms.CharField()
    class Meta:
        model = User
        fields = ['username','department','password1','password2']

class UserLoginForm(forms.Form):
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=30)
	password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)

class DocumentForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),required=True,max_length=30)
	document = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter link to the doc'}),required=True,max_length=80)
	message = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter message'}),required=True,max_length=30)

	class Meta:
		model = Document
		fields = ('title', 'document', 'message' )
