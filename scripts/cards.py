# -*- coding: utf-8 -*-
print("# -*- coding: utf-8 -*-")
import sys
print("import sys")
from PIL import Image, ImageDraw, ImageFont
print("from PIL import Image, ImageDraw, ImageFont")
import os
print("import os")

print("Importando librerías PIL y os")

# Definir el directorio de las imágenes
images_dir = os.path.join("..", "images")
print(f"Directorio de imágenes definido como: {images_dir}")

# Obtener el nombre del archivo de la plantilla desde el primer parámetro o usar el valor por defecto
if len(sys.argv) > 1:
    template_filename = sys.argv[1]
    print(f"Nombre de la plantilla proporcionado como argumento: {template_filename}")
else:
    template_filename = "card_template.jpg"
    print(f"No se proporcionó nombre de plantilla, usando el valor por defecto: {template_filename}")

template_path = os.path.join(images_dir, template_filename)
print(f"Ruta completa de la plantilla: {template_path}")

try:
    # Cargar la plantilla de la carta
    card = Image.open(template_path)
    print(f"Plantilla de carta cargada exitosamente desde: {template_path}")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo de plantilla en la ruta: {template_path}")
    sys.exit(1)

# Obtener el nombre del archivo de salida desde el segundo parámetro o usar el valor por defecto
if len(sys.argv) > 2:
    output_filename = sys.argv[2]
    print(f"Nombre del archivo de salida proporcionado como argumento: {output_filename}")
else:
    output_filename = "card01.jpg"
    print(f"No se proporcionó nombre de archivo de salida, usando el valor por defecto: {output_filename}")

output_path = output_filename
print(f"Ruta completa del archivo de salida: {output_path}")

# Obtener el nombre de la fuente desde el tercer parámetro o usar el valor por defecto
if len(sys.argv) > 3:
    font_filename = sys.argv[3]
    print(f"Nombre de la fuente proporcionado como argumento: {font_filename}")
    font_path = font_filename # Se asume que la ruta completa o el nombre del archivo .ttf se proporciona
else:
    font_path = "arialbd.ttf" # Arial Bold (si existe)
    print(f"No se proporcionó nombre de fuente, usando el valor por defecto: {font_path}")

font_size = 40
print(f"Tamaño de la fuente definido como: {font_size}")

# Cargar los logos
try:
    logo1_path = os.path.join(images_dir, "logo1.jpg")
    print(f"Ruta del Logo 1 definida como: {logo1_path}")
    logo1_original = Image.open(logo1_path).convert("RGBA")
    print(f"Logo 1 original cargado desde: {logo1_path}")

    # Definir el nuevo tamaño para el logo 1 (por ejemplo, aumentar el ancho a XX manteniendo la proporción)
    aspect_ratio = logo1_original.width / logo1_original.height
    print(f"Relación de aspecto del Logo 1: {aspect_ratio}")
    logo1_new_width = 220
    print(f"Nuevo ancho deseado para el Logo 1: {logo1_new_width}")
    logo1_new_height = int(logo1_new_width / aspect_ratio)
    print(f"Nueva altura calculada para el Logo 1: {logo1_new_height}")
    logo1_new_size = (logo1_new_width, logo1_new_height)
    print(f"Nuevo tamaño del Logo 1: {logo1_new_size}")
    logo1 = logo1_original.resize(logo1_new_size)
    print(f"Logo 1 redimensionado a: {logo1_new_size}")


except FileNotFoundError:
    print(f"Advertencia: No se encontró el archivo del Logo 1 en la ruta: {logo1_path}")
    logo1 = None

