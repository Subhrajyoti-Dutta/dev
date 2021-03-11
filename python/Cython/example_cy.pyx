import PIL.Image as Image

def color(x,y):
    cpdef complex C0 = x+y*1j
    cpdef complex C = 0+0j
    cdef int i = 0
    while i < 255 and abs(C) <= 2:
        C = C**2 + C0
        i += 1
    if i == 255: return (0,0,0)
    else: return (i % 4 * 64, i % 8 * 32, i % 16 * 16)


def mandelbrot(int height = 1000, int width = 1000):
    img = Image.new("RGB",(height,width))

    pixel = img.load()

    cdef int dx = 3
    cdef int dy = dx

    print(dx/dy)
    x0,x1 = -2,1
    y0,y1 = 1.5,-1.5

    cdef int j
    cdef int i
    for j in range(0,height):
        for i in range(0,width):
            pixel[i,j] = color(x0 + dx * i/width,y0 - dy *j/height)

    img.show()