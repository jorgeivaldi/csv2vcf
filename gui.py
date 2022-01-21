import os
import PySimpleGUI as sg
from lib import csv2vcf
from libs.csv import getheader_fromcsv
from libs.file import startfile

def main():
    path_csv = ""
    vcf_output = ""
    header = []
    fields_header = []

    sg.theme("Material2")
    layout_fields = [
      [
        sg.Checkbox("nombre (requerido)",key="check_nombre",disabled=True,pad=((20,10),(8,1)),default=False),
      ],
      [
        sg.Checkbox("celular (requerido)",key="check_cel",disabled=True,pad=((20,10),1),default=False),
      ],
      [
        sg.Checkbox("direccion (opcional)",key="check_dir",disabled=True,pad=((20,10),1),default=False),
      ]
    ]
    layout = [
        [
            sg.Text("Archivo CSV",justification="l")
        ],
        [
            sg.Input(default_text="",pad=(6,(0,20)), enable_events=True,key="file_csv",size=(37,1),readonly=True),
            sg.FileBrowse("Abrir",pad=(6,(0,20)),key="btn_open_csv",size=(5,1),file_types=[("CSV",".csv")])
        ],
        [
            sg.Text("Destino",size=(15,1),justification="l")
        ],
        [
            sg.Input(default_text="", enable_events=True,pad=(6,(0,10)),key="output",size=(37,1),readonly=True),
            sg.FileSaveAs("Elegir",pad=(6,(0,10)),key="btn_output_vcf",size=(5,1),file_types=[("VCF",".vcf")])
        ],
        [
            sg.Column(
                [
                    [sg.Frame("Campos",layout_fields,size=(340,100))]
                ],
                pad=(1,(10,20)),
            )
        ],
        [
            sg.Submit("Convertir",pad=(6,1), disabled=True),
        ]
    ]
    window = sg.Window('csv2vcf - by jorge', layout, icon="icon.ico", finalize=True,size=(370,320))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:        # if window was closed
            break
        elif event == "file_csv" and values["file_csv"] != "":
            if path_csv != values["file_csv"]:
                path_csv = values["file_csv"]
                print("file_csv >", values["file_csv"])
                fields_header = getheader_fromcsv(path_csv)
                print("header of file:", fields_header)
                # reseteo valores
                window["check_nombre"].update(value=False)
                window["check_cel"].update(value=False)
                window["check_dir"].update(value=False)
                # establezco valores
                if "nombre" in fields_header: window["check_nombre"].update(value=True)
                if "celular" in fields_header: window["check_cel"].update(value=True)
                if "direccion" in fields_header: window["check_dir"].update(value=True)

        elif event == "field_name" and values["field_name"] != "":
            print("field_name >", values["field_name"])
        elif event == "output" and values["output"] != "":
            if vcf_output != values["output"]:
                vcf_output = values["output"]
                print("output >", values["output"])

        elif event == 'Convertir':
            if path_csv == "":
                sg.popup("Debes seleccionar un archivo CSV",title="Advertencia")
                window.Element("btn_open_csv").SetFocus()
            elif vcf_output == "":
                sg.popup("Debe ingresar una tarjeta de contacto de salida",title="Advertencia")
                window.Element("btn_output_vcf").SetFocus()
            else:
              if not values["check_nombre"] or not values["check_cel"]:
                sg.popup("Los siguientes campos del Archivo CSV son requeridos","nombre, celular",title="Advertencia")
              else:
                print("Convirtiendo CSV a VCF")
                print("Data:")
                print("csv:",path_csv)
                print("output:",vcf_output)
                print("fields:",fields_header)
                csv2vcf(path_csv, vcf_output, debug_enabled=False, want_write_file=True)
                sg.popup("Archivo convertido con éxito",title="Información")
                output_folder = os.path.dirname(vcf_output)
                startfile(output_folder)
        # SI SE SELECCIONO CSV Y SE ESTABLECIO EL ARCHIVO VCF DE SALIDA
        # ACTIVO EL BOTON CONVERTIR
        if path_csv != "" and vcf_output != "":
            window["Convertir"].update(disabled=False)
    window.close()

if __name__ == "__main__":
    main()
