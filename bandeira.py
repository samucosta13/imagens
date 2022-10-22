from PIL import Image

BRANCO = (255,255,255)
def tricolor_vertical(comprimento, altura):
    bandeira = Image.new("RGB", (comprimento,altura), BRANCO)
    cor = [BRANCO, BRANCO, BRANCO]
    print("Primeira cor: ")
    cor[0] = [int(c) for c in input().split()]
    print("Segunda cor:")
    cor[1] = [int(c) for c in input().split()]
    print("Terceira cor:")
    cor[2] = [int(c) for c in input().split()]
    for i in range(comprimento):
        if i < comprimento/3:
            j = 0
            while j < altura:
                bandeira.putpixel((i,j),(cor[0][0],cor[0][1],cor[0][2]))
                j += 1
        if i >= comprimento/3 and i < (2*comprimento/3):
            j = 0
            while j < altura:
                bandeira.putpixel((i,j),(cor[1][0],cor[1][1],cor[1][2]))
                j += 1
        if i >= (2*comprimento/3) and i < comprimento:
            j = 0
            while j < altura:
                bandeira.putpixel((i,j),(cor[2][0],cor[2][1],cor[2][2]))
                j += 1
    bandeira.show()

def tricolor_horizontal(comprimento, altura):
    bandeira = Image.new("RGB", (comprimento,altura), BRANCO)
    cor = [BRANCO, BRANCO, BRANCO]
    print("Primeira cor: ")
    cor[0] = [int(c) for c in input().split()]
    print("Segunda cor:")
    cor[1] = [int(c) for c in input().split()]
    print("Terceira cor:")
    cor[2] = [int(c) for c in input().split()]
    for j in range(altura):
        if j < altura/3:
            i = 0
            while i < comprimento:
                bandeira.putpixel((i,j),(cor[0][0],cor[0][1],cor[0][2]))
                i += 1
        if j >= altura/3 and j < (2*altura/3):
            i = 0
            while i < comprimento:
                bandeira.putpixel((i,j),(cor[1][0],cor[1][1],cor[1][2]))
                i += 1
        if j >= (2*altura/3) and j < altura:
            i = 0
            while i < comprimento:
                bandeira.putpixel((i,j),(cor[2][0],cor[2][1],cor[2][2]))
                i += 1
    bandeira.show()

print("BANDEIRAS: 1 - Faixas verticais, 2 - Faixas horizontais")
tipo = int(input("Digite: "))

a = int(input("Digite o comprimento: "))
b = int(input("Digite a altura: "))

if tipo == 1:
    tricolor_vertical(a,b)
elif tipo == 2:
    tricolor_horizontal(a,b)