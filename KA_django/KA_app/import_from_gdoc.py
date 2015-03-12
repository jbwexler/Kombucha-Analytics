import gspread
import local
from django.db.models.loading import get_model
from KA_app.models import *

def updateBrews(wks):
    manyToMany = [x.attname for x in Brew._meta.many_to_many]
    brewLists = wks.worksheet('Brew').get_all_values()
    brewFields = [field for field in brewLists[2]]
    print len(brewFields)
    for row in brewLists[3:]:
        try:
            brewObj = Brew.objects.get(pk=row[0])
        except:
            brewObj = Brew.objects.create(pk=row[0])
        for column, value in enumerate(row):
            if brewFields[column] in manyToMany:
                model = get_model('KA_app',brewFields[column])
                print model
                addObj = model.objects.get(name=value)
                getattr(brewObj, brewFields[column]).add(addObj)
            brewObj.__dict__[brewFields[column]] = value
        brewObj.save()

def importFromGDoc():
    email = local.email
    password = local.password
    
    # Login with your Google account
    gc = gspread.login(email, password)
    
    # Open a worksheet from spreadsheet with one shot
    wks = gc.open("Kombucha Tasting HyperCube")
    
#     bottleLists = wks.worksheet('Bottle').get_all_values()
#     containerLists = wks.worksheet('Container').get_all_values()
#     teaLists = wks.worksheet('Tea').get_all_values()

    updateBrews(wks)
    
        
importFromGDoc()