from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField
from django.utils.translation import gettext_lazy as _

# Create your models here.

GENDER = (
  ("F","أنثي"),
  ("M","ذكر"),
)

def user_direct(instance,filename):
  ext = filename.split(".")[-1]
  filename = "%s.%s" % (instance.user.id,filename)
  return "user_{0}/{1}".format(instance.user.id,filename)



class User(AbstractUser):
  full_name = models.CharField(max_length=250,null=True,blank=True)
  username = models.CharField(max_length=250,unique=True)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=100,null=True,blank=True)
  Nationality = models.CharField(max_length=250)
  country = models.CharField(max_length=250)
  gender = models.CharField(max_length=250,choices=GENDER)
  password = models.CharField(max_length=100,null=True,blank=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  def __str__(self):
    return self.username



class Profile(models.Model):
  pid = ShortUUIDField(length=7,max_length=25,alphabet="abcdefghijklmnopqrstuvwxyz123")
  slug = models.CharField(max_length=50, blank=True, null=True)
  type = models.CharField(max_length=50)
  image = models.FileField(upload_to=user_direct, default="defult.jpg" ,null=True,blank=True)
  user = models.OneToOneField(User,verbose_name=_("user"),on_delete=models.CASCADE)
  address = models.CharField(max_length=100, blank=True, null=True)
  full_name = models.CharField(max_length=250,null=True,blank=True)
  wallet = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
  verified = models.BooleanField(default=False)
  def __str__(self):
    if self.full_name:
      return f"{self.full_name}"
    else:
      return f"{self.user.username}"



def create_user_profile(sender,instance,created,**kwargs):
  if created:
    Profile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)
