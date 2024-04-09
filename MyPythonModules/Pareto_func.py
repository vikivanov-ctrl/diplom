#Парето
def Pareto(matrix,minMax,name_alternativ):
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
                if ((dominating==num_cols) and (j not in need_to_delete) and (i not in need_to_delete) and (matrix[i]!=matrix[j])):
                    need_to_delete.append(j)
    for i in range(len(need_to_delete)):
        del matrix[max(need_to_delete)]
        del name_alternativ[max(need_to_delete)]
        need_to_delete.remove(max(need_to_delete))