from django import forms
from myapp.models import Student,Movie,Login,Additem

class StudentForm(forms.Form):

    name=forms.CharField()
    marks=forms.IntegerField()

class StudentForm1(forms.ModelForm):

    class Meta:

        model=Student
        fields='__all__'

class MovieForm(forms.ModelForm):
    class Meta:

        model=Movie
        fields='__all__'

class LoginForm(forms.Form):

    name=forms.CharField()
    datetime=forms.CharField()
class Itemaddform(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()
    