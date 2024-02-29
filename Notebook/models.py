from django.db import models

# Create your models here.
class gep(models.Model):
    class Meta:
        #id=models.IntegerField()
        gyarto=models.CharField(max_length=255)
        tipus=models.CharField(max_length=255)
        kijelzo=models.IntegerField()
        memoria=models.IntegerField()
        merevlemez=models.IntegerField()
        videovezerlo=models.CharField(max_length=255)
        processzorid=models.IntegerField()
        oprendszerid=models.IntegerField()
        db=models.IntegerField()
        verbose_name="gep"
        verbose_name_plural="gepek"
    def __str__(self):
        return f"{self}"
    
class processzor(models.Model):
    class Meta:
        #id=models.IntegerField()
        gyarto=models.CharField(max_length=255)
        tipus=models.CharField(max_length=255)
        verbose_name="processzor"
        verbose_name_plural="processzorok"
    def __str__(self):
        return f"{self}"
    
class oprendszer(models.Model):
    class Meta:
        #id2=models.IntegerField()
        nev=models.CharField(max_length=255)
        verbose_name="oprendszer"
        verbose_name_plural="oprendszer"
    def __str__(self):
        return f"{self}"
