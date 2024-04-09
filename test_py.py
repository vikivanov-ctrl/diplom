def pairwise_row_differences(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    new_matrix = []
    
    # Итерация по всем парам строк
    for i in range(num_rows):
        for j in range(num_rows):
            if i != j:  # Исключаем вычитание строки из самой себя
                row_difference = []
                # Подсчет разности между элементами строк
                for col in range(num_cols):
                    diff = matrix[i][col] - matrix[j][col]
                    row_difference.append(diff)
                # Добавление результата в новую матрицу
                new_matrix.append(row_difference)
    
    return new_matrix

#Парето
def Pareto(matrix,minMax):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    need_to_delete=[]
    # Итерация по всем парам строк
    for i in range(num_rows):
        for j in range(num_rows):
            # Исключаем сравнение строки самой с собой
            if i != j:
                dominating=0
                # Сравнение строк
                for col in range(num_cols):
                    if ((minMax[col]=='min') and (matrix[i][col]<=matrix[j][col])):
                        dominating+=1
                    if ((minMax[col]=='max') and (matrix[i][col]>=matrix[j][col])):
                        dominating+=1
                if ((dominating==num_cols) and (j not in need_to_delete)):
                    need_to_delete.append(j)
    for i in range(len(need_to_delete)-1,-1,-1):
        del matrix[need_to_delete[i]]

# Пример использования:
minMax=["min","max","min", "min", "min", "max"]
matrix = [[80, 90, 6, 5.4, 8, 5],
          [65, 58, 2, 9.7, 1, 1], 
          [83, 60, 4, 7.2, 4, 7],
          [40, 80, 10, 7.5, 7, 10],
          [52, 72, 6, 2, 3, 8],
          [94, 96, 7, 3.6, 5, 6]]

matrix1=[[11,12,13,14,15],[1,2,3,4,5],[6,7,8,9,10]]

minMax1=["max","max","max", "max", "max"]
Pareto(matrix1,minMax1)
print(matrix1)