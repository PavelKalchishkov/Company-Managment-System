from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class CustomUserEditProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
