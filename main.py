import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from Marcador import Marcador

marcador = Marcador("Enemy Crushers", "Orangutanes")

img = PIL.Image.new('RGBA', (800, 400), (255, 0, 0, 0))
font = PIL.ImageFont.truetype("AbyssinicaSIL-R.ttf", 32)

d = PIL.ImageDraw.Draw(img)
d.text((180, 20), marcador.teamios[0]+ ' ' + str(marcador.teamios[1]) + '-' +
       str(marcador.teamandroid[1]) + ' ' + marcador.teamandroid[0],
       fill=(255, 255, 255), font=font)


img.save('/tmp/img.png', 'PNG')