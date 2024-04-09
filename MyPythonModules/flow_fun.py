def flow(matrix,len_alternative):
    flow_matrix=[]
    schet_flow=0
    append_zero=0
    while(schet_flow!=len(matrix)):
        row=[]
        for i in range(len_alternative):
            if append_zero==i:
                row.append(float(0))
                continue
            row.append(matrix[schet_flow])
            schet_flow+=1
        flow_matrix.append(row)
        append_zero+=1
    return flow_matrix

def flow_plus(flow_matrix):
    flow_plus_matrix=[]
    sum=0
    for i in range(len(flow_matrix)):
        for j in range(len(flow_matrix[0])):
            sum+=flow_matrix[i][j]
        flow_plus_matrix.append(sum)
        sum=0
    return flow_plus_matrix

def flow_minus(flow_matrix):
    flow_minus_matrix=[]
    sum=0
    for i in range(len(flow_matrix)):
        for j in range(len(flow_matrix[0])):
            sum+=flow_matrix[j][i]
        flow_minus_matrix.append(sum)
        sum=0
    return flow_minus_matrix

def clear_flow(flow_plus,flow_minus):
    clear_flow=[]
    for i in range(len(flow_plus)):
        clear_flow.append(flow_plus[i]-flow_minus[i])
    return clear_flow