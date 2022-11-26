# importar librerias
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path

listaArchivos = []

# crear objeto para unir los pdf
unir = PdfFileMerger()


def abrir_archivo(files):
    filepath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not(filepath and Path(filepath).exists()):
        return
    files.append(filepath)
    # nombre del archivo
    lbl_items["text"] = '\n'.join(str(f) for f in files)
    if len(files) >= 2 and btn_merge['state'] == "disabled":
        btn_merge["state"] = "normal"


def unir_pdfs(archivos):
    for A in archivos:
        unir.append(PdfFileReader(open(A, "rb")))

    output_filename = ent_output_name.get()

    if not output_filename:
        output_filename = "Untitled.pdf"
    elif ".pdf" not in output_filename:
        output_filename += ".pdf"
    unir.write(output_filename)


# crear formulario
ventana = tk.Tk()
ventana.title("Unir pdfs")
ventana.geometry("500x500")
ventana.resizable(0, 0)
ventana.configure(bg='#0059b3')


# --- Preguntar para abrir archivo ---
fr_bg1 = tk.Frame(ventana, bd=3)
lbl_open = tk.Label(fr_bg1, text="Escoja dos archivos PDF para unir")
lbl_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_open = tk.Button(fr_bg1, text="Abrir PDFs",
                     command=lambda: abrir_archivo(listaArchivos))
btn_open.grid(row=1, column=0, sticky="ew", padx=5)
lbl_items = tk.Label(fr_bg1, text="")
lbl_items.grid(row=2, column=0, pady=5)
fr_bg1.pack()

# --- boton unir pdf ---
fr_bg2 = tk.Frame(ventana, bd=3)
lbl_to_merge = tk.Label(fr_bg2, text="Nombre del nuevo pdf")
lbl_to_merge.grid(row=0, column=0, sticky="ew", padx="5", pady="5")

ent_output_name = tk.Entry(master=fr_bg2, width=7)
ent_output_name.grid(row=1, column=0, sticky="ew")

btn_merge = tk.Button(fr_bg2,
                      text="Unir pdf",
                      command=lambda: unir_pdfs(listaArchivos))
btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
fr_bg2.pack()


# --- Boton de salir ---

boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bd=2)
boton_salir.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)

if __name__ == "__main__":
    ventana.mainloop()
