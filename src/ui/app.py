import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from src.api.motorcycles import buscar_motos
from src.config import API_KEY, EXCEL_OUTPUT_PATH

class MotorcycleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscador de Motos")
        self.root.geometry("800x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C2F33")
        
        self.df = None
        self.setup_ui()
        
    def setup_ui(self):
        # Estilos
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#2C2F33", foreground="white", font=("Arial", 10))
        style.configure("TButton", background="#7289DA", foreground="white", font=("Arial", 10, "bold"))
        style.configure("TEntry", font=("Arial", 10))
        
        # Marco de entrada y filtros
        frame_superior = ttk.Frame(self.root, padding=10)
        frame_superior.pack(fill="x")
        
        # Campos de entrada
        ttk.Label(frame_superior, text="Marca:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_marca = ttk.Entry(frame_superior, width=15)
        self.entrada_marca.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_superior, text="Modelo:").grid(row=0, column=2, padx=5, pady=5)
        self.entrada_modelo = ttk.Entry(frame_superior, width=15)
        self.entrada_modelo.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(frame_superior, text="Año:").grid(row=0, column=4, padx=5, pady=5)
        self.entrada_anio = ttk.Entry(frame_superior, width=10)
        self.entrada_anio.grid(row=0, column=5, padx=5, pady=5)
        
        # Combobox de tipo de moto
        ttk.Label(frame_superior, text="Tipo:").grid(row=1, column=0, padx=5, pady=5)
        self.combo_tipo = ttk.Combobox(
            frame_superior, 
            values=["Todos", "Sport", "Cruiser", "Touring", "Naked", "Off-road", "Scooter"], 
            width=12, 
            state="readonly"
        )
        self.combo_tipo.grid(row=1, column=1, padx=5, pady=5)
        self.combo_tipo.current(0)
        
        # Botones
        ttk.Button(frame_superior, text="Buscar", command=self.buscar_moto).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(frame_superior, text="Limpiar", command=self.limpiar_busqueda).grid(row=1, column=3, padx=5, pady=5)
        ttk.Button(frame_superior, text="Descargar Excel", command=self.descargar_excel).grid(row=1, column=4, padx=5, pady=5)
        
        # Tabla de resultados
        columnas = ("Marca", "Modelo", "Año", "Tipo", "Cilindrada", "Potencia", "Velocidad Máx")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings", height=15)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
    
    def buscar_moto(self):
        """ Realiza la búsqueda con filtros opcionales """
        marca = self.entrada_marca.get().strip()
        modelo = self.entrada_modelo.get().strip()
        anio = self.entrada_anio.get().strip()
        tipo = self.combo_tipo.get()
        
        try:
            data = buscar_motos(marca, modelo, anio, tipo)
            
            if not data:
                messagebox.showinfo("Sin resultados", "No se encontraron motos con esos filtros.")
                return
            
            self.actualizar_tabla(data)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def actualizar_tabla(self, data):
        """ Llena la tabla con los datos obtenidos """
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        
        self.df = pd.DataFrame(data)
        
        for i, row in self.df.iterrows():
            self.tabla.insert("", "end", values=(
                row.get("make", "N/A"), row.get("model", "N/A"), row.get("year", "N/A"),
                row.get("type", "N/A"), row.get("engine", "N/A"), row.get("power", "N/A"),
                row.get("top_speed", "N/A")
            ))
    
    def descargar_excel(self):
        """ Guarda los datos en un archivo Excel """
        if self.df is not None:
            try:
                # Asegurar que el directorio existe
                os.makedirs(os.path.dirname(EXCEL_OUTPUT_PATH), exist_ok=True)
                
                self.df.to_excel(EXCEL_OUTPUT_PATH, index=False)
                messagebox.showinfo("Éxito", f"Datos guardados en '{EXCEL_OUTPUT_PATH}'.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            messagebox.showwarning("Advertencia", "No hay datos para guardar.")
    
    def limpiar_busqueda(self):
        """ Limpia todos los campos de entrada y la tabla """
        self.entrada_marca.delete(0, tk.END)
        self.entrada_modelo.delete(0, tk.END)
        self.entrada_anio.delete(0, tk.END)
        self.combo_tipo.current(0)
        for row in self.tabla.get_children():
            self.tabla.delete(row)