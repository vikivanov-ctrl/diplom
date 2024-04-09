#Определение разностей альтернатив
def pairwise_row_differences(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    new_matrix = []
    
    # Итерация по всем парам строк
    for i in range(num_rows):
        for j in range(num_rows):
            # Исключаем вычитание строки из самой себя
            if i != j:  
                row_difference = []
                # Подсчет разности между элементами строк
                for col in range(num_cols):
                    diff = matrix[i][col] - matrix[j][col]
                    row_difference.append(diff)
                # Добавление результата в новую матрицу
                new_matrix.append(row_difference)
    
    return new_matrix
