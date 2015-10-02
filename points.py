# чтение из файла in.txt, где 1 строка = 1 точка в формате (x, y) или [x, y], где x, y - числа
# вывод в файл out.txt и на консоль
from scipy import spatial

points = []
try:
    f = open("in.txt", "r")
    for line in f:
        point = eval(line)
        if isinstance(point[0], (float, int)) and isinstance(point[1], (float, int)):
            points.append(point)
        else:
            raise IOError

except IOError:
    print("File reading error! Using test point list\n")
    points = [[1,1], [2,1], [4,1], [5,2], [1,3], [3,2]]


f = open("out.txt", "w")

for point in points:
    data = points.copy()
    data.remove(point)
    tree = spatial.KDTree(data)
    distance, index = tree.query(point)
    neighbours = tree.query_ball_point(point, 2. * distance)
    f.write('point ({0},{1}) has radius {2} and {3} neighbours\n'.format(point[0], point[1], distance, len(neighbours)))
    print('point ({0},{1}) has radius {2} and {3} neighbours'.format(point[0], point[1], distance, len(neighbours)))