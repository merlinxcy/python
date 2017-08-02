from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#
def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#
width=300
height=300
image=Image.new('RGB',(width,height),(255,255,255))
draw=ImageDraw.Draw(image)
font=ImageFont.truetype('arial.ttf',100)
#for i in range(100,150):
#    draw.point((i,i),fill=(100,100,100))
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
for t in range(4):
    draw.text((1+t*80,random.randint(0,height-10)),rndChar(),fill=rndColor2(),font=font)
#draw.text((200,1),rndChar(),fill=rndColor2(),font=font)
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
