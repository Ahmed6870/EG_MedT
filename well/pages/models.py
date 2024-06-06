from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.text import slugify
import datetime
from django_countries.fields import CountryField
from userauths.models import User,Profile

# def PagesUser(sender,**kwargs):
#     if kwargs['created']:
#         profile.objects.create(user=kwargs['instance'])

# def save_user (sender,instance,**kwargs):
#     instance.profile.save()

# post_save.connect(PagesUser,sender=User)
# post_save.connect(save_user,sender=User)

TYPE_OF_PERSON=(
    ('M' , "Male"),
    ('F' , "Female"),
)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    nationality = models.CharField(db_column='Nationality', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


# class profile(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     address = models.CharField(max_length=100, blank=True, null=True)
#     slug =models.SlugField(_("slug"),blank=True, null=True )
#     type = models.CharField(_("النوع:"),choices=TYPE_OF_PERSON,max_length=50)
#     image = models.FileField(_("الصورة الشخصية :"), upload_to='profile',blank=True, null=True)
#     user = models.OneToOneField('pages.User', models.DO_NOTHING, blank=True, null=True)
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.user.username)
#         super(profile,self).save(*args, **kwargs)
#     def __str__(self):
#         return '%s' %(self.user.username)
#     class Meta:
#         verbose_name = _("profile")
#         verbose_name_plural = _("profiles")
#         managed = False
#         db_table = 'profile'



class CareType(models.Model):
    Care_Type =[
        ("تقوية الأعصاب","تقوية الأعصاب"),
        ("الإسترخاء","الإسترخاء"),
        ("الدفن في الرمال","الدفن في الرمال"),
        ("المياة المعدنية","المياة المعدنية"),
        ("الأبار و العيون ","الأبار و العيون "),
    ]
    Care_id = models.IntegerField(primary_key=True)
    Care = models.CharField(_("الرعاية"),choices=Care_Type,max_length=50)

    def __str__(self):
        return '%s' %(self.Care)


    class Meta:
        managed = False
        verbose_name = _("CareType")
        verbose_name_plural = _("CareTypes")
        db_table = 'Care_type'








