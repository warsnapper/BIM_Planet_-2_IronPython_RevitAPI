import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
from System.Collections.Generic import List

roomTags_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_RoomTags)
doorTags_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_DoorTags)
windowTags_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_WindowTags)
wallTags_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_WallTags)

all_filters = [roomTags_filter, doorTags_filter, windowTags_filter, wallTags_filter]
all_filters_typed = List[DB.ElementFilter](all_filters)

logical_or_filter = DB.LogicalOrFilter(all_filters_typed)

list_of_Ids = [695, 136343]
sumIds = 0

for id in list_of_Ids:
    elements = FEC(doc, DB.ElementId(id)).WherePasses(logical_or_filter)
    elementIds = [element.Id.IntegerValue for element in elements]
    sumIds += sum(elementIds)

print sumIds

# elements = FEC(doc).OfClass(DB.View)

# elementIds = [element.Id for element in elements]

# bprint(elementIds)