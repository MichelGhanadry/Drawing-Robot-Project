import cv2 as imm

images_folder = rf"C:\Users\mghanadr\OneDrive - Intel Corporation\Desktop\SUF STUF\Drawing Robot Project\Drawing-Robot-Project\image_processing\images"

class Image():
    def __init__(self, image_name, image_type="jpg", folder=None):
        self.image_name = image_name
        self.image_type = image_type
        
        if folder is not None:
            self.image_path = fr"{images_folder}\{folder}\{self.image_name}.{self.image_type}"
        else:
            self.image_path = fr"{images_folder}\{self.image_name}.{self.image_type}"
        
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

    def set_pixel(self, i=0, j=0, color=[0,0,0]):
        if (i >= 0 and i < self.image_size[0]) and (j >= 0 and j < self.image_size[1]):
            self.image[i][j] = color
        return

    def set_pixel_range(self, i=0, j=0, color=[0,0,0], h=10):
        for x in range(h):
            for y in range(h):
                self.set_pixel(x+i, y+j, color)
        return