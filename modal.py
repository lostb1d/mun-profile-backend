# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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


class DangPop(models.Model):
    gid = models.AutoField(primary_key=True)
    palika = models.CharField(max_length=80, blank=True, null=True)
    distric = models.CharField(max_length=80, blank=True, null=True)
    gapa_na = models.CharField(max_length=80, blank=True, null=True)
    gn_type = models.CharField(max_length=80, blank=True, null=True)
    provinc = models.IntegerField(blank=True, null=True)
    distrct = models.CharField(max_length=80, blank=True, null=True)
    type_gn = models.CharField(max_length=80, blank=True, null=True)
    ttl_fmly = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totl_hs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ttl_ppl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totl_ml = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totl_fml = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dang_pop'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class GeoappDemographic(models.Model):
    id = models.BigAutoField(primary_key=True)
    totalpopulation = models.IntegerField(db_column='totalPopulation')  # Field name made lowercase.
    malepopulation = models.IntegerField(db_column='malePopulation')  # Field name made lowercase.
    femalepopulation = models.IntegerField(db_column='femalePopulation')  # Field name made lowercase.
    otherpopulation = models.IntegerField(db_column='otherPopulation')  # Field name made lowercase.
    childpopulation = models.IntegerField(db_column='childPopulation')  # Field name made lowercase.
    teenagepopulation = models.IntegerField(db_column='teenagePopulation')  # Field name made lowercase.
    youngpopulation = models.IntegerField(db_column='youngPopulation')  # Field name made lowercase.
    oldagepopulation = models.IntegerField(db_column='oldAgePopulation')  # Field name made lowercase.
    ward = models.ForeignKey('GeoappWarddetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'geoapp_demographic'


class GeoappEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    uneducated = models.IntegerField()
    fundamental = models.IntegerField()
    preprimary = models.IntegerField()
    primary = models.IntegerField()
    bachelor = models.IntegerField()
    master = models.IntegerField()
    technicalslc = models.IntegerField(db_column='technicalSLC')  # Field name made lowercase.
    generaleducation = models.IntegerField(db_column='generalEducation')  # Field name made lowercase.
    underage = models.IntegerField(db_column='underAge')  # Field name made lowercase.
    ward = models.ForeignKey('GeoappWarddetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'geoapp_education'


class GeoappMundetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    slogan = models.CharField(max_length=255)
    noofwards = models.IntegerField(db_column='noOfWards')  # Field name made lowercase.
    introduction = models.TextField()
    logo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geoapp_mundetail'


class GeoappOccupation(models.Model):
    id = models.BigAutoField(primary_key=True)
    agriculturelivestock = models.IntegerField(db_column='agricultureLivestock')  # Field name made lowercase.
    student = models.IntegerField()
    underage = models.IntegerField()
    civilservant = models.IntegerField(db_column='civilServant')  # Field name made lowercase.
    privateoffice = models.IntegerField(db_column='privateOffice')  # Field name made lowercase.
    unemployed = models.IntegerField()
    labour = models.IntegerField()
    foreignemployment = models.IntegerField(db_column='foreignEmployment')  # Field name made lowercase.
    ward = models.ForeignKey('GeoappWarddetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'geoapp_occupation'


class GeoappStaffdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'geoapp_staffdetail'


class GeoappWarddetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    wardno = models.IntegerField(db_column='wardNo')  # Field name made lowercase.
    address = models.CharField(max_length=100)
    introduction = models.TextField()
    president = models.CharField(max_length=30)
    presidentcontact = models.CharField(db_column='presidentContact', max_length=10)  # Field name made lowercase.
    presidentimage = models.CharField(db_column='presidentImage', max_length=100)  # Field name made lowercase.
    secretary = models.CharField(max_length=30)
    secretarycontact = models.CharField(db_column='secretaryContact', max_length=10)  # Field name made lowercase.
    secretaryimage = models.CharField(db_column='secretaryImage', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geoapp_warddetail'


class NplMajrdslGist(models.Model):
    gid = models.AutoField(primary_key=True)
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    length = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    np_road_field = models.IntegerField(db_column='np_road_', blank=True, null=True)  # Field renamed because it ended with '_'.
    np_road_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiLineStringField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'npl_majrdsl_gist'


class Palika(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.FloatField(blank=True, null=True)
    palika = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    gapa_napa = models.CharField(max_length=50, blank=True, null=True)
    gn_type = models.CharField(max_length=50, blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palika'
