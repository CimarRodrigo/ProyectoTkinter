import tkinter as tk
import conversiones
import tablas

def redirigir():
    if radio_state.get() == 1:
        ventana_tablas()
    else:
        ventana_conversiones()

def ventana_conversiones():
    window.destroy()
    conversiones.mostrar_conversiones()

def ventana_tablas():
    window.destroy()
    tablas.mostrar_tablas()

def radio_used():
    print(radio_state.get())

def mostrar_main():

    global window
    global radio_state


    window = tk.Tk()
    window.title("Matematicas discretas")

    window.minsize(width=500, height=300)

    label_titulo = tk.Label(window, text="Matematicas discretas", font=("Arial", 24, "bold"))

    label_titulo.pack()

    label_opcion = tk.Label(window, text="Seleccione una opcion", font=("Arial", 12, "bold"))

    label_opcion.pack()

    # Radiobutton
    radio_state = tk.IntVar()

    radiobutton1 = tk.Radiobutton(window, text="Tablas de verdad", value=1, variable=radio_state, command=radio_used)

    radiobutton2 = tk.Radiobutton(window, text="Conversiones", value=2, variable=radio_state, command= radio_used)

    radiobutton1.pack()

    radiobutton2.pack()

    # si se selecciona un boton mostrar algo nuevo
    button = tk.Button(window, text="Seleccionar", command=redirigir)
    button.pack()

    button_salir = tk.Button(window, text="Salir", command=window.quit)
    button_salir.pack()
    window.mainloop()