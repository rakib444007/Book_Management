from django import forms 
from django.contrib.auth.models import User
from User_profile.models import UserProfile
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from User_profile.constants import GENDER_TYPE
class UserResgistrationsForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2','gender','birth_date']


    def save(self,commit = True):
        user = super().save(commit=True) 
        if commit == True:
            user.save()
            gender = self.cleaned_data.get('gender')
            birth_date = self.cleaned_data.get('birth_date')

            UserProfile.objects.create(
                user = user,
                gender = gender,
                birth_date =birth_date

            )
        return user

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({

                'class':(
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'                   
                )

            })






