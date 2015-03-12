from django.db import models
        
class Scoby(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    parent = models.ManyToManyField('self', null=True, blank=True)
    dateCreated = models.DateField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.brew:
            BrewObj = self.brew.all()[0]
            self.startDate = BrewObj.endDate
        if self.endDate and self.startDate:
            self.brewTime = (self.endDate - self.startDate).days
        
        super(Brew, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.name
        
class Tea(models.Model):
    type_choices = (
    ('green', 'green'),
    ('white', 'white'),
    ('oolong', 'oolong'),
    ('shou', 'shou'),
    ('sheng', 'sheng')
    )
    
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200,choices=type_choices, null=True, blank=True)
    
    
#     def __str__(self):
#         return self.name
        

class Container(models.Model):
    shape_choices = (
    ('tall', 'tall'),
    ('wide', 'wide')
    )
    
    name = models.CharField(max_length=200, null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    shape = models.CharField(max_length=200,choices=shape_choices, null=True, blank=True)
#     def __str__(self):
#         return self.name
        
class Brew(models.Model):
    water_choices = (
    ('filtered', 'filtered'),
    ('unfiltered', 'unfiltered')
    )
    
    sugar_choices = (
    ('white', 'white'),
    ('brown', 'brown'),
    ('honey', 'honey'),
    ('local honey', 'local honey')
    )
    
    location_choices = (
    ('Tyler', 'Tyler'),
    ('Joe', 'Joe')
    )
    
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    brewTime = models.IntegerField(null=True, blank=True)
    container = models.ManyToManyField(Container, related_name='brews', null=True, blank=True)
    teaType = models.ManyToManyField(Tea, related_name='brews', null=True, blank=True)
    teaStrength = models.IntegerField(null=True, blank=True)
    waterType = models.CharField(max_length=200,choices=water_choices, null=True, blank=True)
    waterVol = models.FloatField(null=True, blank=True)
    sugarType = models.CharField(max_length=200,choices=sugar_choices, null=True, blank=True)
    sugarConc = models.FloatField(null=True, blank=True)
    scoby = models.ManyToManyField(Scoby, related_name='brews', null=True, blank=True)
    location = models.CharField(max_length=200,choices=location_choices, null=True, blank=True)

#     def __date__(self):              
#         return self.startDate
        
    def save(self, *args, **kwargs):
        if self.endDate and self.startDate:
            self.brewTime = (self.endDate - self.startDate).days
        super(Brew, self).save(*args, **kwargs)
        
class Bottle(models.Model):
    type_choices = (
    ('beer', 'beer'),
    ("gt's", "gt's"),
    )
    
    name = models.CharField(max_length=200, null=True, blank=True)
    brew = models.ManyToManyField(Brew, related_name='bottles', null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    bottleTime = models.IntegerField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=200,choices=type_choices, null=True, blank=True)
    joeRating = models.IntegerField(null=True, blank=True)
    tyRating = models.IntegerField(null=True, blank=True)
    avgRating = models.IntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.brew:
            BrewObj = self.brew.all()[0]
            self.startDate = BrewObj.endDate
        if self.endDate and self.startDate:
            self.brewTime = (self.endDate - self.startDate).days
        if self.joeRating and self.tyRating:
            self.avgRating = (self.joeRating + self.tyRating)/2
        
        super(Brew, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name
        