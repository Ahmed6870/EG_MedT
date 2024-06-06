# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AvailableRoom(models.Model):
    resort = models.OneToOneField('Resorts', models.DO_NOTHING, primary_key=True)  # The composite primary key (resort_id, room_type) found, that is not supported. The first column is selected.
    room_type = models.CharField(max_length=25)
    count_rooms = models.IntegerField(blank=True, null=True)
    availed_rooms = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'available_room'
        unique_together = (('resort', 'room_type'),)


class CareDR(models.Model):
    resort = models.OneToOneField('Resorts', models.DO_NOTHING, primary_key=True)  # The composite primary key (resort_id, care_id, des_id) found, that is not supported. The first column is selected.
    care = models.ForeignKey('CareTypes', models.DO_NOTHING)
    des = models.ForeignKey('Destinationss', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'care_d_r'
        unique_together = (('resort', 'care', 'des'),)


class CareTypes(models.Model):
    care_id = models.IntegerField(primary_key=True)
    care = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'care_types'


class ComplainsComments(models.Model):
    complains_comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    offer = models.ForeignKey('Offers', models.DO_NOTHING, blank=True, null=True)
    resort = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complains_comments'


class Destinationss(models.Model):
    des_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    information = models.TextField(blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=45, blank=True, null=True)
    clas = models.CharField(max_length=45, blank=True, null=True)
    photo_larg = models.CharField(db_column='photo_Larg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo_small = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destinationss'


class DiseaseDR(models.Model):
    resort = models.OneToOneField('Resorts', models.DO_NOTHING, primary_key=True)  # The composite primary key (resort_id, disease_id, des_id) found, that is not supported. The first column is selected.
    disease = models.ForeignKey('Diseases', models.DO_NOTHING)
    des = models.ForeignKey(Destinationss, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'disease_d_r'
        unique_together = (('resort', 'disease', 'des'),)


class Diseases(models.Model):
    disease_id = models.IntegerField(primary_key=True)
    disease = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'diseases'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Hotels(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.ForeignKey(Destinationss, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    information = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotels'


class Offers(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    period = models.IntegerField()
    count_person = models.CharField(max_length=50)
    count_room = models.IntegerField()
    information = models.TextField()
    resort = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    inf = models.CharField(max_length=100, blank=True, null=True)
    inf1 = models.CharField(max_length=100, blank=True, null=True)
    inf2 = models.CharField(max_length=100, blank=True, null=True)
    inf3 = models.CharField(max_length=100, blank=True, null=True)
    inf4 = models.CharField(max_length=100, blank=True, null=True)
    inf5 = models.CharField(max_length=100, blank=True, null=True)
    inf6 = models.CharField(max_length=100, blank=True, null=True)
    inf7 = models.CharField(max_length=100, blank=True, null=True)
    inf8 = models.CharField(max_length=100, blank=True, null=True)
    inf9 = models.CharField(max_length=100, blank=True, null=True)
    inf10 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers'


class OffersBooking(models.Model):
    offer_book_id = models.IntegerField(primary_key=True)
    arrival_date = models.DateField()
    book_state = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers_booking'


class OffersBookingOffers(models.Model):
    book = models.ForeignKey(OffersBooking, models.DO_NOTHING)
    offer = models.OneToOneField(Offers, models.DO_NOTHING, primary_key=True)  # The composite primary key (offer_id, book_id) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'offers_booking_offers'
        unique_together = (('offer', 'book'),)


class PagesProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contry = models.CharField(max_length=32, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_profile'


class Profile(models.Model):
    slug = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50)
    image = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'


class RegularBooking(models.Model):
    regular_id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=50)
    arrival_date = models.DateTimeField()
    leave_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    count_persons = models.IntegerField(blank=True, null=True)
    count_rooms = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    book_date = models.DateField(blank=True, null=True)
    book_state = models.CharField(max_length=150, blank=True, null=True)
    resort = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='Room_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regular_booking'


class RegularRoom(models.Model):
    regular = models.ForeignKey(RegularBooking, models.DO_NOTHING)
    room = models.OneToOneField('Rooms', models.DO_NOTHING, primary_key=True)  # The composite primary key (room_id, regular_id) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'regular_room'
        unique_together = (('room', 'regular'),)


class Resorts(models.Model):
    resort_id = models.IntegerField(primary_key=True)
    des = models.ForeignKey(Destinationss, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    photo1 = models.CharField(max_length=100, blank=True, null=True)
    photo2 = models.CharField(max_length=100, blank=True, null=True)
    photo3 = models.CharField(max_length=100, blank=True, null=True)
    photo4 = models.CharField(max_length=100, blank=True, null=True)
    photo5 = models.CharField(max_length=100, blank=True, null=True)
    photo6 = models.CharField(max_length=100, blank=True, null=True)
    photo_s0 = models.CharField(db_column='photo_S0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo_s1 = models.CharField(db_column='photo_S1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo_s2 = models.CharField(db_column='photo_S2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo_s3 = models.CharField(db_column='photo_S3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo_s4 = models.CharField(db_column='photo_S4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo_s5 = models.CharField(db_column='photo_S5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo_s6 = models.CharField(db_column='photo_S6', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resorts'


class ResortsPhone(models.Model):
    resort = models.OneToOneField(Resorts, models.DO_NOTHING, primary_key=True)  # The composite primary key (resort_id, phone) found, that is not supported. The first column is selected.
    phone = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'resorts_phone'
        unique_together = (('resort', 'phone'),)


class RoomOffers(models.Model):
    room = models.OneToOneField('Rooms', models.DO_NOTHING, primary_key=True)  # The composite primary key (room_id, offer_id) found, that is not supported. The first column is selected.
    offer = models.ForeignKey(Offers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'room_offers'
        unique_together = (('room', 'offer'),)


class Rooms(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=100)
    room_cost = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.CharField(max_length=100, blank=True, null=True)
    limit = models.IntegerField()
    resort = models.ForeignKey(Resorts, models.DO_NOTHING, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    inf1 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)
