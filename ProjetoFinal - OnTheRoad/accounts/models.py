from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, nome, username, telefone, password=None):
        if not email:
            raise ValueError('Usuários devem ter um email')
        if not nome:
            raise ValueError('Usuários devem ter um nome')
        if not username:
            raise ValueError('Usuários devem ter um nome de usuário')
        if not telefone:
            raise ValueError('Usuários devem ter um telefone')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            username=username,
            telefone=telefone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, username, telefone, password):
        user = self.create_user(
            email,
            password=password,
            nome=nome,
            username=username,
            telefone=telefone
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True,)
    nome = models.CharField(verbose_name='nome', max_length=128)
    username = models.CharField(verbose_name='nome de usuário', max_length=128)
    telefone = models.CharField(verbose_name='telefone', max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'username', 'telefone']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
