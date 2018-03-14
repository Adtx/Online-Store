from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignInForm(AuthenticationForm):
    
    username = forms.CharField(label='Nome', max_length=254)
    password = forms.CharField(label='Palavra-Passe', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': "Nome ou Palavra-Passe incorretos",
        'inactive': "Esta conta nao existe",
    }

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)

class UserRegistrationForm(UserCreationForm):

    error_messages = {
        'password_mismatch': "As palavras-passe não correspondem.",
    }
    password1 = forms.CharField(label="Palavra-Passe", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirme a Palavra-Passe", widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {
            'username': 'Nome',
            'email': 'Endereço de Email'
        }
        # error_messages = {
        #     'username': {
        #         'unique': 'O nome de utilizador que escolheu nao esta disponivel'
        #     },
        #     'password1': {
        #         'min_length': 'A Palavra-Passe deve ter pelo menos 8 caracteres alfanumericos'
        #     },
        #     'password2': {
        #         'password_mismatch': "As palavras-passe não correspondem."
        #     }
        # }
        # help_texts = {
        #     'username': None,
        #     'email': None,
        #     'password2': None
        # }
            