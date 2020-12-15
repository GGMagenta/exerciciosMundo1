# Ver se o site pudim está acessível
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[0;31mNão foi possivel acessar o site pudim')
else:
    print('\033[0;32mConsegui acessar o site pudim')
