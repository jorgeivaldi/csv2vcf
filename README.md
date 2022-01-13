# CSV To VCF

Convierte archivo CSV a Tarjeta VCF (varias en una)

## How to use
En main.py debes reemplazar **CONTACTOS.csv** por tu archivo csv, y debes respetar el **orden y nombres** de las columnas:

[**nombre**, **celular**, **direccion**]
o
[**nombre**, **celular**]

```bash
virtualenv venv
source venv/bin/activate
python main.py
```

En la carpeta output se generara el archivo **contactos.vcf** con todas las tarjetas vcf