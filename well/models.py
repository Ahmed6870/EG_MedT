# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    c = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class CareAR(models.Model):
    c = models.OneToOneField('CareType', models.DO_NOTHING, primary_key=True)  # The composite primary key (c_id, a_id, r_id) found, that is not supported. The first column is selected.
    a = models.ForeignKey(Area, models.DO_NOTHING)
    r = models.ForeignKey('Resorts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'care_a_r'
        unique_together = (('c', 'a', 'r'),)


class CareType(models.Model):
    care = models.CharField(max_length=30)
    information = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'care_type'


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=255, blank=True, null=True)
    count_area = models.IntegerField(blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Disease(models.Model):
    disease = models.CharField(max_length=30)
    information = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class DiseaseAR(models.Model):
    d = models.OneToOneField(Disease, models.DO_NOTHING, primary_key=True)  # The composite primary key (d_id, a_id, r_id) found, that is not supported. The first column is selected.
    a = models.ForeignKey(Area, models.DO_NOTHING)
    r = models.ForeignKey('Resorts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'disease_a_r'
        unique_together = (('d', 'a', 'r'),)


class Hotels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=255, blank=True, null=True)
    a = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotels'


class HotelsPhone(models.Model):
    h = models.OneToOneField(Hotels, models.DO_NOTHING, primary_key=True)  # The composite primary key (h_id, phone) found, that is not supported. The first column is selected.
    phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'hotels_phone'
        unique_together = (('h', 'phone'),)


class Offers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    count_persons = models.IntegerField()
    count_rooms = models.IntegerField()
    information = models.CharField(max_length=255, blank=True, null=True)
    r = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers'


class OffersBooking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=32, blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    o = models.ForeignKey(Offers, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'offers_booking'


class RegularBooking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    room_type = models.CharField(max_length=46, blank=True, null=True)
    arrival_date = models.DateField()
    leave_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    count_persons = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    count_rooms = models.IntegerField()
    r = models.ForeignKey('Resorts', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regular_booking'


class RegularRoom(models.Model):
    regular = models.ForeignKey(RegularBooking, models.DO_NOTHING)
    room = models.OneToOneField('Room', models.DO_NOTHING, primary_key=True)  # The composite primary key (room_id, regular_id) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'regular_room'
        unique_together = (('room', 'regular'),)


class Resorts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=255, blank=True, null=True)
    a = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resorts'


class ResortsPhone(models.Model):
    r = models.OneToOneField(Resorts, models.DO_NOTHING, primary_key=True)  # The composite primary key (r_id, phone) found, that is not supported. The first column is selected.
    phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'resorts_phone'
        unique_together = (('r', 'phone'),)


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=46, blank=True, null=True)
    room_cost = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    r = models.ForeignKey(Resorts, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class RoomOffer(models.Model):
    room = models.OneToOneField(Room, models.DO_NOTHING, primary_key=True)  # The composite primary key (room_id, offer_id) found, that is not supported. The first column is selected.
    offer = models.ForeignKey(Offers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'room_offer'
        unique_together = (('room', 'offer'),)
