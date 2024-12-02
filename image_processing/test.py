from Image import Image
from colors import colors

image = Image('cow')

#################### Basics ####################
print(image.get_image_id())
print(image.get_image_size())

image.set_pixel(10, 20, 'black')
print(image.get_pixel(10,20))

#################### Colors ####################
for i, color in enumerate(colors):
    image.set_pixel_range(i*12, 50, color, h=10)

image.show_image()

edges = image.edges()
edges.show_image()
