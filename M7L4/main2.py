""""Crea un diccionario que admita varios niveles de dificultad.
Primero, haz que el usuario seleccione el nivel, luego selecciona aleatoriamente una palabra de la lista asociada con esta dificultad.
Grabar voz → transcribir → traducir → comparar.
Lleva un registro de la puntuación y los errores.
Una vez que el jugador cometa 3 errores, el juego debe terminar.
¡Para asegurar una comparación precisa, convierte todo a minúsculas!"""
import speech_recognition as sr
import random   
import time
# Diccionario con niveles de dificultad
palabras = {
    "fácil": {
        "gato": "cat",
        "perro": "dog", 
        "casa": "house"
    },
    "medio": {
        "árbol": "tree",
        "libro": "book",
        "coche": "car"
    },
    "difícil": {
        "sol": "sun",
        "luna": "moon",
        "agua": "water",    
        "fuego": "fire"
    }
}
# Función para seleccionar una palabra aleatoria según el nivel de dificultad
def seleccionar_palabra(nivel):
    palabra_espanol = random.choice(list(palabras[nivel].keys())) 
    traduccion_ingles = palabras[nivel][palabra_espanol] 
    return palabra_espanol, traduccion_ingles
# Función para grabar la voz del jugador
def grabar_voz():
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Pronuncia la traducción en inglés:") 
        audio = r.listen(source) 
    try:
        texto = r.recognize_google(audio, language="en-US") 
        return texto.lower() 
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
        return None
    except sr.RequestError as e:
        print(f"Error al solicitar resultados; {e}")
        return None
# Función principal del juego
def jugar():
    print("Selecciona el nivel de dificultad: fácil, medio, difícil")
    nivel = input().lower()
    if nivel not in palabras:
        print("Nivel no válido. Selecciona entre fácil, medio o difícil.")
        return
    palabra_espanol, traduccion_ingles = seleccionar_palabra(nivel) 
    print(f"Traduce la palabra: {palabra_espanol}") 
    time.sleep(2)  
    errores = 0
    while errores < 3:
        respuesta = grabar_voz() 
        if respuesta:
            if respuesta == traduccion_ingles:
                print("¡Correcto!")
                return
            else:
                errores += 1
                print(f"Incorrecto. La traducción correcta es: {traduccion_ingles}")
                print(f"Errores: {errores}/3")
        else:
            print("No se pudo obtener una respuesta válida.")
    print("Has cometido 3 errores. ¡Juego terminado!")
if __name__ == "__main__":
    jugar()