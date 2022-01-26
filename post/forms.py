from django import forms
from django.core import validators


class UserForm(forms.Form):
    user_email = forms.EmailField()
    user_vmail = forms.EmailField()

    def clean(self):
        all_data = super().clean()
        print(all_data)
        user_email = all_data["user_email"]
        user_vmail = all_data["user_vmail"]

        if user_email != user_vmail:
            raise forms.ValidationError("Email does not match")
