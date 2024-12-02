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
