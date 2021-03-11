import PIL.Image as Image

def color(x,y):
    C0 = x+y*1j
    C = 0+0j
    i = 0
    while i < 255 and abs(C) <= 2:
        C = C**2 + C0
        i += 1
    if i == 255: return (0,0,0)
    else: return (i % 4 * 64, i % 8 * 32, i % 16 * 16)


height = width = 1000
img = Image.new("RGB",(height,width))

pixel = img.load()

dx = dy = 3
x0,x1 = -2,1
y0,y1 = 1.5,-1.5

for j in range(0,height):
    for i in range(0,width):
        pixel[i,j] = color(x0 + dx * i/width,y0 - dy *j/height)

img.show()