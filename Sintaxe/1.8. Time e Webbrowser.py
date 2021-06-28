'''
Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2h
Trabalho inicia de 8h as 12
'''
import webbrowser
import time


intervalos = 2
contador = 0
print('O programa de controle de descanso foi ativado ')

while contador < intervalos:
    time.sleep(10) #-> quantos segundo pra abrir a url. Depois do primeiros 10 segundos ele reestarta e como o contador chega a 2 ele para.
    webbrowser.open('https://www.youtube.com/watch?v=JRVD-pndqY0') # -> vai abrir a url
    contador = contador + 1