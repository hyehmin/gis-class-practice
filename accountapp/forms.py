from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # super : 부모 클래스 접근할 때 사용함.
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True