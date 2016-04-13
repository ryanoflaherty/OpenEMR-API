from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        # Crispy Forms Helper
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'
        self.helper.form_id = "login-form"
        self.helper.form_method = "post"
        self.helper.form_action = "./"

        self.helper.layout = Layout(
            'username',
            'password',
        )


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        # Crispy Forms Helper
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'
        self.helper.form_id = "login-form"
        self.helper.form_method = "post"
        self.helper.form_action = "./"

        self.helper.layout = Layout(
            'username',
            'password',
        )


class CrispyPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(CrispyPasswordChangeForm, self).__init__(*args, **kwargs)

        # Crispy Forms Helper
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'
        self.helper.form_id = "password-change-form"
        self.helper.form_method = "post"
        self.helper.form_action = "./"

        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
        )