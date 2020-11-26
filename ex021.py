# Faca tocar um arquivo mp3 importando um modulo
# pygame não funcionou, a solução no comentário do youtube foi importar somente o mixer e usar input para no finalizar o programa
from pygame import mixer
mixer.init()
mixer.music.load('random_music1.mp3')
mixer.music.play()
input('Impedindo programa de finalizar...')
