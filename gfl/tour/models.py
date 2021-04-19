from django.db import models
from django.core.validators import RegexValidator
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, is_admin=False):
        if not phone:
            raise ValueError('users must have a phone number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(
            phone=phone
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,


        )
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
            is_admin=True,


        )
        return user

class User(AbstractBaseUser):
    phone_regex = RegexValidator( regex   =r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    phone       = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    name        = models.CharField(max_length = 20, blank = True, null = True)
    standard    = models.CharField(max_length = 3, blank = True, null = True)
    score       = models.IntegerField(default = 16)
    first_login = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


        return str(self.phone) + ' is sent ' + str(self.otp)



roles = (
    ("BATSMAN", "BATSMAN"),
    ("BOWLER", "BOWLER"),
    ("KEEPER", "KEEPER"),
)
class Team(models.Model): #MI #RCB #KKR #CSK #DC
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Match(models.Model): #MI vs RCB
    team_a = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team_a')
    team_b = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team_b')
    
    def __str__(self):
            return str(self.team_a.name)+ " vs "+str(self.team_b.name)
class TeamPlayer(models.Model):
    player = models.ForeignKey(User,on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team,on_delete=models.CASCADE)
    role = models.CharField(max_length=100,choices=roles)

    def __str__(self):
        return self.player.username

class Tournament(models.Model): #IPL #IPL22
    name = models.CharField(max_length=100)
    match_id = models.ForeignKey(Match,on_delete=models.CASCADE) 
    umpire = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tour_umpire')
    scorer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tour_scorer')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
