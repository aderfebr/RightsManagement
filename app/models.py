# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Group(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'


class GroupRights(models.Model):
    groupid = models.IntegerField(blank=True, null=True)
    rightsid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_rights'


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=45, blank=True, null=True)
    icon = models.CharField(max_length=45, blank=True, null=True)
    index = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Rights(models.Model):
    rightsid = models.IntegerField(primary_key=True)
    rightsname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rights'


class Token(models.Model):
    userid = models.CharField(max_length=45, blank=True, null=True)
    value = models.CharField(max_length=45, blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token'


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroup(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'