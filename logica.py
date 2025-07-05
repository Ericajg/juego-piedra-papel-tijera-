from random import choice # Importamos la función choice del módulo random

opciones = ["Piedra", "Papel", "Tijera"]
eleccion_pc = choice(opciones)    # Elección aleatoria de la PC



#-------------funcion para elegir piedra----------------
def elegir_piedra(texto_usuario, texto_pc, texto_resultado):
    texto_usuario.set("Piedra")   # actualiza el texto que se muestra
    eleccion_pc = choice(opciones)  # la compu elige al azar
    texto_pc.set(eleccion_pc)       # muestra lo que eligió la compu
    texto_resultado.set(calcular_resultado(texto_usuario.get(), eleccion_pc))
    
#-------------funcion para elegir papel----------------
def elegir_papel(texto_usuario, texto_pc, texto_resultado):
    texto_usuario.set("Papel")   
    eleccion_pc = choice(opciones) 
    texto_pc.set(eleccion_pc)
    texto_resultado.set(calcular_resultado(texto_usuario.get(), eleccion_pc))     

#-------------funcion para elegir tijera----------------
def elegir_tijera(texto_usuario, texto_pc, texto_resultado):
    texto_usuario.set("Tijera")   
    eleccion_pc = choice(opciones) 
    texto_pc.set(eleccion_pc)
    texto_resultado.set(calcular_resultado(texto_usuario.get(), eleccion_pc))
    
#-------------funcion resultado----------------
def calcular_resultado(valor_usuario, valor_pc):
    if valor_usuario == valor_pc:
        return "Empate"
    elif (valor_usuario == "Piedra" and valor_pc == "Tijera") or \
         (valor_usuario == "Papel" and valor_pc == "Piedra") or \
         (valor_usuario == "Tijera" and valor_pc == "Papel"):
        return "Ganaste"
    else:
        return "Perdiste"
