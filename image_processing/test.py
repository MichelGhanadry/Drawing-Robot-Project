from Image import Image

image = Image('cow')

print(image.get_image_id())
print(image.get_image_size())

image.set_pixel(10, 20, 'black')
print(image.get_pixel(10,20))

for i, key in enumerate(colors):
    image.set_pixel_range(i*12, 50, colors[key], h=10)
    
image.show_image()