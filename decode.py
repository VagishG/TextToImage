  import base64
from PIL import Image

file_photo='output.png'
file_output='tt.txt'

def toStr(binary):
#   this needs to be done


def imgToBinary(a):
    img=Image.open(a)
    color=img.load()
    binary=""
    for i in range(0,144):
        for j in range(0,256):
            # print(color[j,i])
            if color[j,i]==(0,0,0):
                binary+="0"
            elif color[j,i]==(255,255,255):
                binary+="1"
            else:
                return binary
                break

binary=imgToBinary(file_photo)
# print(binary)
toStr(binary)
