from PIL import Image

img = Image.open('./sect17:Scripting/image-playground/Pokedex/pikachu.jpg')

# fil_img = img.filter(ImageFilter.SMOOTH)
fil_img = img.convert('L')
# fil_img.save('grey.png', 'png')  # PNG accepts these different actions
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))
# fil_img.show()
# crooked = fil_img.rotate(90)
# crooked.save("grey.png", 'png')
resize = fil_img.resize((300, 300))  # resize needs a tuple
resize.save("grey.png", 'png')
