# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class LibCbDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=160, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=240, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CB-DB'

class LibCcdDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CCD-DB'

class LibCcdDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CCD-DB1'

class LibCdvdDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CDVD-DB'

class LibCtDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CT-DB'

class LibCtDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CT-DB1'

class LibCvDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CV-DB'

class LibCvDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_CV-DB1'

class LibChoirDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=240, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=160, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    resourcenumber = models.CharField(db_column='ResourceNumber', max_length=10, blank=True) # Field name made lowercase.
    copynumber = models.IntegerField(db_column='CopyNumber', blank=True, null=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_Choir-DB'

class LibChoirDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=240, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=160, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    resourcenumber = models.CharField(db_column='ResourceNumber', max_length=10, blank=True) # Field name made lowercase.
    copynumber = models.IntegerField(db_column='CopyNumber', blank=True, null=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_Choir-DB1'

class LibClassnumberlookuptable(models.Model):
    deweyclassnumber = models.CharField(db_column='DeweyClassNumber', max_length=100, blank=True) # Field name made lowercase.
    mcccpre96classnumber = models.CharField(db_column='MCCCPre96ClassNumber', max_length=100, blank=True) # Field name made lowercase.
    afccatalognumber = models.CharField(db_column='AFCcatalogNumber', max_length=100, blank=True) # Field name made lowercase.
    deweyclassnumberdescription = models.CharField(db_column='DeweyClassNumberDescription', max_length=400, blank=True) # Field name made lowercase.
    deweyclassnumberchinesedescription = models.CharField(db_column='DeweyClassNumberChineseDescription', max_length=100, blank=True) # Field name made lowercase.
    keeperindex1 = models.IntegerField(db_column='KeeperIndex1', blank=True, null=True) # Field name made lowercase.
    keeperindex2 = models.IntegerField(db_column='KeeperIndex2', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_ClassNumberLookUpTable'

class LibDummyrecordtable(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=8, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_DummyRecordTable'

class LibDummyrecordtable1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=8, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_DummyRecordTable1'

class LibEbDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=8, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_EB-DB'

class LibEbDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=8, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_EB-DB1'

class LibEbDb2(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=8, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_EB-DB2'

class LibEcdDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_ECD-DB'

class LibEcdDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_ECD-DB1'

class LibEdvdDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_EDVD-DB'

class LibEtDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_ET-DB'

class LibEtDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_ET-DB1'

class LibEvDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_EV-DB'

class LibEvDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_EV-DB1'

class LibGeneralPurposeLabel(models.Model):
    upperleft = models.CharField(db_column='UpperLeft', max_length=20, blank=True) # Field name made lowercase.
    firstline = models.CharField(db_column='FirstLine', max_length=400, blank=True) # Field name made lowercase.
    secondline = models.CharField(db_column='SecondLine', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_General Purpose Label'

class LibGeneralPurposeLabel1(models.Model):
    upperleft = models.CharField(db_column='UpperLeft', max_length=20, blank=True) # Field name made lowercase.
    firstline = models.CharField(db_column='FirstLine', max_length=400, blank=True) # Field name made lowercase.
    secondline = models.CharField(db_column='SecondLine', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_General Purpose Label1'

class LibKcbDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KCB-DB'

class LibKcbDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KCB-DB1'

class LibKcdvdDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KCDVD-DB'

class LibKctDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True) # Field name made lowercase.
    runningtime = models.CharField(db_column='RunningTime', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=200, blank=True) # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True) # Field name made lowercase.
    mcccpurchasedate = models.CharField(db_column='MCCCPurchaseDate', max_length=100, blank=True) # Field name made lowercase.
    purchaseprice = models.CharField(db_column='PurchasePrice', max_length=100, blank=True) # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=20, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KCT-DB'

class LibKctDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True) # Field name made lowercase.
    runningtime = models.CharField(db_column='RunningTime', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=200, blank=True) # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True) # Field name made lowercase.
    mcccpurchasedate = models.CharField(db_column='MCCCPurchaseDate', max_length=100, blank=True) # Field name made lowercase.
    purchaseprice = models.CharField(db_column='PurchasePrice', max_length=100, blank=True) # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=20, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KCT-DB1'

class LibKcvDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True) # Field name made lowercase.
    runningtime = models.CharField(db_column='RunningTime', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=200, blank=True) # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True) # Field name made lowercase.
    mcccpurchasedate = models.CharField(db_column='MCCCPurchaseDate', max_length=100, blank=True) # Field name made lowercase.
    purchaseprice = models.CharField(db_column='PurchasePrice', max_length=100, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=20, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KCV-DB'

class LibKcvDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True) # Field name made lowercase.
    runningtime = models.CharField(db_column='RunningTime', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=200, blank=True) # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True) # Field name made lowercase.
    mcccpurchasedate = models.CharField(db_column='MCCCPurchaseDate', max_length=100, blank=True) # Field name made lowercase.
    purchaseprice = models.CharField(db_column='PurchasePrice', max_length=100, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=20, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KCV-DB1'

class LibKebDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KEB-DB'

class LibKebDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KEB-DB1'

class LibKecdDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KECD-DB'

class LibKecdDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KECD-DB1'

class LibKedvdDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KEDVD-DB'

class LibKevDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True) # Field name made lowercase.
    runningtime = models.CharField(db_column='RunningTime', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=200, blank=True) # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True) # Field name made lowercase.
    mcccpurchasedate = models.CharField(db_column='MCCCPurchaseDate', max_length=100, blank=True) # Field name made lowercase.
    purchaseprice = models.CharField(db_column='PurchasePrice', max_length=100, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KEV-DB'

class LibKevDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True) # Field name made lowercase.
    runningtime = models.CharField(db_column='RunningTime', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=200, blank=True) # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True) # Field name made lowercase.
    mcccpurchasedate = models.CharField(db_column='MCCCPurchaseDate', max_length=100, blank=True) # Field name made lowercase.
    purchaseprice = models.CharField(db_column='PurchasePrice', max_length=100, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KEV-DB1'

class LibKeeperindextable(models.Model):
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    chinesename = models.CharField(db_column='ChineseName', max_length=100, blank=True) # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=100, blank=True) # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KeeperIndexTable'

class LibKeeperindextable1(models.Model):
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    chinesename = models.CharField(db_column='ChineseName', max_length=100, blank=True) # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=100, blank=True) # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=30, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KeeperIndexTable1'

class LibKeeperpreferencetable(models.Model):
    deweycallnumber = models.CharField(db_column='DeweyCallNumber', max_length=100, blank=True) # Field name made lowercase.
    keeperindex1 = models.IntegerField(db_column='KeeperIndex1', blank=True, null=True) # Field name made lowercase.
    keeperindex2 = models.IntegerField(db_column='KeeperIndex2', blank=True, null=True) # Field name made lowercase.
    keeperindex3 = models.IntegerField(db_column='KeeperIndex3', blank=True, null=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KeeperPreferenceTable'

class LibKeeperpreferencetable1(models.Model):
    deweycallnumber = models.CharField(db_column='DeweyCallNumber', max_length=100, blank=True) # Field name made lowercase.
    keeperindex1 = models.IntegerField(db_column='KeeperIndex1', blank=True, null=True) # Field name made lowercase.
    keeperindex2 = models.IntegerField(db_column='KeeperIndex2', blank=True, null=True) # Field name made lowercase.
    keeperindex3 = models.IntegerField(db_column='KeeperIndex3', blank=True, null=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_KeeperPreferenceTable1'

class LibPre96CbDb(models.Model):
    pre96assessionnumber = models.CharField(db_column='Pre96AssessionNumber', max_length=100, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    pre96classnumber = models.CharField(db_column='Pre96ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=60, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_Pre96CB-DB'

class LibPre96CbDb1(models.Model):
    pre96assessionnumber = models.CharField(db_column='Pre96AssessionNumber', max_length=100, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    pre96classnumber = models.CharField(db_column='Pre96ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=60, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_Pre96CB-DB1'

class LibPre96EbDb(models.Model):
    pre96assessionnumber = models.CharField(db_column='Pre96AssessionNumber', max_length=100, blank=True) # Field name made lowercase.
    pre96classnumber = models.CharField(db_column='Pre96ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=80, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_Pre96EB-DB'

class LibPre96EbDbOld(models.Model):
    pre96assessionnumber = models.CharField(db_column='Pre96AssessionNumber', max_length=100, blank=True) # Field name made lowercase.
    pre96classnumber = models.CharField(db_column='Pre96ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=80, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=20, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_Pre96EB-DB-old'

class LibRomanpinintable(models.Model):
    chinesecharacter = models.CharField(db_column='ChineseCharacter', max_length=10, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_RomanPinInTable'

class LibRomanpinintable1(models.Model):
    chinesecharacter = models.CharField(db_column='ChineseCharacter', max_length=10, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=12, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_RomanPinInTable1'

class LibVbstapes(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_VBSTapes'

class LibVbstapes1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_VBSTapes1'

class LibYcmDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YCM-DB'

class LibYcmDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=100, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=140, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YCM-DB1'

class LibYcvDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YCV-DB'

class LibYcvDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=400, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YCV-DB1'

class LibYebDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=60, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YEB-DB'

class LibYevDb(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YEV-DB'

class LibYevDb1(models.Model):
    classnumber = models.CharField(db_column='ClassNumber', max_length=20, blank=True) # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=6, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=120, blank=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=280, blank=True) # Field name made lowercase.
    clutternumber = models.CharField(db_column='ClutterNumber', max_length=10, blank=True) # Field name made lowercase.
    autocounter = models.IntegerField(db_column='AutoCounter', blank=True, null=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=40, blank=True) # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=160, blank=True) # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=510, blank=True) # Field name made lowercase.
    keeper = models.CharField(db_column='Keeper', max_length=40, blank=True) # Field name made lowercase.
    keeperindex = models.IntegerField(db_column='KeeperIndex', blank=True, null=True) # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YEV-DB1'

class LibYearindextable(models.Model):
    yearindex = models.CharField(db_column='YearIndex', max_length=8, blank=True) # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=12, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YearIndexTable'

class LibYearindextable1(models.Model):
    yearindex = models.CharField(db_column='YearIndex', max_length=8, blank=True) # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=12, blank=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'LIB_YearIndexTable1'
