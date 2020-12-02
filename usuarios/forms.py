from django.contrib.auth.forms import UserCreationForm

class CadastroCustom(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CadastroCustom, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email","first_name","last_name")

class CadastroCustomEdit(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CadastroCustomEdit, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email","first_name","last_name")
        exclude = ['username']