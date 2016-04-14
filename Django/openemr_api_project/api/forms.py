from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, HTML
from crispy_forms.bootstrap import InlineRadios
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm


class UserCreateForm(UserCreationForm):

    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'username'}),
        help_text="Must be at least 8 characters."
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        required=True,
        widget = forms.TextInput(attrs={'placeholder': 'John'}),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Smith'}),
    )
    email = forms.EmailField(
        label="Email",
        required=False,
        widget = forms.TextInput(attrs={'placeholder': 'johnsmith@example.com'}),
    )
    is_staff = forms.ChoiceField(
        widget=forms.Select(),
        label="Admin user",
        required=True,
        help_text="Will this user be an administrator of this site/application?",
        choices=((True, "Yes"),(False, "No"))
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "is_staff")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_staff = False

        if self.cleaned_data["is_staff"] == "True":
            user.is_staff = True

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        # Crispy Forms Helper
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-9'
        self.helper.form_id = "user-create-form"
        self.helper.form_method = "post"
        self.helper.form_action = "./"

        self.helper.layout = Layout(
            'username',
            'first_name',
            'last_name',
            'email',
            InlineRadios('is_staff'),
            'password1',
            'password2',
        )


class UserUpdateForm(forms.Form):

    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'username'}),
        help_text="Must be at least 8 characters."
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'John'}),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Smith'}),
    )
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'johnsmith@example.com'}),
    )
    is_staff = forms.ChoiceField(
        widget=forms.Select(),
        label="Admin user",
        required=True,
        help_text="Will this user be an administrator of this site/application?",
        choices=((True, "Yes"), (False, "No"))
    )
    is_active = forms.ChoiceField(
        widget=forms.Select(),
        label="Admin user",
        required=True,
        help_text="Deactivate this account?",
        choices=((True, "Yes"), (False, "No"))
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "is_staff", "is_active")

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        # Crispy Forms Helper
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-9'
        self.helper.form_id = "login-form"
        self.helper.form_method = "post"
        self.helper.form_action = "./"

        self.helper.layout = Layout(
            'username',
            'first_name',
            'last_name',
            'email',
            InlineRadios('is_staff'),
            InlineRadios('is_active'),
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
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-9'
        self.helper.form_id = "password-change-form"
        self.helper.form_method = "post"
        self.helper.form_action = "./"

        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
        )