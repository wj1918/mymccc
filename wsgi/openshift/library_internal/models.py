# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class CbDb(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title 
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=160, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=240, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, primary_key=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CB-DB'

class EbDb(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title 
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=8, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, primary_key=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'EB-DB'

