from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

# Desabilitar os avisos
GPIO.setwarnings(False)

# Define os pinos dos LEDs
led_pin_verde = 16
led_pin_vermelho = 26

# Inicializa as configurações do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin_verde, GPIO.OUT)
GPIO.setup(led_pin_vermelho, GPIO.OUT)

# Cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para leitura.")

while True:
	id,texto = leitor.read() # Le um numero do FRID mais proximo
	# Verifica se esta autorizado ou nao
	if (str(id) == "712936067078"): # Caso sim, liga a led verde
		print("Autorizado")
		GPIO.output(led_pin_verde, True)
		GPIO.output(led_pin_vermelho, False)
	else: # Caso nao, liga a led vermelha
		print("Nao Autorizado")
		GPIO.output(led_pin_verde, False)
		GPIO.output(led_pin_vermelho, True)
	sleep(1) # Aguarda para a proxima leitura