import clr
clr.AddReference('RevitAPI') 

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import ElementCategoryFilter, BuiltInCategory, BuiltInParameter, WallType


# filter = ElementCategoryFilter(BuiltInCategory.OST_Walls)
# elements = FEC(doc).WherePasses(filter).WhereElementIsElementType()

# print len([element for element in elements])

elements = FEC(doc).OfClass(WallType)

# print len([element for element in elements])

sumIds = 0
for element in elements:
    try:
        # bprint(element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK].Id.IntegerValue)
        sumIds += element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK].Id.IntegerValue
        # print type(element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK])
    except:
        # print type(element.Category)
        bprint(element.Category.Name)
        bprint(element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK])

print sumIds