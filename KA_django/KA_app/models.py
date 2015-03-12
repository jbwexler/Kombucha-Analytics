from django.db import models

class Enum(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
        
class Scoby(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ManyToManyField('self', null=True, blank=True)
    def __str__(self):
        return self.name
        
class Tea(models.Model):
    name = models.CharField(max_length=200)
    type = models.ManyToManyField(Enum, related_name='teas', null=True, blank=True)
    def __str__(self):
        return self.name
        

class Container(models.Model):
    name = models.CharField(max_length=200)
    volume = models.FloatField(null=True, blank=True)
    shape = models.ManyToManyField(Enum, related_name='containers', null=True, blank=True)
    def __str__(self):
        return self.name
        
class Brew(models.Model):
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    container = models.ManyToManyField(Container, related_name='brews', null=True, blank=True)
    teaType = models.ManyToManyField(Tea, related_name='brews', null=True, blank=True)
    teaStrength = models.IntegerField(null=True, blank=True)
    sugarType = models.ManyToManyField(Enum, related_name='brews_sugar', null=True, blank=True)
    sugarConc = models.FloatField(null=True, blank=True)
    waterType = models.ManyToManyField(Enum, related_name='brews_water', null=True, blank=True)
    waterVol = models.FloatField(null=True, blank=True)
    scoby = models.ManyToManyField(Scoby, related_name='brews', null=True, blank=True)
    def __str__(self):              
        return self.startDate
        
    def brewTime(self):
        return (self.endDate - self.starDate).days()
        
class Bottle(models.Model):
    name = models.CharField(max_length=200)
    brew = models.ManyToManyField(Brew, related_name='bottles', null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    shape = models.ManyToManyField(Enum, related_name='bottles_shape', null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    bottleType = models.ManyToManyField(Enum, related_name='bottles_type', null=True, blank=True)

    def __str__(self):
        return self.name
        