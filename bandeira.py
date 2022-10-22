from PIL import Image
BRANCO = (255,255,255)
def tricolor_horizontal(comprimento, altura):
    bandeira = Image.new("RGB", (comprimento,altura), BRANCO)
    cor = [BRANCO, BRANCO, BRANCO]
    cor[0] = [int(c) for c in input().split()]
    cor[1] = [int(c) for c in input().split()]
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
tricolor_horizontal(360,240)