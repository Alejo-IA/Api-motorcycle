import tkinter as tk
from tkinter import messagebox
from src.ui.app import MotorcycleApp
from src.config import API_KEY

def main():
    """Función principal que inicia la aplicación"""
    # Verificar que tenemos la API key antes de iniciar
    if not API_KEY:
        messagebox.showerror(
            "Error de configuración", 
            "No se encontró la API key. Por favor crea un archivo .env con la variable API_NINJA_KEY"
        )
        return
    
    root = tk.Tk()
    app = MotorcycleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()