class CareDR(models.Model):
    care = models.OneToOneField('CareType', models.DO_NOTHING, primary_key=True)  # The composite primary key (care_id, des_id, resort_id) found, that is not supported. The first column is selected.
    resort = models.ForeignKey('Resorts', models.DO_NOTHING)
    des =models.ForeignKey("destinations", models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'care_d_r'
        verbose_name = _("CareDR")
        verbose_name_plural = _("CareDRS")
        unique_together = (('care', 'resort'),)






class Resorts(models.Model):
    resort_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    photo = models.FileField(upload_to= "Resorts/name",blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    des = models.ForeignKey('Destinations',models.DO_NOTHING)
    def __str__(self):
        return '%s' %(self.name)

    class Meta:
        managed = True
        verbose_name = _("Resort")
        verbose_name_plural = _("Resorts")
        db_table = 'resorts'








class ResortsPhone(models.Model):
    resort = models.OneToOneField('Resorts', models.DO_NOTHING, primary_key=True)  # The composite primary key (resort_id, phone) found, that is not supported. The first column is selected.
    phone = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'resorts_phone'
        verbose_name = _("ResortsPhone")
        verbose_name_plural = _("ResortsPhone")
        unique_together = (('resort', 'phone'),)






class Rooms(models.Model):
    Room_Type = [
        ('غرفة لفرد واحد', 'غرفة لفرد واحد'),
        ('غرفة لفردين', 'غرفة لفردين'),
        ('غرفة لفردين أو أكثر', 'غرفة لفردين أو أكثر'),
        ('غرفة لعائلة', 'غرفة لعائلة'),
    ]
    room_id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=100,choices=Room_Type)
    room_cost = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.FileField(blank=True, null=True)
    limit = models.IntegerField()
    resort = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    def __str__(self):
        return '%s' %(self.room_id  )

    class Meta:
        managed = False
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        db_table = 'rooms'





class RoomOffers(models.Model):
    room = models.OneToOneField('Rooms', models.DO_NOTHING, primary_key=True)  # The composite primary key (room_id, offer_id) found, that is not supported. The first column is selected.
    offer = models.ForeignKey('Offers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'room_offers'
        verbose_name = _("RoomOffer")
        verbose_name_plural = _("RoomOffers")
        unique_together = (('room', 'offer'),)





class RegularRoom(models.Model):
    room = models.OneToOneField('Rooms', models.DO_NOTHING, primary_key=True)  # The composite primary key (room_id, regular_id) found, that is not supported. The first column is selected.
    regular = models.ForeignKey('RegularBooking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'regular_room'
        verbose_name = _("RegularRoom")
        verbose_name_plural = _("RegularRooms")
        unique_together = (('room', 'regular'),)





class RegularBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey('Rooms',on_delete=models.CASCADE)
    regular_id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=50)
    arrival_date = models.DateTimeField( blank=True, null=True)
    leave_date = models.DateTimeField( blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    count_persons = models.IntegerField(blank=True, null=True)
    count_rooms = models.IntegerField( blank=True, null=True)
    book_date = models.DateField(blank=True, null=True)
    book_state = models.CharField(max_length=150, blank=True, null=True)
    resort = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.arrival_date} to {self.leave_date}'
    class Meta:
        managed = False
        verbose_name = _("RegularBooking")
        verbose_name_plural = _("RegularBookings")
        db_table = 'regular_booking'






class Offers(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=0,blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    count_person = models.CharField(max_length=50,blank=True, null=True)
    count_room = models.IntegerField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    resort = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return '%s' %(self.name)

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")
        managed = False
        db_table = 'offers'






class Destinations(models.Model):
    des_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    information = models.TextField(blank=True, null=True)
    photo = models.FileField(blank=True, null=True, upload_to="Destinations/")
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '%s' %(self.name)

    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")
        managed = True
        db_table = 'destinations'







class Diseases(models.Model):
    disease_type ={
        ('الروماتيزم',"الروماتيزم"),
        ('عرق النسا',"عرق النسا"),
        ('التهابات الجلدية',"التهابات الجلدية"),
        ('الإرتشاح المفصلي',"الإرتشاح المفصلي"),
        ('التورم',"التورم"),
        ('الروماتويد',"الروماتويد"),
        ('الصدفية',"الصدفية"),
        ('الضعف و الوهن',"الضعف و الوهن"),
        ('ألم الظهر',"ألم الظهر"),
        ('ألم المفاصل',"ألم المفاصل"),
    }

    disease_id = models.IntegerField(primary_key=True)
    disease = models.CharField(_("المرض"),choices=disease_type,max_length=50)

    class Meta:
        verbose_name = _("Disease")
        verbose_name_plural = _("Diseases")
        managed = True
        db_table = 'diseases'






class DiseaseDR(models.Model):
    disease = models.OneToOneField('Diseases', models.DO_NOTHING, primary_key=True)  # The composite primary key (disease_id, resort_id) found, that is not supported. The first column is selected.
    resort = models.ForeignKey('Resorts', models.DO_NOTHING)
    des = models.ForeignKey('Destinations', models.DO_NOTHING)

    class Meta:
        managed = False
        verbose_name = _("DiseaseDR")
        verbose_name_plural = _("DiseaseDRS")
        db_table = 'disease_d_r'
        unique_together = (('disease', 'resort'),)









class ComplainsComments(models.Model):
    complains_comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('UserauthsUser', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    offer = models.ForeignKey('Offers', models.DO_NOTHING, blank=True, null=True)
    resort = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _("ComplainsComment")
        verbose_name_plural = _("ComplainsComments")
        managed = False
        db_table = 'complains_comments'








class Hotels(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.ForeignKey('Destinations', models.DO_NOTHING)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    information = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Hotel")
        verbose_name_plural = _("Hotels")
        managed = False
        db_table = 'Hotels'







class OffersBooking(models.Model):
    offer_book_id = models.IntegerField(primary_key=True)
    arrival_date = models.DateField()
    book_state = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey('UserauthsUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _("OffersBooking")
        verbose_name_plural = _("OffersBookings")
        managed = False
        db_table = 'offers_booking'








class OffersBookingOffers(models.Model):
    book = models.ForeignKey('OffersBooking', models.DO_NOTHING)
    offer = models.OneToOneField('Offers', models.DO_NOTHING, primary_key=True)  # The composite primary key (offer_id, book_id) found, that is not supported. The first column is selected.

    class Meta:
        verbose_name = _("OffersBookingOffers")
        verbose_name_plural = _("OffersBookingOffers")
        managed = False
        db_table = 'offers_booking_offers'
        unique_together = (('offer', 'book'),)




# class UserauthsProfile(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     pid = models.CharField(max_length=25)
#     slug = models.CharField(max_length=50, blank=True, null=True)
#     type = models.CharField(max_length=50)
#     image = models.CharField(max_length=100, blank=True, null=True)
#     address = models.CharField(max_length=100, blank=True, null=True)
#     full_name = models.CharField(max_length=500, blank=True, null=True)
#     wallet = models.DecimalField(max_digits=12, decimal_places=2)
#     verified = models.IntegerField()
#     user_id = models.BigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'userauths_profile'


class UserauthsUser(models.Model):
    id = models.IntegerField(primary_key=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    full_name = models.CharField(max_length=500, blank=True, null=True)
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=254)
    phone = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=500)
    password = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(db_column='Nationality', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'userauths_user_pages'


# class UserauthsUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user_id = models.BigIntegerField()
#     group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'userauths_user_groups'


# class UserauthsUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#     user_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'userauths_user_user_permissions'
