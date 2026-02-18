"""El jugador vea una palabra en español; El jugador debe pronunciar la traducción en ingles; La aplicación grabe la voz, reconozca el habla y compare el resultado con la traducción. Si el jugador acierta, se muestra un mensaje de felicitación; Si el jugador falla, se muestra la traducción correcta. """
import speech_recognition as sr
import random  
import time
# Lista de palabras en español e inglés
palabras = {
    "gato": "cat",
    "perro": "dog", 
    "casa": "house",
    "árbol": "tree",
    "libro": "book",
    "coche": "car",
    "sol": "sun",
    "luna": "moon",
    "agua": "water",    
    "fuego": "fire"
}   
# Función para seleccionar una palabra aleatoria
def seleccionar_palabra(): 
    palabra_espanol = random.choice(list(palabras.keys())) 
    traduccion_ingles = palabras[palabra_espanol] 
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
    palabra_espanol, traduccion_ingles = seleccionar_palabra() 
    print(f"Traduce la palabra: {palabra_espanol}") 
    time.sleep(2)  
    respuesta = grabar_voz() 
    if respuesta:
        if respuesta == traduccion_ingles:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La traducción correcta es: {traduccion_ingles}")
    else:
        print("No se pudo obtener una respuesta válida.")
if __name__ == "__main__":
    jugar()