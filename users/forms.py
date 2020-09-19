from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SocialUser

class SocialUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = SocialUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class SocialUserChangeForm(UserChangeForm):
    class Meta:
        model = SocialUser
        fields = ('first_name', 'last_name', 'email', 'password')
