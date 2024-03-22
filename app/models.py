from django.db import models


class Group(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'


class GroupRights(models.Model):
    groupid = models.CharField(max_length=45, blank=True, null=True)
    rightsid = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_rights'


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=45, blank=True, null=True)
    icon = models.CharField(max_length=45, blank=True, null=True)
    vis = models.CharField(max_length=45, blank=True, null=True)
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
    username = models.CharField(unique=True, max_length=45, blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    groupname = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'