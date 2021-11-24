# CSV To VCF

Convierte archivo CSV a Tarjeta VCF (varias en una)

## How to use
En main.py debes reemplazar **CONTACTOS.csv** por tu archivo csv, y debes respetar el orden de las columnas:
*Nombre y Apellido, Celular, Dirección*
```bash
virtualenv venv
source venv/bin/activate
python main.py
```

En la carpeta output se generara el archivo **contactos.vcf** con todas las tarjetas vcf