try:
    logo2_path = os.path.join(images_dir, "370x200_ECSF_Roadmap12.jpg")
    print(f"Ruta del Logo 2 definida como: {logo2_path}")
    logo2_original = Image.open(logo2_path).convert("RGBA")
    print(f"Logo 2 original cargado desde: {logo2_path}")

    # Definir el nuevo tamaño para el logo 2 (por ejemplo, aumentar el ancho a XX manteniendo la proporción)
    aspect_ratio = logo2_original.width / logo2_original.height
    print(f"Relación de aspecto del Logo 2: {aspect_ratio}")
    logo2_new_width = 800
    print(f"Nuevo ancho deseado para el Logo 2: {logo2_new_width}")
    logo2_new_height = int(logo2_new_width / aspect_ratio)
    print(f"Nueva altura calculada para el Logo 2: {logo2_new_height}")
    logo2_new_size = (logo2_new_width, logo2_new_height)
    print(f"Nuevo tamaño del Logo 2: {logo2_new_size}")
    logo2 = logo2_original.resize(logo2_new_size)
    print(f"Logo 2 redimensionado a: {logo2_new_size}")

except FileNotFoundError:
    print(f"Advertencia: No se encontró el archivo del Logo 2 en la ruta: {logo2_path}")
    logo2 = None

# Crear un objeto de dibujo
draw = ImageDraw.Draw(card)
print("Objeto de dibujo creado")

# Definir la fuente y el color del texto
orange_color = (255, 165, 0)
print(f"Color del texto definido como naranja: {orange_color}")

try:
    font = ImageFont.truetype(font_path, font_size)
    print(f"Fuente cargada exitosamente desde: {font_path} con tamaño: {font_size}")
except IOError:
    try:
        font = ImageFont.truetype("arial.ttf", font_size) # Intenta con Arial regular si bold no existe
        print(f"No se pudo cargar la fuente desde: {font_path}, usando Arial con tamaño: {font_size}")
    except IOError:
        font = ImageFont.load_default()
        print(f"No se pudo cargar la fuente Arial, usando fuente por defecto")

# Definir las posiciones para las capas (ajusta estos valores según tu plantilla y los nuevos tamaños de los logos)
logo1_position = (400, 120)
print(f"Posición del Logo 1 definida como: {logo1_position}")

# Ajustar la posición del logo 2 considerando su nuevo tamaño
logo2_position = (110, 400)
print(f"Posición del Logo 2 definida como: {logo2_position}")
text1_position = (110, 920)
print(f"Posición del Texto 1 definida como: {text1_position}")
text2_position = (110, 1080)
print(f"Posición del Texto 2 definida como: {text2_position}")
text3_position = (110, 1225)
print(f"Posición del Texto 3 definida como: {text3_position}")
text4_position = (110, 1350) # Ejemplo de posición centrada
print(f"Posición del Texto 4 definida como: {text4_position}")

# Pegar los logos si se cargaron
if logo1:
    card.paste(logo1, logo1_position, logo1)
    print(f"Logo 1 pegado en la posición: {logo1_position}")

if logo2:
    card.paste(logo2, logo2_position, logo2)
    print(f"Logo 2 pegado en la posición: {logo2_position}")

# Dibujar los textos
draw.text(text1_position, "Rol", fill=orange_color, font=font)
print(f"Texto 'Rol' dibujado en la posición: {text1_position} con color naranja")

draw.text(text2_position, "CISO: Director de Seguridad Corporativa", fill=orange_color, font=font)
print(f"Texto 'CISO: Director de Seguridad Corporativa' dibujado en la posición: {text2_position} con color naranja")

draw.text(text3_position, "Habilidades", fill=orange_color, font=font)
print(f"Texto 'Habilidades' dibujado en la posición: {text3_position} con color naranja")

draw.text(text4_position, "Capacidad de gestión de riesgos", fill=orange_color, font=font)
print(f"Texto 'Capacidad de gestión de riesgos' dibujado en la posición: {text4_position} con color naranja")

# Guardar la imagen resultante
try:
    card.save(output_path)
    print(f"Imagen guardada exitosamente en: {output_path}")
except Exception as e:
    print(f"Error al guardar la imagen: {e}")

print("Script finalizado.")
