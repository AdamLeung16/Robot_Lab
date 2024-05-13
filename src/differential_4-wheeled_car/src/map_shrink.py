def read_txt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # 假设每行元素之间用空格分隔
        # 使用列表推导式将每行拆分为列表，并转换为整数类型
        data = [[num for num in line.split(' ')] for line in lines]
    return data

def scale_matrix(data, target_rows, target_cols):
    scaled_matrix = []
    original_rows = len(data)
    original_cols = len(data[0]) if data else 0

    r = original_rows // target_rows
    c = original_cols // target_cols
    fr,fc = 0,0
    for i in range(target_rows):
        row = []
        if i == target_rows-1:
            fr = r+original_rows-r*target_rows
        else:
            fr = r
        for j in range(target_cols):
            if j == target_cols-1:
                fc = c+original_cols-c*target_cols
            else:
                fc = c
            flag = 0
            for rr in range(fr):
                for cc in range(fc):
                    if i*r+rr<original_rows and j*c+cc<original_cols and (data[i*r+rr][j*c+cc]== '100' or data[i*r+rr][j*c+cc]== '-1'):
                        flag +=1
            if flag>0:
                row.append(100)  
            else:
                row.append(0)          
        scaled_matrix.append(row)
    return scaled_matrix
def transpose(data):
    # 使用zip函数进行行列转置
    transposed_data = list(map(list, zip(*data)))
    return transposed_data
def mirror_horizontal(data):
    # 对矩阵进行左右镜像
    mirrored_data = [row[::-1] for row in data]
    return mirrored_data

def mirror_vertical(data):
    # 对矩阵进行上下镜像
    mirrored_data = data[::-1]
    return mirrored_data
def print_matrix(matrix):
    txt = open('/home/adam/catkin_ws/src/differential_4-wheeled_car/map/map_tiny.txt','w')
    for row in matrix:
        for state in row:
            txt.write(str(state)+' ')
        txt.write('\n')

file_path = 'map.txt'  # 替换为你的文件路径
data = read_txt(file_path)
scaled_matrix = scale_matrix(data, 9, 15)
# mirrored_horizontal_data = mirror_horizontal(scaled_matrix)
# 上下镜像
mirrored_vertical_data = mirror_vertical(scaled_matrix)
# transposed_data = transpose(scaled_matrix)
print_matrix(mirrored_vertical_data)