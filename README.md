> [!NOTE]
Practica hecha por el alumno David Enrique Pérez Bejarano

> [!CAUTION]
Es necesario el copiado mediante git bash en condición de windows abajo del 11 o uso simple de la terminal para activar este archivo para su mejor comprensión

> [!IMPORTANT]
Uso pleno de Python para la creacion de imagenes cambiando colores usando arrays (tambien puede usarse con videos)

> [!TIP]
Se dejo el codigo para un copiado más simple tomando en cuenta que puede usarse de forma más simple así.

```html
# crear una carpeta de salida si no existe
if not os.path.exists("output_imagenes"):
    os.makedirs("output_imagenes")
    print("Carpeta 'output_imagenes' creada.")

# lectura y visualización de la imagen
imagen_path = "data/imagen1.jpg"
imagen = cv2.imread(imagen_path)

image_as_np = np.array(imagen)


#Aplicacion de filtro mas complejo de 5x5
kernel = np.array(
[
    [1 , 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1 , 4, 6, 4, 1]
], dtype=np.float32
)

kernel /= 256.0 # Normalización del kernel

test_image_as_np = cv2.filter2D(image_as_np, -1, kernel)
cv2.imwrite("output_imagenes/imagen_filtrada_5x5.jpg", test_image_as_np)

print(f"muestra la imagen como array de numpy:\n{image_as_np}")

if imagen is None:
    raise FileNotFoundError(f"No se pudo cargar la imagen en {imagen_path}")

# guardar copia original
cv2.imwrite("output_imagenes/imagen_original.jpg", imagen)  

```
