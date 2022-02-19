import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
from System.Collections.Generic import List

walls_filter = DB.ElementClassFilter(DB.WallType)
floors_filter = DB.ElementClassFilter(DB.FloorType)
roofs_filter = DB.ElementClassFilter(DB.RoofType)
rooms_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Rooms)
stairs_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Stairs)
curtainWallMullions_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_CurtainWallMullions)

all_filters = [walls_filter, floors_filter, roofs_filter, rooms_filter, stairs_filter, curtainWallMullions_filter]
all_filters_typed = List[DB.ElementFilter](all_filters)

logical_or_filter = DB.LogicalOrFilter(all_filters_typed)

elements = FEC(doc).WherePasses(logical_or_filter)

print elements.GetElementCount() # количесво элементов в коллекторе int

excluded_uniqueIds = [
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b4',
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b6',
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b7',
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b9',
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8ba',
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bc',
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bd',
                    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bf',
                    ]

excluded_elementIds = []
for element in elements:
    if element.UniqueId in excluded_uniqueIds:
        excluded_elementIds.append(element.Id)

excluded_elementIds_typed = List[DB.ElementId](excluded_elementIds)

elements = elements.Excluding(excluded_elementIds_typed)

print elements.GetElementCount() # количесво элементов в коллекторе int

print sum([element.Id.IntegerValue for element in elements])

#-----------------------------------------------------------------------------------------------------------

# intElementIds = [element.Id.IntegerValue for element in elements]
# sumId = sum(intElementIds)
# print sumId
# print ''

# for element in elements:
#     if element.UniqueId in excluded_uniqueId:
#         print element.Id.IntegerValue
#         sumId -= element.Id.IntegerValue
#         print sumId

#-----------------------------------------------------------------------------------------------------------

# elements = [element for element in elements]
# print len(elements)

# def checking_availability(elements, excluded_uniqueId):
#     for element in elements:
#         if element.UniqueId in excluded_uniqueId:
#             print element.UniqueId

# checking_availability(elements, excluded_uniqueId)

# list_idexes = []
# for element in elements:
#     if element.UniqueId in excluded_uniqueId:
#         list_idexes.append(elements.index(element))

# for i in list_idexes:
#     del elements[i]

# print len(elements)

# checking_availability(elements, excluded_uniqueId)

# elementIds = [element.Id for element in elements]
# intElementIds = [element.IntegerValue for element in elementIds]

# print sumId

#-----------------------------------------------------------------------------------------------------------

# for elem in elements:
#     if elem.UniqueId in excluded_uniqueId:
#         print 'Yes'

# bprint(elements)
# # для проверки будем выводить на печать как полученный элемент, так и имя его категории
# bprint([(element, element.Category.Name) for element in elements])
# print elements.GetElementCount()
