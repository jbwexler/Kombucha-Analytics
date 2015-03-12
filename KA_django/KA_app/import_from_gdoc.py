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
        if row[1]:
            try:
                brewObj = Brew.objects.get(pk=row[0])
            except:
                brewObj = Brew.objects.create(pk=row[0])
            for column, value in enumerate(row):
                if value:
                    if brewFields[column] in manyToMany:
                        depField = Brew._meta.get_field_by_name(brewFields[column])
                        model = depField[0].rel.to      
                        print value         
                        addObj = model.objects.get(name=value)
                        getattr(brewObj, brewFields[column]).add(addObj)
                    elif 'date' in brewFields[column].lower():
                        dateList = [int(float(x)) for x in value.split('-')]
                        brewObj.__dict__[brewFields[column]] = datetime.date(dateList[0],dateList[1],dateList[2])
                    else:
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