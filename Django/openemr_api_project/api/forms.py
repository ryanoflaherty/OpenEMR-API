from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class LoginForm(forms.Form):

    username = forms.CharField(
        label="Username",
        required=True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label= "Password",
        required=True,
    )

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

    class Meta:
        model = User
