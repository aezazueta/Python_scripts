from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'PhotoEditor/imgs'
pathOut = 'PhotoEditor/editedImgs'

for file in os.listdir(path):
    #carga de la imagen a editar
    img = Image.open(f"{path}/{file}")
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
    edit_im.save(f'{pathOut}/{clean_name}_edited.jpg')