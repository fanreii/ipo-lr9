from .isCorrectRect import isCorrectRect


class RectCorrectError(Exception):
    pass


def isCollisionRect(list_1, list_2):

  firstRectangleCoords, secondRectangleCoords = list_1, list_2

  if not isCorrectRect(firstRectangleCoords):
    raise RectCorrectError("1й прямоугольник некорректный")
  
  elif not isCorrectRect(secondRectangleCoords):
    raise RectCorrectError("2й прямоугольник некорректный")

  else:

    (x1_left, y1_left), (x1_right, y1_right) = firstRectangleCoords
    (x2_left, y2_left), (x2_right, y2_right) = secondRectangleCoords

    #  если хоть одно истинно, то прямоугольники точно не пересекаються
    if (
        (x1_left > x2_right)
        or (y1_left > y2_right)
        or (x1_right < x2_left)
        or (y1_right < y2_left)
        ):
      return False
    
    return True
  