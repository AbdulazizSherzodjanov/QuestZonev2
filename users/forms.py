from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None


from .models import ProfileModel

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

    def __init__(self,*args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email']:
            self.fields[fieldname].help_text = None



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']

























