import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_resultado.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar solo números")

ventana = tk.Tk()
ventana.title("Convertidor de Temperatura")

frame = tk.Frame(ventana)
frame.pack(padx=10, pady=10)

label_titulo = tk.Label(frame, text="Convertidor de Temperatura", font=("Arial", 16))
label_titulo.grid(row=0, columnspan=2, pady=10)

label_celsius = tk.Label(frame, text="Celsius:")
label_celsius.grid(row=1, column=0, padx=5, pady=5)

entry_celsius = tk.Entry(frame)
entry_celsius.grid(row=1, column=1, padx=5, pady=5)

button_convertir = tk.Button(frame, text="Convertir", command=convertir)
button_convertir.grid(row=2, columnspan=2, pady=5)

label_resultado = tk.Label(frame, text="Resultado en Fahrenheit")
label_resultado.grid(row=3, columnspan=2, pady=5)

ventana.mainloop()
