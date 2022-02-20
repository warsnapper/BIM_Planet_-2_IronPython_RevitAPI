import clr
clr.AddReference('RevitAPI') 

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import ElementCategoryFilter, BuiltInCategory, BuiltInParameter


filter = ElementCategoryFilter(BuiltInCategory.OST_Walls)
elements = FEC(doc).WherePasses(filter).WhereElementIsElementType()

for element in elements:
    bprint(element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK].Id.IntegerValue)
    # print type(element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK])

# bprint(elements)