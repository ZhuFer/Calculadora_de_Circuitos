def calcular_paralelo(r_list, i, j, fuente_val, parametro_buscado):
    # 'i-1' porque el usuario pone 'Resistencia 1' pero en Python la posición es 0
    # 'j' porque en Python el recorte [start:end] no incluye el último
    r_seleccionadas = r_list[i-1 : j]
    # 1. Resistencia Equivalente: Suma de los inversos (1 / (1/R1 + 1/R2 ...))
    if 0 in r_seleccionadas:
        req = 0 # Si hay un cable sin resistencia (corto), Req es 0
    else:
        req = 1 / sum(1/r for r in r_list)
        
    v_total = 0
    i_total = 0
    
    # 2. Ley de Ohm para el circuito completo
    if parametro_buscado == "Corriente Total":
        v_total = fuente_val
        i_total = v_total / req if req > 0 else 0
        
    elif parametro_buscado == "Voltaje Total":
        i_total = fuente_val
        v_total = i_total * req
        
    # 3. Datos Individuales
    # El voltaje es el mismo para todos, la corriente se divide por ramas (I_i = V_total / R_i)
    v_individuales = [v_total] * 4
    i_individuales = [v_total / r if r > 0 else 0 for r in r_list]
    
    return {
        "req": req,
        "v_total": v_total,
        "i_total": i_total,
        "v_ind": v_individuales,
        "i_ind": i_individuales
    }