from django import forms
from test1.models import File_Upload


    
class File_Upload_Form(forms.ModelForm):
    class Meta:
        model = File_Upload
        fields = ('description','document')

class File_upload(forms.Form):
    document=forms.FileField()