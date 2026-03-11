# Importamos la librería. Le ponemos el apodo "ctk" para no escribir 
# "customtkinter" completo cada vez que queramos usar algo.
import customtkinter as ctk
# --- IMPORTAMOS NUESTRA LÓGICA MATEMÁTICA ---
from logic.serie import calcular_serie
from logic.paralelo import calcular_paralelo
from logic.format import formato_ingenieria

# --- CONFIGURACIÓN GLOBAL DE LA INTERFAZ ---
# Obligamos a la ventana a usar el modo oscuro (muy profesional).
ctk.set_appearance_mode("Dark")  
# Elegimos el color base para los botones y elementos interactivos.
ctk.set_default_color_theme("blue")  

# Creamos nuestra clase principal que hereda de ctk.CTk 
# (Esto significa que nuestra clase ES una ventana de CustomTkinter).
class CalculadoraCircuitos(ctk.CTk):
    
    # El método __init__ es el "constructor". Es lo primero que se ejecuta
    # automáticamente cuando creamos la ventana.
    def __init__(self):
        # super().__init__() llama al constructor de la ventana original de ctk
        # para prepararla antes de que le pongamos nuestros botones.
        super().__init__()

        # 1. Ajustes básicos de la ventana (self representa a esta misma ventana)
        self.title("Calculadora de Circuitos (4 Resistores)")
        self.geometry("600x550") # Ancho x Alto en píxeles
        self.resizable(False, False) # Evitamos que el usuario cambie el tamaño

        # 2. Título principal de la aplicación
        # ctk.CTkLabel es una simple etiqueta de texto no editable.
        self.lbl_titulo = ctk.CTkLabel(self, text="Análisis de Circuitos", font=ctk.CTkFont(size=24, weight="bold"))
        # .pack() es el organizador. "Empaqueta" el elemento en la ventana, 
        # poniéndolo hasta arriba y centrado. 'pady' le da un margen (arriba, abajo).
        self.lbl_titulo.pack(pady=(20, 10))

        # --- SECCIÓN 1: SELECCIÓN DE CIRCUITO ---
        # Un Frame es como una "caja invisible" que nos ayuda a agrupar otros elementos.
        self.frame_tipo = ctk.CTkFrame(self)
        self.frame_tipo.pack(pady=10, padx=20, fill="x") # fill="x" hace que ocupe todo el ancho
        
        self.lbl_tipo = ctk.CTkLabel(self.frame_tipo, text="1. Tipo de Circuito:", font=ctk.CTkFont(weight="bold"))
        self.lbl_tipo.pack(side="left", padx=15, pady=10) # side="left" lo empuja a la izquierda de la caja

        # StringVar es una variable especial de Tkinter. Si su valor cambia, 
        # la interfaz gráfica se entera inmediatamente.
        self.var_circuito = ctk.StringVar(value="Serie")
        
        # RadioButtons son botones de opción. Solo puedes elegir uno a la vez.
        # Ambos comparten la misma variable (var_circuito), por eso se desmarcan entre sí.
        self.radio_serie = ctk.CTkRadioButton(self.frame_tipo, text="Serie", variable=self.var_circuito, value="Serie")
        self.radio_serie.pack(side="left", padx=10)
        
        self.radio_paralelo = ctk.CTkRadioButton(self.frame_tipo, text="Paralelo", variable=self.var_circuito, value="Paralelo")
        self.radio_paralelo.pack(side="left", padx=10)

        # --- SECCIÓN 2: PARÁMETRO A CALCULAR ---
        self.frame_param = ctk.CTkFrame(self)
        self.frame_param.pack(pady=10, padx=20, fill="x")

        self.lbl_param = ctk.CTkLabel(self.frame_param, text="2. ¿Qué deseas calcular?", font=ctk.CTkFont(weight="bold"))
        self.lbl_param.pack(side="left", padx=15, pady=10)

        self.var_parametro = ctk.StringVar(value="Resistencia Total")
        self.opciones_parametro = ["Resistencia Total", "Voltaje Total", "Corriente Total"]
        
        # OptionMenu es una lista desplegable. Le pasamos las opciones que creamos arriba.
        self.combo_parametro = ctk.CTkOptionMenu(self.frame_param, variable=self.var_parametro, values=self.opciones_parametro)
        self.combo_parametro.pack(side="left", padx=10)

        # --- SECCIÓN 3: ENTRADA DE DATOS (CAJAS DE TEXTO) ---
        self.frame_datos = ctk.CTkFrame(self)
        self.frame_datos.pack(pady=10, padx=20, fill="x")

        self.lbl_datos = ctk.CTkLabel(self.frame_datos, text="3. Ingresa los valores conocidos:", font=ctk.CTkFont(weight="bold"))
        # Aquí usamos .grid() en lugar de .pack(). 
        # Grid nos permite organizar las cosas como en una tabla de Excel (filas y columnas).
        self.lbl_datos.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky="w") # sticky="w" lo alinea al oeste (izquierda)

        # Creamos una lista vacía para guardar las cajas de texto y leerlas después
        self.entradas_r = []
        
        # Usamos un ciclo FOR para no escribir 4 veces el mismo código.
        for i in range(4):
            lbl = ctk.CTkLabel(self.frame_datos, text=f"R{i+1} (Ω):")
            lbl.grid(row=i+1, column=0, padx=15, pady=5, sticky="e") # sticky="e" (este/derecha)
            
            # CTkEntry es la caja de texto donde el usuario escribe.
            entrada = ctk.CTkEntry(self.frame_datos, placeholder_text=f"Valor R{i+1}")
            entrada.grid(row=i+1, column=1, padx=10, pady=5)
            
            # Guardamos esta caja en nuestra lista
            self.entradas_r.append(entrada)

        # Entrada extra para la Fuente (Voltaje o Corriente)
        self.lbl_fuente = ctk.CTkLabel(self.frame_datos, text="Fuente (V o A):")
        self.lbl_fuente.grid(row=5, column=0, padx=15, pady=5, sticky="e")
        self.entrada_fuente = ctk.CTkEntry(self.frame_datos, placeholder_text="Valor de la fuente")
        self.entrada_fuente.grid(row=5, column=1, padx=10, pady=5)


        # --- SECCIÓN: RANGO DE RESISTENCIAS ---
        self.frame_rango = ctk.CTkFrame(self)
        self.frame_rango.pack(pady=10, padx=20, fill="x")

        self.lbl_rango = ctk.CTkLabel(self.frame_rango, text="4. Rango de cálculo:", font=ctk.CTkFont(weight="bold"))
        self.lbl_rango.pack(side="left", padx=15)

        self.var_ri = ctk.StringVar(value="1")
        self.combo_ri = ctk.CTkOptionMenu(self.frame_rango, variable=self.var_ri, values=["1", "2", "3", "4"], width=60)
        self.combo_ri.pack(side="left", padx=5)

        self.lbl_al = ctk.CTkLabel(self.frame_rango, text="al")
        self.lbl_al.pack(side="left")

        self.var_rj = ctk.StringVar(value="4")
        self.combo_rj = ctk.CTkOptionMenu(self.frame_rango, variable=self.var_rj, values=["1", "2", "3", "4"], width=60)
        self.combo_rj.pack(side="left", padx=5)

        # --- BOTÓN DE CÁLCULO ---
        # command=self.ejecutar_calculo le dice al botón qué función ejecutar al hacerle clic.
        # IMPORTANTE: Se pone sin paréntesis al final, para que no se ejecute solo al arrancar.
        self.btn_calcular = ctk.CTkButton(self, text="Calcular Parámetros", command=self.ejecutar_calculo, fg_color="#28a745", hover_color="#218838")
        self.btn_calcular.pack(pady=20)

        # --- SECCIÓN 4: ÁREA DE RESULTADOS ---
        self.caja_resultados = ctk.CTkTextbox(self, height=150, font=ctk.CTkFont(family="Consolas", size=14))
        self.caja_resultados.pack(pady=10, padx=20, fill="x")
        self.caja_resultados.insert("0.0", "Los resultados aparecerán aquí...")
        # La deshabilitamos para que el usuario no pueda borrar o escribir texto ahí por accidente
        self.caja_resultados.configure(state="disabled")

    # --- LÓGICA DE EVENTOS ---
    def ejecutar_calculo(self):
        """
        Recolecta los datos de la interfaz, valida que el rango Ri a Rj sea lógico
        y muestra los resultados formateados en la caja de texto.
        """
        try:
            # 1. Obtener el rango de resistencias (Ri a Rj)
            # Convertimos a entero porque los OptionMenu devuelven texto "1", "2"...
            i_idx = int(self.var_ri.get())
            j_idx = int(self.var_rj.get())

            # Validación: El inicio no puede ser mayor al fin
            if i_idx > j_idx:
                self.mostrar_error("Error de Rango: Ri debe ser menor o igual a Rj.")
                return

            # 2. Recolectar valores de los Entry y convertirlos a número decimal (float)
            # Obtenemos la lista completa de las 4 cajas
            r_full = []
            for caja in self.entradas_r:
                valor = caja.get().strip()
                # Si una caja está vacía, la tratamos como 0 para no crashear
                r_full.append(float(valor) if valor else 0.0)
            
            val_fuente = float(self.entrada_fuente.get() if self.entrada_fuente.get() else 0)

            # 3. Determinar qué lógica usar (Serie o Paralelo)
            circuito_tipo = self.var_circuito.get()
            parametro = self.var_parametro.get()

            # Enviamos la lista completa y los índices. La lógica interna hará el recorte.
            if circuito_tipo == "Serie":
                res = calcular_serie(r_full, i_idx, j_idx, val_fuente, parametro)
            else:
                res = calcular_paralelo(r_full, i_idx, j_idx, val_fuente, parametro)

            # 4. Construir el reporte de resultados para la pantalla
            # Usamos nuestra función de formato_ingenieria para que se vea profesional
            txt =  f"--- RESULTADOS ({circuito_tipo.upper()}) ---\n"
            txt += f"Rango analizado: R{i_idx} hasta R{j_idx}\n"
            txt += f"Resistencia Eq:  {formato_ingenieria(res['req'], 'Ω')}\n"
            txt += f"Voltaje Total:   {formato_ingenieria(res['v_total'], 'V')}\n"
            txt += f"Corriente Total: {formato_ingenieria(res['i_total'], 'A')}\n"
            txt += "-"*35 + "\n"
            txt += "DETALLE DE LA SECCIÓN SELECCIONADA:\n"

            # Solo mostramos el detalle de las resistencias que entraron en el rango
            # res['v_ind'] y res['i_ind'] ya vienen recortados desde la lógica
            for n, (v, curr) in enumerate(zip(res['v_ind'], res['i_ind'])):
                num_r = i_idx + n
                txt += f"R{num_r}: {formato_ingenieria(v, 'V')} | {formato_ingenieria(curr, 'A')}\n"

            # 5. Imprimir en la caja de texto (Textbox)
            self.actualizar_pantalla_resultados(txt)

        except ValueError:
            self.mostrar_error("Error de Datos: Asegúrate de usar solo números y puntos decimales.")

    def actualizar_pantalla_resultados(self, mensaje):
        """Método auxiliar para escribir en la caja de texto bloqueada."""
        self.caja_resultados.configure(state="normal")
        self.caja_resultados.delete("0.0", "end")
        self.caja_resultados.insert("0.0", mensaje)
        self.caja_resultados.configure(state="disabled")

    def mostrar_error(self, mensaje_error):
        """Muestra un mensaje de error estilizado en la caja de resultados."""
        self.actualizar_pantalla_resultados(f"⚠️ {mensaje_error}")
# --- PUNTO DE ARRANQUE DEL PROGRAMA ---
# Esto evita que el código se ejecute por accidente si otro archivo lo importa.
# Solo arranca si corremos este archivo directamente.
if __name__ == "__main__":
    app = CalculadoraCircuitos() # Instanciamos nuestra ventana
    app.mainloop() # Iniciamos el "bucle infinito" para que la ventana no se cierre al instante.