from PIL import Image

img = Image.open("img/landscape.png")
basewidth = 1000
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save("img/landscape_downsampled.png")