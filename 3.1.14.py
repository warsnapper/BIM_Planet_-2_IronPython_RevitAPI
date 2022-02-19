import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredWorksetCollector as FWC
from Autodesk.Revit.DB import WorksetKind

familyWorksets = FWC(doc).OfKind(WorksetKind.FamilyWorkset)
viewWorksets = FWC(doc).OfKind(WorksetKind.ViewWorkset)

number_of_familyWorksets = len(list(familyWorksets))
number_of_viewWorksets = len(list(viewWorksets))

print number_of_familyWorksets + number_of_viewWorksets