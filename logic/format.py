import math

def formato_ingenieria(valor, unidad=""):
    """
    Toma un número decimal y lo convierte a notación de ingeniería (k, M, m, µ, etc.)
    Ejemplo: 0.005, "A" -> "5.00 mA"
    """
    if valor == 0:
        return f"0.00 {unidad}"
    
    # Truco matemático: Usamos logaritmos para saber cuántos ceros tiene el número
    # y lo redondeamos al múltiplo de 3 más cercano (porque la ingeniería va de 10^3 en 10^3).
    exponente = int(math.floor(math.log10(abs(valor)) / 3.0) * 3)
    
    # Recorremos el punto decimal
    valor_formateado = valor / (10 ** exponente)
    
    # Diccionario con nuestros prefijos
    prefijos = {
        -12: "p",   # pico
        -9: "n",    # nano
        -6: "µ",    # micro
        -3: "m",    # mili
        0: "",      # unidad base
        3: "k",     # kilo
        6: "M",     # mega
        9: "G"      # giga
    }
    
    # Buscamos la letra correspondiente. Si el número es absurdamente grande o pequeño, dejamos la notación científica "e".
    prefijo = prefijos.get(exponente, f"e{exponente}")
    
    return f"{valor_formateado:.2f} {prefijo}{unidad}"