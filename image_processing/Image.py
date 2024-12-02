import cv2 as imm
from colors import colors

images_folder = rf"C:\Users\mghanadr\OneDrive - Intel Corporation\Desktop\SUF STUF\Drawing Robot Project\Drawing-Robot-Project\image_processing\images"

class Image():
    def __init__(self, image_name, image_type="jpg", data=None, folder=None):
        self.image_name = image_name
        self.image_type = image_type
        
        if folder is not None:
            self.image_path = fr"{images_folder}\{folder}\{self.image_name}.{self.image_type}"
        else:
            self.image_path = fr"{images_folder}\{self.image_name}.{self.image_type}"
        
        if data is not None:
            self.image = data
        else:
            self.image = imm.imread(self.image_path)

        self.image_size = self.get_image_size()
        return

    def show_image(self, blocking=True):
        imm.imshow(self.get_image_id(), self.image)
        if blocking:
            imm.waitKey(0)
            imm.destroyAllWindows()
        return

########################################### Gets & Sets ###########################################
    
    def get_image_size(self):
        if self.image is None:
            rows = 0
            cols = 0
        else:
            rows = len(self.image)
            cols = len(self.image[0])
        return rows, cols

    def get_image_id(self):
        return f"{self.image_name}.{self.image_type}"

    def get_pixel(self, i=0, j=0):
        row = i if i >= 0 and i < self.image_size[0] else 0
        col = j if j >= 0 and j < self.image_size[1] else 0
        return self.image[row][col].copy()

    def set_pixel(self, i=0, j=0, color='black'):
        color_value = [0,0,0] if color not in colors else colors[color]
        if (i >= 0 and i < self.image_size[0]) and (j >= 0 and j < self.image_size[1]):
            self.image[i][j] = color_value
        return

    def set_pixel_range(self, i=0, j=0, color=[0,0,0], h=10):
        for x in range(h):
            for y in range(h):
                self.set_pixel(x+i, y+j, color)
        return
    
    def make_copy(self, new_name=None):
        name = new_name if new_name is not None else self.image_name + "_copy"
        return Image(name, self.image_type, data=self.image.copy())

    def edges(self, gaussian_blur=13, threshold1=50, threshold2=100):
        blured_image = imm.GaussianBlur(self.image, (gaussian_blur, gaussian_blur), 0)
        edges = imm.Canny(blured_image, threshold1=threshold1, threshold2=threshold2)
        new_image = self.make_copy(self.image_name + "_edges")

        for i in range(edges.shape[0]):
            for j in range(edges.shape[1]):
                if edges[i][j] == 0:
                    new_image.set_pixel(i, j, 'white') # not an edge
                else:
                    new_image.set_pixel(i, j, 'black') # edge

        return new_image