from .isCorrectRect import isCorrectRect


class RectCorrectError(Exception):
    pass


def intersectionAreaMultiRect(rects_coords):
    num_of_rect = 1
    unique_coords = []

    for rect in rects_coords:
        num_of_rect += 1

        if not isCorrectRect(rect):
            raise RectCorrectError(f"Некорректный {num_of_rect} прямоугольник")
        
        if rect not in unique_coords:
            unique_coords.append(rect)
    
    total_square = 0
    len_of_lst = len(unique_coords)
    for i in range(len_of_lst - 1):

        if i == (len_of_lst - 1):
            break

        for j in range(i + 1, len_of_lst):
            (x1_left, y1_left), (x1_right, y1_right) = unique_coords[i]
            (x2_left, y2_left), (x2_right, y2_right) = unique_coords[j]

            if (
                (x1_left > x2_right)
                or (y1_left > y2_right)
                or (x1_right < x2_left)
                or (y1_right < y2_left)
            ):
              continue


            xCross_left = max(x1_left, x2_left)
            yCross_bottom = max(y1_left, y2_left)
            xCross_right = min(x1_right, x2_right)
            yCross_top = min(y1_right, y2_right)

            crossWidth = xCross_right - xCross_left
            crossHeight = yCross_top - yCross_bottom

            total_square += crossWidth * crossHeight

    return total_square