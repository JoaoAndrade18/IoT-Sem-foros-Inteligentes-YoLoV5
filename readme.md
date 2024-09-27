# doc simples sobre o projeto

## 1. Detecção de Objetos com YOLOv5 e OpenCV

Arquivo `main.py` é o arquivo principal do projeto. Ele faz o seguinte:

- Carregar o modelo YOLOv5 com o método `torch.hub.load`
- Carregar a imagem `t7.jpg` com o método `cv2.imread`
- Realizar a detecção de objetos com o método `model(img)`
- Obter as detecções como DataFrame com o método `results.pandas().xyxy[0]`
- Desenhar as caixas na imagem original com o método `results.render()`
- Exibir a imagem com as detecções com o método `cv2.imshow('Detect cars with YoLov5', img)`

## 2. euristica.py 

O arquivo `euristica.py` é um exemplo de código que faz a euristica de um semáforo. Ele faz o seguinte:

- Definir um dicionário `pesos` que armazena os pesos de cada modais
- Definir uma função `calcular_peso` que recebe um dicionário de modais e um dicionário de pesos e retorna o total de pesos
- Definir dois dicionários `modais_ns` e `modais_lo` que armazenam as quantidades de modais em cada direção
- Definir duas variáveis `Wns` e `Wlo` que armazenam o peso total de modais em cada direção
- Usar a função `calcular_peso` para calcular o peso total de modais em cada direção
- Usar uma condição `if` para decidir qual direção abrir o semáforo

## 3. semaforo-arduino.c++

O arquivo `semaforo-arduino.c` é um exemplo de código que controla um semáforo com um Arduino. Ele faz o seguinte:

- Definir a variável principal `data` que define quais semáforos abrir
- Definir as variaveis de pinos `semaforoNorteSul` e `semaforoLesteOeste` que armazenam o estado verde do semáforo Norte-Sul e Leste-Oeste
- Definir duas variáveis `semaforoRedNS` e `semaforoRedLO` que armazenam o estado vermelho do semáforo Norte-Sul e Leste-Oeste
- Configurar os pinos de saída para os semáforos com o método `pinMode`
- Usar uma condição `if` para controlar o semáforo Norte-Sul e Leste-Oeste

## Em /prints estão os resultados em imagens sobre o projeto