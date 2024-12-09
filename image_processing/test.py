from Image import Image
from colors import colors

image = Image('apple')

# #################### Basics ####################
# print(image.get_image_id())
# print(image.get_image_size())

# image.set_pixel(10, 20, 'black')
# print(image.get_pixel(10,20))

# #################### Colors ####################
# for i, color in enumerate(colors):
#     image.set_pixel_range(i*12, 50, color, h=10)

# #################### Edges ####################
edges = image.edges()
sample_size = 10
points = edges.get_representative_points(sample_size, to_color=False)

# #################### Path #####################
path = edges.find_path(points, sample_size)
print(f'before path minimize we had {len(path)} pathes of lengths: {[len(s) for s in path]}')
edges.show_path(path, h=sample_size)

# ################ Minimize Path ################
# edges.minimize_path(path, 2)
# print(f'after path minimize we have {len(path)} pathes of lengths: {[len(s) for s in path]}')
# edges.show_path(path, h=sample_size)

# ################ Connect Path #################
edges.connect_path(path)
edges.show_image()
