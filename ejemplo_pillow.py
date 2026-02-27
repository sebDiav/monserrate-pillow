from PIL import Image, ImageDraw

# Abrir imagen de Monserrate
imagen = Image.open("monserrate.png")

print("Tamaño:", imagen.size)
print("Formato:", imagen.format)
print("Modo:", imagen.mode)

# Redimensionar imagen
imagen = imagen.resize((600, 400))

# Convertir a escala de grises
imagen = imagen.convert("L")

# Convertir nuevamente a RGB para poder dibujar texto
imagen = imagen.convert("RGB")

# Crear objeto para dibujar
draw = ImageDraw.Draw(imagen)

# Texto cultural
texto = "Santuario de Monserrate - Patrimonio Cultural Colombiano"

# Posición del texto
posicion = (20, 350)

# Agregar texto
draw.text(posicion, texto, fill=(255, 255, 255))

# Guardar imagen final
imagen.save("monserrate_cultural.jpg")

print("Imagen cultural generada correctamente.")
