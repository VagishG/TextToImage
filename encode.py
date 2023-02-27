import base64
from PIL import Image

file_path='f.txt'
def fill(x, y, color):

    img.putpixel((x, y), color)
def toBinary(a):
    with open(a) as f:
        contents = f.read()
        print(contents)
    t=contents.encode(("ascii"))
    binary="".join(["{:08b}".format(x) for x in t])
    return binary
img = Image.new('RGB', (256,144), color='blue')
binary=toBinary(file_path)
x=0
y=0
for char in binary:
    if char == '1':
        fill(x, y, (255, 255, 255))
    else:
        fill(x, y, (0, 0, 0))
    x += 1
    if x >= 256:
        x = 0
        y += 1

# Save and show image
img.save('output.png')
img.show()

