from django import forms
from test1.models import File_Upload
from registration.models import User_Profile
class File_Upload_Form(forms.ModelForm):
    class Meta:
        model=File_Upload
        fields='__all__'

class User_Profile_Form(forms.ModelForm):
    class Meta:
        model=User_Profile
        fields='__all__'
class User_Profile_Login_Form(forms.ModelForm):
    class Meta:
        model=User_Profile
        fields=('username','email','password')