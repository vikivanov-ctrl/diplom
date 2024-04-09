def agregate(matrix,weight):

    agregate_matrix=[]
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows):
        sum=0
        for j in range(num_cols):
            sum+=matrix[i][j]*float(weight[j])
        agregate_matrix.append(sum)

    return agregate_matrix
    