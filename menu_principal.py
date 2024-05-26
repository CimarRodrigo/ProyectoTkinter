import tkinter as tk
import menu_lineal as lineal
import menu

def mostrar_menu_principal():

    global window
    global radio_state

    window = tk.Tk()
    window.title("Proyecto introduccion a la programacion :v")
    
    window.configure(bg="beige")
    

    window.minsize(width=500, height=300)

    label_titulo = tk.Label(window, text="Proyecto introduccion a la programacion 😎🤓☝", font=("Comic Sans MS", 24, "bold"), bg="lightblue")

    label_titulo.pack()

    label_opcion = tk.Label(window, text="Seleccione una opcion", font=("Arial", 12, "bold"))

    label_opcion.pack()

    # Radiobutton
    radio_state = tk.IntVar()

    radiobutton1 = tk.Radiobutton(window, text="Lineal", value=1, variable=radio_state, command=radio_used)

    radiobutton2 = tk.Radiobutton(window, text="Discretas", value=2, variable=radio_state, command= radio_used)


    radiobutton1.pack()

    radiobutton2.pack()

    # si se selecciona un boton mostrar algo nuevo
    button = tk.Button(window, text="Seleccionar", command=redirigir)
    button.pack()

    button_salir = tk.Button(window, text="Salir", command=window.quit)
    button_salir.pack()
    window.mainloop()

def radio_used():

    print(radio_state.get())

def redirigir():

    if radio_state.get() == 1:
        ventana_lineal()
    elif radio_state.get() == 2:
        ventana_discretas()


def ventana_lineal():

    window.destroy()
    lineal.mostrar_menu_lineal()

def ventana_discretas():

    window.destroy()
    menu.mostrar_main()
