from pathlib import path

BASE = path(__file__).resolve().parent.parent
print(BASE) #carpeta de mi proyecto 

raw = BASE / "data" / "raw"
clean = BASE / "data" / "clean"
#creacion de carpetas
raw.mkdir(parents =True,exist_ok = True)

clean.mkdir(parents =True,exist_ok = True)

#escribir a un archivo txt
txt_path = raw / "notas.tx"
txt_path.write_text("Mis alumnos novan a reprobar")

#leer ccv
"leer jeison"



