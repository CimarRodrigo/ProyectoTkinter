import tkinter as tk
import numpy as np
import menu_principal as principal

def redirigir():
    global dimension
    dimension = int(entry_dimension.get())
    ventana_matriz(dimension)

def ventana_matriz(dimension):
    global matriz_entries1, matriz_entries2, result_entries, result_label

    for widget in window.winfo_children():
        widget.destroy()

    matriz_entries1 = []
    matriz_entries2 = []

    frame_matrices = tk.Frame(window)
    frame_matrices.pack(pady=10)

    label_matriz1 = tk.Label(frame_matrices, text="Matriz 1:")
    label_matriz1.grid(row=0, column=0, columnspan=dimension, pady=(10, 0))

    for i in range(dimension):
        row_entries1 = []
        for j in range(dimension):
            entry = tk.Entry(frame_matrices, width=5)
            entry.grid(row=i+1, column=j, padx=5, pady=5)
            row_entries1.append(entry)
        matriz_entries1.append(row_entries1)

    label_matriz2 = tk.Label(frame_matrices, text="Matriz 2 (solo para suma, resta y multiplicación):")
    label_matriz2.grid(row=0, column=dimension+1, columnspan=dimension, pady=(10, 0))

    for i in range(dimension):
        row_entries2 = []
        for j in range(dimension):
            entry = tk.Entry(frame_matrices, width=5)
            entry.grid(row=i+1, column=j+dimension+1, padx=5, pady=5)
            row_entries2.append(entry)
        matriz_entries2.append(row_entries2)

    frame_botones = tk.Frame(window)
    frame_botones.pack(pady=10)

    button_suma = tk.Button(frame_botones, text="Suma de matrices", command=suma_matrices)
    button_suma.grid(row=0, column=0, padx=5, pady=5)

    button_resta = tk.Button(frame_botones, text="Resta de matrices", command=resta_matrices)
    button_resta.grid(row=0, column=1, padx=5, pady=5)

    button_mult = tk.Button(frame_botones, text="Multiplicación de matrices", command=multiplicacion_matrices)
    button_mult.grid(row=0, column=2, padx=5, pady=5)

    button_det = tk.Button(frame_botones, text="Determinante de la matriz 1", command=determinante_matriz)
    button_det.grid(row=1, column=0, padx=5, pady=5)

    button_trans = tk.Button(frame_botones, text="Transpuesta de la matriz 1", command=transpuesta_matriz)
    button_trans.grid(row=1, column=1, padx=5, pady=5)

    button_inv = tk.Button(frame_botones, text="Inversa de la matriz 1", command=inversa_matriz)
    button_inv.grid(row=1, column=2, padx=5, pady=5)

    result_label = tk.Label(window, text="Resultado:")
    result_label.pack(pady=(20, 10))

    frame_resultado = tk.Frame(window)
    frame_resultado.pack(pady=(10, 0))

    result_entries = []
    for i in range(dimension):
        row_entries = []
        for j in range(dimension):
            entry = tk.Entry(frame_resultado, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row_entries.append(entry)
        result_entries.append(row_entries)

def get_matrix(entries):
    try:
        matrix = np.array([[float(entry.get()) for entry in row] for row in entries])
        return matrix
    except ValueError:
        result_label.config(text="Por favor, asegúrese de que todos los campos estén llenos con números válidos.")
        return None

def set_matrix(matrix, entries):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(matrix[i][j]))

def suma_matrices():
    matriz1 = get_matrix(matriz_entries1)
    matriz2 = get_matrix(matriz_entries2)
    if matriz1 is not None and matriz2 is not None:
        resultado = np.add(matriz1, matriz2)
        set_matrix(resultado, result_entries)

def resta_matrices():
    matriz1 = get_matrix(matriz_entries1)
    matriz2 = get_matrix(matriz_entries2)
    if matriz1 is not None and matriz2 is not None:
        resultado = np.subtract(matriz1, matriz2)
        set_matrix(resultado, result_entries)

def multiplicacion_matrices():
    matriz1 = get_matrix(matriz_entries1)
    matriz2 = get_matrix(matriz_entries2)
    if matriz1 is not None and matriz2 is not None:
        resultado = np.dot(matriz1, matriz2)
        set_matrix(resultado, result_entries)

def determinante_matriz():
    matriz1 = get_matrix(matriz_entries1)
    if matriz1 is not None:
        resultado = np.linalg.det(matriz1)
        result_label.config(text=f"Determinante: {resultado:.2f}")

def transpuesta_matriz():
    matriz1 = get_matrix(matriz_entries1)
    if matriz1 is not None:
        resultado = np.transpose(matriz1)
        set_matrix(resultado, result_entries)

def inversa_matriz():
    matriz1 = get_matrix(matriz_entries1)
    if matriz1 is not None:
        try:
            resultado = np.linalg.inv(matriz1)
            set_matrix(resultado, result_entries)
        except np.linalg.LinAlgError:
            result_label.config(text="La matriz no es invertible.")

def mostrar_menu_lineal():
    global window, entry_dimension

    window = tk.Tk()
    window.title("Algebra lineal")
    window.minsize(width=800, height=600)

    label_titulo = tk.Label(window, text="Algebra lineal", font=("Arial", 24, "bold"))
    label_titulo.pack(pady=(10, 20))

    label_opcion = tk.Label(window, text="Ingrese la dimensión de la matriz:", font=("Arial", 12, "bold"))
    label_opcion.pack(pady=(10, 5))

    entry_dimension = tk.Entry(window, width=5)
    entry_dimension.pack(pady=(0, 10))

    button_dimension = tk.Button(window, text="Seleccionar", command=redirigir)
    button_dimension.pack(pady=(5, 10))

    button_salir = tk.Button(window, text="Volver", command=volver_menu)
    button_salir.pack(pady=(10, 20))

    window.mainloop()

def volver_menu():
    window.destroy()
    principal.mostrar_menu_principal()