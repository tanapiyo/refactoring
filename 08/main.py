#from abc import ABCMeta, abstractmethod
class Shape:
   TYPECODE_LINE = 0
   TYPECODE_RECTANGLE = 1
   TYPECODE_OVAL = 2
   def __init__(self, typecode, startx, starty, endx, endy):
       self._startx = startx
       self._starty = starty
       self._endx = endx
       self._endy = endy
   def get_name(self):
       pass
   def __str__(self):
       return '[' + self.get_name() + ', (' + str(self._startx) +  \
           ', ' + str(self._starty) + ')-' + '(' + str(self._endx) + \
           ', ' + str(self._endy) + ') ]'
   def draw(self):
       pass
class LineShape(Shape):
   def get_name(self):
       return "LINE"
   def draw(self):
       print('draw_line:{}'.format(str(self)))
class RectangleShape(Shape):
   def get_name(self):
       return "RECTANGLE"
   def draw(self):
       print('draw_rectangle:{}'.format(str(self)))
class OvalShape(Shape):
   def get_name(self):
       return "OVAL"
   def draw(self):
       print('draw_oval:{}'.format(str(self)))