import tkinter as tk
import menu
import funciones as fn



def volver():
    window.destroy()
    menu.mostrar_main()


def mostrar_tablas():
    global window
    window = tk.Tk()
    window.title("Tablas de verdad")
    window.minsize(width=500, height=300)
    label_titulo = tk.Label(window, text="Tablas de verdad", font=("Arial", 12, "bold")) 
    label_titulo.pack()

    button_volver = tk.Button(window, text="Volver", command=volver)
    button_volver.pack()

    def listbox_used(event):
        cadena = ""
        if listbox.get(listbox.curselection()) == "Negación":
            cadena = fn.negacion(cadena)
        
        if(listbox.get(listbox.curselection()) == "Conjunción"):
            cadena = fn.conjuncion(cadena)
        
        if(listbox.get(listbox.curselection()) == "Disyunción"):
            cadena = fn.disyuncion(cadena)

        if(listbox.get(listbox.curselection()) == "Condicional"):
            cadena = fn.condicional(cadena)

        if(listbox.get(listbox.curselection()) == "Bicondicional"):
            cadena = fn.bicondicional(cadena)

        if(listbox.get(listbox.curselection()) == "Disyunción exclusiva"):
            cadena = fn.disyuncion_exclusiva(cadena)


        label_tabla.config(text=cadena)
        # print(listbox.get(listbox.curselection()))

    listbox = tk.Listbox(height=6)

    tablas = ["Negación", "Conjunción", "Disyunción", "Condicional", "Bicondicional", "Disyunción exclusiva"]

    for tabla in tablas:

        listbox.insert(tablas.index(tabla), tabla)

    listbox.bind("<<ListboxSelect>>", listbox_used)
    
    listbox.pack()

    label_tabla = tk.Label(window, text="", font=("Arial", 12, "bold"))
    label_tabla.pack()







    window.mainloop()