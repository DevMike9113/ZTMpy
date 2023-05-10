from PIL import Image

img = Image.open('./sect17:Scripting/image-playground/astro.jpg')

print(img.size)

# res = img.resize((400, 400))
img.thumbnail((400, 400))  # doesnt squish image
print(img.size)
res = img
res.save("resizedAstro.jpg")
res.show()
