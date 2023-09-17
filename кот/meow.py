from PIL import Image, ImageFilter

with Image.open("images.jpg") as pic_original:
    print("Зображення відкрито")
    print("Розмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)
    pic_original.show()

    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    print("Зображення створене")
    print("Розмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jpg")
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("up.jpg")
    pic_up.show()