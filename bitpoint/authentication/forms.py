from django import forms
from bitpoint.voting.models import User

from local.constants import *

class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password",
        required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password",
        required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        id = self.cleaned_data.get('id')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class([
                'Old password don\'t match'])
        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class([
                'Passwords don\'t match'])
        return self.cleaned_data



class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Firstname",
        max_length=30,
        required=False)

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Lastname",
        max_length=30,
        required=False)

    level = forms.ChoiceField(
        choices=LEVEL,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Current level",
        required=True)
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g abc@example.com'}),
        label="Email address",
        max_length=75,
        required=False)

    state_of_origin = forms.ChoiceField(
        choices=STATES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="State of origin",
        required=True)

    town = forms.ChoiceField(
        choices=TOWNS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Town",
        required=True)

    gender = forms.ChoiceField(
        choices=GENDER,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Gender",
        required=True)

    hall_of_residence = forms.ChoiceField(
        choices=HALL_OF_RESIDENCE,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Hall of residence",
        required=True)

    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g 07033389645'}),
        label="Phone Number",
        max_length=16,
        required=False)

    facebook_id = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g abdulrasheed.ibrahim.756'}),
        label="Facebook",
        max_length=50,
        required=False,
        )
    twitter_handler = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g @abdulrasheeed1'}),
        max_length=50,
        required=False,
        )
    instagram_id = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g abdoul_rashid'}),
        max_length=50,
        required=False,
        )
    pinterest = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g somepinterestid'}),
        max_length=50,
        required=False,
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'level', 'mobile',
                  'email', 'state_of_origin', 'town', 'hall_of_residence', 
                  'facebook_id', 'twitter_handler', 'instagram_id', 'pinterest']