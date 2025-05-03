import tkinter as tk
from utils import actualizar_hora
from funciones import abrir_contactos, abrir_llamadas, abrir_ajustes, abrir_apps

# Crear ventana principal
root = tk.Tk()
root.title("Interfaz Tipo Celular")
root.geometry("300x550")
root.configure(bg="skyblue")

# Reloj y barra superior
barra_superior = tk.Frame(root, bg="navy", height=50)
barra_superior.pack(fill="x")

reloj = tk.Label(barra_superior, text="", font=("Arial", 16), bg="navy", fg="white")
reloj.pack(side="left", padx=10)
actualizar_hora(root, reloj)

# Área de botones
espacio = tk.Frame(root, bg="skyblue")
espacio.pack(expand=True)

btn_contactos = tk.Button(espacio, text="📞 Contactos", command=lambda: abrir_contactos(root), width=20,
                          bg="lightgreen", fg="black", font=("Arial", 12))
btn_contactos.pack(pady=10)

btn_llamadas = tk.Button(espacio, text="📱 Llamadas", command=lambda: abrir_llamadas(root), width=20,
                         bg="lightblue", fg="black", font=("Arial", 12))
btn_llamadas.pack(pady=10)

btn_ajustes = tk.Button(espacio, text="⚙️ Ajustes", command=lambda: abrir_ajustes(root), width=20,
                        bg="lightgray", fg="black", font=("Arial", 12))
btn_ajustes.pack(pady=10)

btn_apps = tk.Button(espacio, text="📦 Apps", command=lambda: abrir_apps(root), width=20,
                     bg="orange", fg="black", font=("Arial", 12))
btn_apps.pack(pady=10)

# Iniciar aplicación
root.mainloop()
