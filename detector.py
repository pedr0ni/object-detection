import numpy as np
import cv2

obj = input("Digite o objeto que você quer detectar: \ncarro,pessoa\n")

cascade = 0

olhos = 0
ds = 0
corpo = 0

if (obj == "carro"):
    #Detectar carros
    cascade = cv2.CascadeClassifier('carro/cascade.xml')
    print("Procurando por",obj)
elif (obj == "pessoa"):
    #Detectar pessoa
    ask = input("Você deseja procurar por olhos também? (s-n)\n")
    if (ask == "s"):
        olhos = 1
    ask = input("Você deseja procurar por sorrisos? (s-n)\n")
    if (ask == "s"):
        ds = 1
    ask = input("Você deseja procurar por corpo completo? (s-n)\n")
    if (ask == "s"):
        corpo = 1
    cascade = cv2.CascadeClassifier('pessoa/cascade.xml')
    print("Procurando por",obj)
else:
    print("Objeto não identificado.")
    exit()

img = input("Digite o nome da imagem:\n")

img = cv2.imread(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

objetos = cascade.detectMultiScale(gray, 1.3, 5)
resultado = 0

eye = cv2.CascadeClassifier('pessoa/olhos.xml')
smile = cv2.CascadeClassifier('pessoa/sorriso.xml')
body = cv2.CascadeClassifier('pessoa/corpo.xml')

for (x,y,w,h) in objetos:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    resultado = resultado + 1
    if (olhos == 1):
        eyes = eye.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    if (ds == 1):
        sorrisos = smile.detectMultiScale(roi_gray)
        for (sx,sy,sw,sh) in sorrisos:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

print("Foram encontrados",resultado,obj)

cv2.imshow('Resultados',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
