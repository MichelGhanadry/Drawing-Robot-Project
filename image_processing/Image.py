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

    def set_pixel_range(self, i=0, j=0, color='black', h=10):
        for x in range(h):
            for y in range(h):
                self.set_pixel(x+i, y+j, color)
        return

########################################### Edges ###########################################
    
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

    def _is_black(self, i, j):
        color = self.get_pixel(i,j)
        return color[0] == 0 and color[1] == 0 and color[2] == 0

    def _is_edge(self, i=0, j=0, h=10):
        is_edge = False
        for x in range(h):
            for y in range(h):
                if self._is_black(x+i, y+j):
                   is_edge = True
                # self.set_pixel(x+i, y+j, [255,255,255])
        return is_edge

    def get_representative_points(self, sample_size=5, to_color=False):
        res = []
        for i in range(0, self.image_size[0]-sample_size, sample_size):
            for j in range(0, self.image_size[1]-sample_size, sample_size):
                if self._is_edge(i, j, h=sample_size):
                    res.append((i,j))
                    if to_color:
                        self.set_pixel_range(i, j, h=sample_size)
        return res

    def find_path(self, points, h):
        res = []
        while len(points) > 0:
            t = self._find_neighbor(points=points, current_point=points[0], h=h)
            res.append(t)
        return res
        
    def _find_neighbor(self, points, current_point, h):
        res = []
        i,j = current_point
        
        neighbor = ((i+h),j)
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        neighbor = ((i-h),j)
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        neighbor = (i,(j+h))
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        neighbor = (i,(j-h))
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        neighbor = ((i-h),(j-h))
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        neighbor = ((i+h),(j-h))
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        neighbor = ((i-h),(j+h))
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        neighbor = ((i+h),(j+h))
        if neighbor in points:
            points.remove(neighbor)
            rec_res = self._find_neighbor(points=points, current_point=neighbor, h=h)
            res.append(neighbor)
            res.extend(rec_res)

        return res

    def show_path(self, path, h):
        base = self.make_copy()
        for section in path:
            for point in section:
                i, j = point
                base.set_pixel_range(i, j, h=h)
                
        base.show_image()
        return
