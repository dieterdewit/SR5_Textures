from KryuGL import *

# Posicion de la Camara
eye = V3(1, 1, 5)
center = V3(0, 0, 0)
displace = V3(0, 1, 0)

# Llama las funciones para la escritura de la imagen .bmp
r = Bitmap(600, 600)
r.glViewPort(1, 1, 599, 599)
r.lookAt(eye, center, displace)

# Lectura de la Textura
fondo = Texture('./Fondo/fondo.bmp')
r.framebuffer_fondo(fondo)

# Se elige un shader a utilizar en los modelos siguientes
r.shader = r.gouraud

# ---------- Cargar los modelos bmp con textura mtl ----------
# Tie-Fighter
r.glLoad(
    './Modelos/tie.obj',
    mtl='./Modelos/tie.mtl',
    translate=(0.5,0.5,0),
    scale=(0.5,0.5,0.5),
    rotate=(0.2,-0.2,0)
    )

r.glClearZbuffer()

# ------------------------------------------------------------

# Creacion del Archivo
r.glFinish('StarWars_15146.bmp')
