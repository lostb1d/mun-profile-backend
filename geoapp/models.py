from django.db import models
from django.contrib.gis.db import models



# Create your models here.

class MunDetail(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/', default='', null='TRUE')
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    slogan = models.CharField(max_length=255)
    noOfWards = models.IntegerField()
    introduction = models.TextField()

    def __str__(self):
        return self.name

    # employee details 
class StaffDetail(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    level = models.IntegerField()

    def __str__(self):
        return self.name


    #ward office detail 
class WardDetail(models.Model):
    wardNo = models.IntegerField()
    address = models.CharField(max_length=100)
    introduction = models.TextField()

    president = models.CharField(max_length=30)
    presidentContact = models.CharField(max_length=10)
    presidentImage = models.ImageField(upload_to='images/')
    
    secretary = models.CharField(max_length=30)
    secretaryContact = models.CharField(max_length=10)
    secretaryImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.wardNo)
    
#demographic details    
class Demographic(models.Model):
    ward = models.ForeignKey(WardDetail, on_delete=models.CASCADE)

    totalPopulation = models.IntegerField()
    malePopulation = models.IntegerField()
    femalePopulation = models.IntegerField()
    otherPopulation = models.IntegerField()

    childPopulation = models.IntegerField()
    teenagePopulation = models.IntegerField()
    youngPopulation = models.IntegerField()
    oldAgePopulation = models.IntegerField()

    def __str__(self):
        return str(self.ward.wardNo)

class Education(models.Model):
    ward = models.ForeignKey(WardDetail, on_delete=models.CASCADE)
    uneducated = models.IntegerField()
    fundamental = models.IntegerField()
    preprimary =  models.IntegerField()
    primary = models.IntegerField()
    bachelor = models.IntegerField()
    master = models.IntegerField()
    technicalSLC = models.IntegerField()
    generalEducation = models.IntegerField()
    underAge = models.IntegerField()

    def __str__(self):
        return str(self.ward.wardNo)
    
class Occupation(models.Model):
    ward = models.ForeignKey(WardDetail, on_delete=models.CASCADE)
    agricultureLivestock = models.IntegerField()
    student  = models.IntegerField()
    underage  = models.IntegerField()
    civilServant  = models.IntegerField()
    privateOffice   = models.IntegerField()
    unemployed  = models.IntegerField()
    labour  = models.IntegerField()
    foreignEmployment  = models.IntegerField()

    def __str__(self):
        return str(self.ward.wardNo)
    
class DangPop(models.Model):
    gid = models.AutoField(primary_key=True)
    palika = models.CharField(max_length=80, blank=True, null=True)
    distric = models.CharField(max_length=80, blank=True, null=True)
    gapa_na = models.CharField(max_length=80, blank=True, null=True)
    gn_type = models.CharField(max_length=80, blank=True, null=True)
    provinc = models.IntegerField(blank=True, null=True)
    distrct = models.CharField(max_length=80, blank=True, null=True)
    type_gn = models.CharField(max_length=80, blank=True, null=True)
    ttl_fmly = models.IntegerField( blank=True, null=True, default=0)
    totl_hs = models.IntegerField(blank=True, null=True, default=0)
    ttl_ppl = models.IntegerField(blank=True, null=True, default=0)
    totl_ml = models.IntegerField(blank=True, null=True, default=0)
    totl_fml = models.IntegerField(blank=True, null=True, default=0)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dang_pop'

    def __str__(self):
        return self.gapa_na