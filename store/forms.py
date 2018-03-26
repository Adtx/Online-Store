from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Costumer
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

    class Meta:
        model = Costumer

class CostumerRegistrationForm(UserCreationForm):

    error_messages = {
        'password_mismatch': "As palavras-passe não correspondem.",
    }
    password1 = forms.CharField(label="Palavra-Passe", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirme a Palavra-Passe", widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(CostumerRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Costumer
        fields = ['username','email','password1','password2']
        labels = {
            'username': 'Nome',
            'email': 'Endereço de Email'
        }

# class CostumerUpdateForm(forms.ModelForm):


#     def __init__(self, *args, **kwargs):
#         super(CostumerUpdateForm, self).__init__(*args, **kwargs)
#         self.fields['username'].help_text = None

#         self.fields['username']= forms.CharField(
#            label =('User Name'), max_length = constants.MAX_LEN_NAME, 
#            initial = profile_default.username)


#     class Meta:
#         model = Costumer
#         fields = ['username', 'email', 'telephone','street', 'city', 'district', 'zipcode', 'country']
#         labels = {
#             'username': 'Nome',
#             'email': 'Endereço de Email',
#             'telephone': 'Telefone',
#             'street': 'Rua',
#             'city': 'Cidade',
#             'district': 'Distrito',
#             'zipcode': 'Código Postal',
#             'country': 'País'
#         }



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
            