def calcular_serie(r_list, i, j, fuente_val, parametro_buscado):
    # 'i-1' porque el usuario pone 'Resistencia 1' pero en Python la posición es 0
    # 'j' porque en Python el recorte [start:end] no incluye el último
    r_seleccionadas = r_list[i-1 : j]
    # 1. Resistencia Equivalente: En serie, ¡solo se suman!
    1
    req = sum(r_seleccionadas)
    
    v_total = 0
    i_total = 0
    
    # 2. Descubrir qué nos falta usando la Ley de Ohm
    if parametro_buscado == "Corriente Total":
        # Si queremos corriente, la fuente que nos dieron fue de Voltaje (I = V / R)
        v_total = fuente_val
        i_total = v_total / req if req > 0 else 0
        
    elif parametro_buscado == "Voltaje Total":
        # Si queremos voltaje, la fuente que nos dieron fue de Corriente (V = I * R)
        i_total = fuente_val
        v_total = i_total * req
        
    # 3. Datos Individuales de los 4 resistores
    # La corriente es la misma para los 4, pero el voltaje se divide (V_i = I_total * R_i)
    v_individuales = [i_total * r for r in r_list]
    i_individuales = [i_total] * 4 
    
    # Devolvemos un "diccionario" empaquetando todos los resultados
    return {
        "req": req,
        "v_total": v_total,
        "i_total": i_total,
        "v_ind": v_individuales,
        "i_ind": i_individuales
    }