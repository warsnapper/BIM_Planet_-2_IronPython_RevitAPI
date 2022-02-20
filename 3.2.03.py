from tabnanny import check
import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import BuiltInParameter, Parameter

def parameter_chek(parameter):
    types = [
        'системный',
        'несистемный'
    ]
    if isinstance (parameter, Parameter):
        b_parameter = parameter.Definition.BuiltInParameter
        check = b_parameter == BuiltInParameter.INVALID
        print 'Параметр с Id {} - {}'.format(parameter.Id, types[check])
        print 'Значение его перечисления равно {}\n'.format(b_parameter)
    else:
        print 'Некорректный аргумент\n' \
              'Необходим экземпляр класса Parameter\n'

element = selection[0]
marks = element.GetParameters('Марка')
for mark in marks:
    parameter_chek(mark)

parameter_chek('WrongElement')

