from PIL import Image

i1 = Image.open("A.png")
i2 = Image.open("B.png")
img = Image.new('RGB', i1.size)

p1 = i1.load()
p2 = i2.load()
pnew = img.load()

for i in range(i1.size[0]):
    for j in range(i1.size[1]):
        if p1[i,j] != p2[i,j]:
            pnew[i,j] = (255,255,255)

img.show()
