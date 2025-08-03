from rest_framework import serializers
from account.models import Account

class AccountSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input': 'password'}, write_only=True)


    class Meta:
        model = Account
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True},
        }

    def save(self):
        password = self.validated_data.pop('password')
        password2 = self.validated_data.pop('password2')

        self.validated_data.update({
            'email': self.validated_data.get('email'),
        })

        if Account.objects.filter(email=self.validated_data.get('email')).exists():
            message = "Email already exists"
            raise serializers.ValidationError({'message': message})

        if password != password2 :
            raise serializers.ValidationError({'password': 'Password mismatch'})

        account = Account(**self.validated_data)
        account.set_password(password)
        account.save()
        return account