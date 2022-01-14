class Rectangle:

  def __init__(self,width, height):
    self.width = width
    self.height = height
    self.perimeter = 2*width + 2*height
    self.diagonal = ((width**2+height**2)**.5)

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2*self.width + 2*self.height

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    
    if(self.height > 50 or self.width >50):
      return 'Too big for picture.'

    icon = '*'
    line = self.width*icon + '\n'
    starPicture = self.height *line
    return starPicture

  def get_amount_inside(self, shape):
    return (self.get_area() / shape.get_area()) // 1


class Square(Rectangle):

  def __init__(self, height):
    super().__init__(height,height)
  
  def __str__(self):
      return f'Square(side={self.width})'

  def set_side(self, side):
      self.width = side
      self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width
  
  def set_height(self, height):
    self.width = height
    self.height = height