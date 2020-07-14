from django import forms
from django.core import validators # this is to check if there is any robot came in and scraped the page where human will never actually do that
from test_app.models import table_User

def check_for_name(value):
    for i in value:
        if i.isnumeric():
            raise forms.ValidationError("Name cannot contain numbers!")
            break

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_name])
    mail = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    txt = forms.CharField(widget=forms.Textarea)

    # hidden field that can be used to catch malicious bots on the website
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # this function is used to check the match of mail and verify_mail
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['mail']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('Email doesn\'t match!')

    # # this is to validate the form input by using clean function/method
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']

    #     # this is to check if there is any robot came in and scraped the page where human will never actually do that
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("I GOT YOU BOT!")
    #     return botcatcher

# ============================== INPUT DIRECTLY TO DB ======================================

class newUserForm(forms.ModelForm):
    class Meta():
        model = table_User
        fields = '__all__'

# ================================= FORMS FOR USERPROFILE =====================================

from test_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')