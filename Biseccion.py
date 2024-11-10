import tkinter as tk
from tkinter import ttk
import math

def centrar_ventana(ventana, ancho, alto):
    # Obtener el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    # Calcular la posición x y y
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    
    # Establecer la geometría de la ventana
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')


def biseccion(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return None, None, []
    
    iteraciones = []
    a_n = a
    b_n = b
    m_n = (a_n + b_n) / 2.0
    error = abs(f(m_n))
    count = 0
    ErrorAlg = 0.0

    while error > tol:
        iteraciones.append((count, a_n, b_n, m_n, error, ErrorAlg))
        if f(a_n) * f(m_n) < 0:
            b_n = m_n
        else:
            a_n = m_n
        ErrorAlg = abs(((m_n - ((a_n + b_n)/2.0))/((a_n + b_n)/2.0))) #ERROR ALGORITMICO
        m_n = (a_n + b_n) / 2.0
        error = abs(f(m_n))
        count += 1

    iteraciones.append((count, a_n, b_n, m_n, error, ErrorAlg))
    return m_n, error, iteraciones

def funcion(x):
    return math.exp(x) - 3 *(x ** 2) 

def calcular():
    a = float(entry_a.get())# obtiene los datos de a
    b = float(entry_b.get())# obtiene los datos de b
    tol = float(entry_tol.get()) #obtiene los datos de tolerancia
    
    raiz, error, iteraciones = biseccion(funcion, a, b, tol) #llamada a la funcion
    output_text.delete(1.0, tk.END) #limpia el texto de la salida
    if raiz is None:
        output_text.insert(tk.END, "La función debe cambiar de signo en el intervalo [a, b].\n")
    else:
        #Recorre las iteraciones y las muestra en la interfaz.
        output_text.insert(tk.END, f"Realizando Iteraciones....\n")
        for iteracion in iteraciones:
            output_text.insert(tk.END, f" \nIteración {(iteracion[0])+1}:\n a = {iteracion[1]}\n b = {iteracion[2]}\n m = {iteracion[3]}\n Error Algoritmico = {iteracion[5]} \n error = {iteracion[4]}\n")
        output_text.insert(tk.END, f"\nRaíz aproximada: {raiz}\nError final: {error}\n")

# Configuración de la interfaz gráfica
root = tk.Tk() #[creando ventana principal]
root.title("Método de Bisección")#[Establecer el titulo de la ventana]

ancho_ventana = 430  # Ancho de la ventana
alto_ventana = 430  # Alto de la ventana
centrar_ventana(root, ancho_ventana, alto_ventana)  # Centrar la ventana

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Limite Inferior [a]:", foreground="blue").grid(row=0, column=0, sticky=tk.W)
entry_a = ttk.Entry(frame, width=15)
entry_a.grid(row=0, column=1)

ttk.Label(frame, text="Limite Superior [b]:", foreground="blue").grid(row=1, column=0, sticky=tk.W)
entry_b = ttk.Entry(frame, width=15)
entry_b.grid(row=1, column=1)

ttk.Label(frame, text="Tolerancia:", foreground="blue").grid(row=2, column=0, sticky=tk.W)
entry_tol = ttk.Entry(frame, width=15)
entry_tol.grid(row=2, column=1)


btn_calcular = tk.Button(frame, text="Calcular", command=calcular, bg="red", fg="white")
btn_calcular.grid(row=3, column=0,sticky=tk.W, columnspan=2,)


#Crear Scroollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.grid(row=4, column=2, sticky=(tk.N, tk.S))

output_text = tk.Text(frame, width=50, height=20, yscrollcommand=scrollbar.set) #Crea un área de texto para mostrar los resultados.
output_text.grid(row=4, column=0, columnspan=2)   #Posiciona el Area de texto
scrollbar.config(command=output_text.yview)

root.mainloop()