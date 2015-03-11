from django.db import models

class Bottle(models.Model):
    name = models.CharField()
    brew = models.ForeignKey(Brew)
    startDate = models.DateField()
    endDate = models.DateField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Brew(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    container = models.ManytoManyField(Container)
    teaType = models.ManyToManyField(Tea)
    teaStrength = models.IntegerField()
    sugarType = models.ForeignKey(Enum)
    sugarConc = models.FloatField()
    waterType = models.ForeignKey(Enum)
    waterVol = models.FloatField()
    
    
    
    def __str__(self):              
        return self.startDate
        
    def brewTime(self):
        return (self.endDate - self.starDate).days()

class Container(models.Model):
    name = models.CharField()
    volume = models.FloatField()
    shape = models.ForeignKey(Enum)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
class Scoby(models.Model):
    name = models.CharField()
    parent = models.ManyToManyField('self')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
        
class Tea(models.Model):
    name = models.CharField()
    type = models.ForeignKey(Enum)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
        

class Enum(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
        