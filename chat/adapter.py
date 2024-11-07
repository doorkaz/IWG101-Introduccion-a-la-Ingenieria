from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

# https://stackoverflow.com/questions/66735981/django-allauth-custom-signup-form-doesnt-save-all-of-the-fields
class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
  
        data = form.cleaned_data

        email = data.get("email")
        username = data.get("username")

        user.avatar = data.get("avatar")
        user.bio = data.get("bio")
        user.discord = data.get("discord")

        user_email(user, email)
        user_username(user, username)

        if "password1" in data:
            user.set_password(data["password1"])
        
        self.populate_username(request, user)
        if commit:
            user.save()
        return user