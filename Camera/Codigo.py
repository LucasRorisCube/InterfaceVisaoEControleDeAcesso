import cv2
import os
import time
from picamera2 import Picamera2
import RPi.GPIO as GPIO
from time import sleep

# Setup do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

can_take_picture = False # Variavel global para verificar se pode tirar foto

def button_pressed(pin): # Caso o botao for pressionado, permite tirar foto
	global can_take_picture	
	can_take_picture = True

# Define os pinos dos LEDs
led_pin_verde = 16
led_pin_vermelho = 26

# Define o pino do botao
button_pin = 12

# Setup do GPIO para os Leds e o botao
GPIO.setup(led_pin_verde, GPIO.OUT)
GPIO.setup(led_pin_vermelho, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Adiciona um evento para executar uma funcao quando o botao for pressionado
GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=button_pressed, bouncetime=200)

# Importa o classificador
face_detector = cv2.CascadeClassifier("/home/sel/haarcascade_frontalface_default.xml")

# Inicializa a Janela e a Camera
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888', "size": (640, 480)}))
picam2.start()

# Diretorio onde as fotos sao armazenadas
output_directory = "detected_faces"
os.makedirs(output_directory, exist_ok=True)

try:
	while True:

		im = picam2.capture_array() # Le a imagem
		grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # Transforma em Gray scale

		faces = face_detector.detectMultiScale(grey, 1.1, 5) # Detecta as faces

		if len(faces) == 0: # Caso nao tenha faces, liga o led vermelha
			GPIO.output(led_pin_vermelho, True)
			GPIO.output(led_pin_verde, False)
			can_take_picture = False
		else: # Caso tenha face, liga o led verde
			GPIO.output(led_pin_vermelho, False)
			GPIO.output(led_pin_verde, True)
		
		# Para cada face encontrada, desenhar um retangulo em volta
		for (x, y, w, h) in faces:

			cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0)) # Desenha o retangulo
			
			if can_take_picture: # Caso o botao estiver precionado, salvar a imagem
				print("Foto Salva")
				timestamp = int(time.time())
				filename = os.path.join(output_directory, f"face_{timestamp}.jpg")

				cv2.imwrite(filename, im[y:y+h, x:x+w])
				sleep(1)
				can_take_picture = False

		cv2.imshow("Camera", im)

		cv2.waitKey(1)
except KeyboardInterrupt as e: # Interrompe o caso
	GPIO.cleanup()
	print("Acabou")