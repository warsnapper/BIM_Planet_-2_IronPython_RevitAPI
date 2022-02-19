import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB

elements = FEC(doc).OfClass(DB.View)

elementIds = [element.Id for element in elements]

bprint(elementIds)