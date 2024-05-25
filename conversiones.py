import tkinter as tk
import menu
import funciones as fn

def volver():
    window.destroy()
    menu.mostrar_main()

def convertir():
    numero = input.get()
    base_origen = seleccion.get()
    base_destino = resultado.get()

    try:
        if base_origen == "Decimal":
            numero_decimal = int(numero)
        elif base_origen == "Binario":
            numero_decimal = int(numero, 2)
        elif base_origen == "Octal":
            numero_decimal = int(numero, 8)
        elif base_origen == "Hexadecimal":
            numero_decimal = int(numero, 16)
        
        if base_destino == "Decimal":
            resultado_final = str(numero_decimal)
        elif base_destino == "Binario":
            resultado_final = bin(numero_decimal)
        elif base_destino == "Octal":
            resultado_final = oct(numero_decimal)
        elif base_destino == "Hexadecimal":
            resultado_final = hex(numero_decimal)


        if(resultado_final[:2] == '0b' or resultado_final[:2] == '0o' or resultado_final[:2] == '0x'):
            resultado_final = resultado_final[2:]

        label_resultado_conversion.config(text=f"Resultado: {resultado_final}")
    except ValueError:
        label_resultado_conversion.config(text="Entrada inválida")

def mostrar_conversiones():
    global window
    window = tk.Tk()
    window.title("Conversion")
    window.minsize(width=500, height=300)

    # Configuración de la rejilla para centrar los widgets
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    window.rowconfigure(4, weight=1)
    window.rowconfigure(5, weight=1)

    # Etiqueta de título
    label_titulo = tk.Label(window, text="Conversiones", font=("Arial", 18, "bold"))
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    # Etiqueta y entrada para el número
    label_ingrese = tk.Label(window, text="Ingrese un número", font=("Arial", 12, "bold"))
    label_ingrese.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    global input
    input = tk.Entry(window, width=10)
    input.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Etiqueta y menú desplegable para la selección de base de origen
    label_base = tk.Label(window, text="Seleccione la base de origen", font=("Arial", 12, "bold"))
    label_base.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    global seleccion
    seleccion = tk.StringVar()
    bases = ["Decimal", "Binario", "Octal", "Hexadecimal"]
    seleccion.set(bases[0])
    menu_bases = tk.OptionMenu(window, seleccion, *bases)
    menu_bases.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    
    # Etiqueta y menú para la selección de base de destino
    label_base_destino = tk.Label(window, text="Seleccione la base de destino", font=("Arial", 12, "bold"))
    label_base_destino.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    global resultado
    resultado = tk.StringVar()
    resultado.set(bases[0])
    menu_resultado = tk.OptionMenu(window, resultado, *bases)
    menu_resultado.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Botón para convertir
    button_convertir = tk.Button(window, text="Convertir", command=convertir)
    button_convertir.grid(row=4, column=0, columnspan=2, pady=10)

    # Etiqueta para mostrar el resultado
    global label_resultado_conversion
    label_resultado_conversion = tk.Label(window, text="", font=("Arial", 12, "bold"))
    label_resultado_conversion.grid(row=5, column=0, columnspan=2, pady=10)

    # Botón para volver
    button_volver = tk.Button(window, text="Volver", command=volver)
    button_volver.grid(row=6, column=0, columnspan=2, pady=10)

    window.mainloop()

# Para probar la función directamente, descomenta la línea siguiente
# mostrar_conversiones()
