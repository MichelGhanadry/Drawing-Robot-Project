from Image import Image

image = Image('cow')

print(image.get_image_id())
print(image.get_image_size())

image.set_pixel(10, 20, [0,0,0])
print(image.get_pixel(10,20))

image.show_image()