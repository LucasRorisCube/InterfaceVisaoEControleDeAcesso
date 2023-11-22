# InterfaceVisaoEControleDeAcesso
Prática 5: Introdução a interfaces de visão computacional, sistemas de versionamento de arquivos e controle de acesso via Tags

Nesta prática temos dois projetos: 1 - projeto de controle de acesso via Tag RFID, e 2 - projeto da câmera (modificado)

# Nome dos integrantes:

Gabriel Vinicius dos Santos (11819424)

Lucas Alves Roris (11913771)

# Projeto 1 - Controle de acesso via Tag RFID

O vídeo mostrando o funcionamento pode ser visto em  ```InterfaceVisaoEControleDeAcesso/Videos/GerenciamentoDeAcesso.mp4```

E todo código usado para este projeot se econtra em ```InterfaceVisaoEControleDeAcesso/ControleDeAcesso/Catraca.py```.

O código mencionado acima refere-se ao controle de acesso utilizando uma Raspberry Pi e programação em Python para comunicação SPI (Serial Peripheral Interface) com uma tag RFID (Radio Frequency Identification). O script utiliza a biblioteca SimpleMFRC522 para interagir com o leitor RFID. O objetivo do projeto é ler o identificador único da tag RFID e, com base nesse identificador, determinar se o acesso é autorizado ou não. A Raspberry Pi sinaliza o resultado através de LEDs verde e vermelho.

O código começa inicializando o GPIO (General Purpose Input/Output) e configurando os pinos dos LEDs. Em seguida, cria um objeto leitor da classe SimpleMFRC522 para interagir com o leitor RFID. O programa entra em um loop infinito, onde a Raspberry Pi aguarda a aproximação de uma tag RFID. Quando a tag é detectada, o código lê o identificador da tag e verifica se ele corresponde a um identificador predefinido autorizado. Se a correspondência for positiva, o LED verde é aceso, indicando acesso autorizado; caso contrário, o LED vermelho é aceso, indicando acesso não autorizado.

Por im, tomemos que a sinalização da liberação do controle de acesso via Tag foi um sucesso, mostrando um exmeplo prático de uso muito comum de sistemas embarcados, como vemos por exemplo, no bandeijão da USP.

# Projeto 2 - Câmera (modificado)

O vídeo mostrando o funcionamento do projeto pode ser visto em ```InterfaceVisaoEControleDeAcesso/Videos/ReconhecimentoFacial.mp4```

e todo código usado para este projeot se econtra em ```https://github.com/LucasRorisCube/InterfaceVisaoEControleDeAcesso/blob/main/Camera/Codigo.py```.

O código mencionado acima é um projeto de reconhecimento facial usando uma Raspberry Pi e a linguagem de programação Python, juntamente com a biblioteca OpenCV para processamento de imagem e a biblioteca picamera2 para interação com a câmera. O projeto utiliza um botão físico conectado à Raspberry Pi para acionar a captura de uma foto somente quando um rosto é detectado na imagem da câmera. LEDs vermelho e verde são utilizados para indicar se um rosto foi detectado ou não, respectivamente.

O script começa configurando o GPIO (General Purpose Input/Output) para controlar os LEDs e monitorar o estado do botão. O programa utiliza um classificador de cascata Haar para detectar faces na imagem capturada pela câmera. Quando um rosto é detectado, o LED verde é aceso, indicando que a câmera está pronta para tirar uma foto. Se nenhum rosto for detectado, o LED vermelho é aceso. A variável can_take_picture é utilizada para controlar se o botão foi pressionado, permitindo assim a captura da foto.

Dentro do loop principal, o código verifica continuamente a presença de faces na imagem. Se uma face é detectada e o botão foi pressionado, uma foto é capturada, salva em um diretório específico com um nome de arquivo único baseado no timestamp e o LED verde é desligado. O código lida adequadamente com uma interrupção do teclado (KeyboardInterrupt) para realizar uma limpeza apropriada do GPIO.

Em resumo, o proejto para tirar abertar o botão para tirar foto apenas quando o algoritmo reconhece um rosto foi um sucesso!

No final, imagem como a abaixo podem ser obtidas neste proejto:

![alt text](https://github.com/LucasRorisCube/InterfaceVisaoEControleDeAcesso/blob/main/Camera/detected_faces/face_1697658771.jpg)
