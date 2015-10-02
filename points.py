from scipy import spatial

data = [[1,1], [2,1], [4,1], [5,2], [1,3], [3,2]]

tree = spatial.KDTree(data)
# print('ball', [data[i] for i in tree.query_ball_point([2,1], 1)])
distance, index = tree.query([2, 5])
print('query', distance, index, data[index])