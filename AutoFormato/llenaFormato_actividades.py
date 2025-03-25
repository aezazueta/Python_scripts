import pandas as pd
from docxtpl import DocxTemplate
import os

# ruta del archivo actual
path_file = os.path.abspath(__file__)
# ruta de la plantilla
path_template = os.path.dirname(path_file)+'/PR-10-F04 REPORTE DE PROYECTOS INDIVIDUALES DEL DOCENTE.docx'
# ruta de la carpeta de salida
path_out = os.path.dirname(path_file)+'/reportes'

# objeto DocxTemplate
doc = DocxTemplate(path_template)
# carga de datos desde archivo excel
data = pd.read_excel('Actividades.xlsx')
# captura del nombre de docente y jefe de academia
profesor = input('Capture el nombre del docente del reporte----> ')
jefe_academico = input('Capture el nombre del jefe de academia ---->')

# recorrido por cada uno de los registros del archivo excel
for index, fila in data.iterrows():
    # print('\n\n index \t', index)
    # print( fila)
    # en un diccionario se cargan cada uno de los campos del registro para ser utilizados en la plantilla
    context = {
        'periodo':fila['periodo'],
        'año':fila['año'],
        'nombre':fila['nombre'],
        'proyecto':fila['proyecto'],
        'objetivo': fila['objetivo'],
        'descripcion': fila['descripcion'],
        'metas':fila['metas'],
        'actividades': fila['actividades'],
        'evidencias':fila['evidencias'],
        'conclusiones':fila['conclusiones'],
        'observaciones': fila['observaciones'],
        'profesor': profesor,
        'jefe_academico' : jefe_academico
    }

    # renderizado de la plantilla con los datos del registro
    doc.render(context)
    # guardado del reporte en la carpeta de salida con el nombre del proyecto
    doc.save(f'PR-10-F04 REPORTE DE PROYECTOS INDIVIDUALES {profesor}_{fila["proyecto"]}.docx')