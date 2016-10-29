from Vector import Vector


class Base:
    def __init__(self, position, area_center, area_width, area_heigth):
        self.position = position
        self.area_center = area_center
        self.area_heigth = area_heigth
        self.area_width = area_width

    def in_area(self):
        return self.position.x <= self.area_center.x + self.area_width//2 and \
               self.position.x >= self.area_center.x - self.area_width//2 and \
               self.position.y <= self.area_center.y + self.area_heigth//2 and \
               self.position.y >= self.area_center.y - self.area_heigth//2


    def move_by(self, vector):
        if self.in_area():
            self.position += vector
        else:
            center_direction = self.area_center - self.position
            print(center_direction)
            moving_vector = center_direction / center_direction.length() * vector.length()
            self.position += moving_vector

