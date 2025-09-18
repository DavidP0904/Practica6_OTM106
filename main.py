import cv2
import os
import numpy as np

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

#conversion a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output_imagenes/imagen_gris.jpg", gris)

#aplicacion de filtro gaussiano
blur = cv2.GaussianBlur(imagen, (15, 15), 0)
cv2.imwrite("output_imagenes/imagen_blur.jpg", blur)

# lectura de video y extraccion de fotogramas
video_path = "data/video1.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(f"No se pudo abrir el video en {video_path}")

#ir al segundo 5 (aprox. frame 150 si el video es de 30 fps)
cap.set(cv2.CAP_PROP_POS_MSEC, 5000)
ret,frame = cap.read()

if ret:
    cv2.imwrite("output_imagenes/frame_segundo_5.jpg", frame)
else:
    print("No se pudo capturar el fotograma en el segundo 5.")

#cortar los primeros 10 segundos y guardar el video resultante
cap.set(cv2.CAP_PROP_POS_MSEC, 0) #reiniciar al inicio del video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
out = cv2.VideoWriter("output_imagenes/video_cortado.mp4", fourcc, fps, (width, height))
for i in range(int(fps * 10)): #10 segundos
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
out.release()

# convertir el video de 10 segundos a escala de grises iterando frame por frame y guardarlo
cap.set(cv2.CAP_PROP_POS_MSEC, 0) #reiniciar al inicio del video
out_gray = cv2.VideoWriter(
    "output_imagenes/video_gris.mp4", fourcc, fps, (width, height), isColor=False
    )
for i in range(int(fps * 10)): #10 segundos
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out_gray.write(gray_frame)
out_gray.release()
cap.release()
print("Procesamiento completado. Revisa la carpeta 'output_imagenes' para los resultados.")