from PIL import Image, ImageEnhance, ImageFilter
import os

# ruta del archivo actual
path_file = os.path.abspath(__file__)
# ruta de la carpeta de imagenes
path_img = os.path.dirname(path_file)+'/imgs'
print(path_img)

pathOut = os.path.dirname(path_file)+'/editedImgs'
print(pathOut)

print('Editando imagenes con resaltado de bordes...')
# recorrido de la carpeta de imagenes
for file in os.listdir(path_img):
    #carga de la imagen a editar
    img = Image.open(f"{path_img}/{file}")
    # aplicacion de filtro de nitidez con conversion a escala de grises (modo L)
    edit = img.filter(ImageFilter.CONTOUR)

    # separacion del nombre del archivo de su extension
    clean_name = os.path.splitext(file)[0]
    # conversion de la imagen de RGB
    edit_im = edit.convert('RGB')
    # guardado de la imagen editada en la carpeta de salida
    edit_im.save(f'{pathOut}/{clean_name}_edit_CONTOUR.jpg')

print('Editando imagenes con efecto blur...')
# recorrido de la carpeta de imagenes
for file in os.listdir(path_img):
    #carga de la imagen a editar
    img = Image.open(f"{path_img}/{file}")
    # aplicacion de filtro de nitidez con conversion a escala de grises (modo L)
    edit = img.filter(ImageFilter.BLUR)

    # separacion del nombre del archivo de su extension
    clean_name = os.path.splitext(file)[0]
    # conversion de la imagen de RGB
    edit_im = edit.convert('RGB')
    # guardado de la imagen editada en la carpeta de salida
    edit_im.save(f'{pathOut}/{clean_name}_edit_BLUR.jpg')

print('Editando imagenes con delineado de bordes...')
# recorrido de la carpeta de imagenes
for file in os.listdir(path_img):
    #carga de la imagen a editar
    img = Image.open(f"{path_img}/{file}")
    # aplicacion de filtro de nitidez con conversion a escala de grises (modo L)
    edit = img.filter(ImageFilter.FIND_EDGES)

    # separacion del nombre del archivo de su extension
    clean_name = os.path.splitext(file)[0]
    # conversion de la imagen de RGB
    edit_im = edit.convert('RGB')
    # guardado de la imagen editada en la carpeta de salida
    edit_im.save(f'{pathOut}/{clean_name}_edit_FIND_EDGES.jpg')

print('Editando imagenes con mayor nitidez, contraste y conversion a escala de grises...')
# recorrido de la carpeta de imagenes
for file in os.listdir(path_img):
    #carga de la imagen a editar
    img = Image.open(f"{path_img}/{file}")
    # aplicacion de filtro de nitidez con conversion a escala de grises (modo L)
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    # creacion de un valor para incrementar contraste
    factor = 1.5
    # aplicacion de contraste a la imagen
    enhacer = ImageEnhance.Contrast(edit)
    edit = enhacer.enhance(factor)

    # separacion del nombre del archivo de su extension
    clean_name = os.path.splitext(file)[0]
    # conversion de la imagen de RGB
    edit_im = edit.convert('RGB')
    # guardado de la imagen editada en la carpeta de salida
    edit_im.save(f'{pathOut}/{clean_name}_edit_sharpen_BW.jpg')

print('Edicion de imagenes finalizada...')
