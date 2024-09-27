import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('./images/t7.jpg') 

results = model(img)

df = results.pandas().xyxy[0]  # Obter as detecções como DataFrame
print(df)

modais_presentes = df['name'].unique().tolist()
print("Modais presentes na imagem:", modais_presentes)

results.render()  # Desenha as caixas na imagem original

# Exibir a imagem com as detecções
cv2.imshow('Detect cars with YoLov5', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
