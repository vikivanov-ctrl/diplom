from math import exp
#Обычная функция
def usual(d_matrix_copy,col,napravlenie):
    num_rows = len(d_matrix_copy)
    if (napravlenie=="max"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]<=0):
                d_matrix_copy[i][col]=0
            else:
                d_matrix_copy[i][col]=1
    if (napravlenie=="min"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]>=0):
                d_matrix_copy[i][col]=0
            else:
                d_matrix_copy[i][col]=1

#U-образная
def u_kind(d_matrix_copy, col, parametr, napravlenie):
    num_rows = len(d_matrix_copy)
    q=float(parametr[4:])
    if (napravlenie=="max"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]<=q):
                d_matrix_copy[i][col]=0
            else:
                d_matrix_copy[i][col]=1
    if (napravlenie=="min"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]>=-q):
                d_matrix_copy[i][col]=0
            else:
                d_matrix_copy[i][col]=1
    
#V-образная
def v_kind(d_matrix_copy, col, parametr, napravlenie):
    num_rows = len(d_matrix_copy)
    p=float(parametr[4:])
    if (napravlenie=="max"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]<=0):
                d_matrix_copy[i][col]=0
            if ((d_matrix_copy[i][col]>0) and (d_matrix_copy[i][col]<=p)):
                d_matrix_copy[i][col]=float(d_matrix_copy[i][col]/p)
            if (d_matrix_copy[i][col]>p):
                d_matrix_copy[i][col]=1
    if (napravlenie=="min"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]>=0):
                d_matrix_copy[i][col]=0
            if ((d_matrix_copy[i][col]>=-p) and (d_matrix_copy[i][col]<0)):
                d_matrix_copy[i][col]=float(d_matrix_copy[i][col]/-p)
            if (d_matrix_copy[i][col]<-p):
                d_matrix_copy[i][col]=1

#Уровневая функция
def level_kind(d_matrix_copy, col, parametr, napravlenie):
    num_rows = len(d_matrix_copy)
    q=float(parametr[parametr.find("q:")+2:parametr.find("p:")])
    p=float(parametr[parametr.find("p:")+2])
    if (napravlenie=="max"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]<=q):
                d_matrix_copy[i][col]=0
            if ((d_matrix_copy[i][col]>q) and (d_matrix_copy[i][col]<=p)):
                d_matrix_copy[i][col]=0.5
            if (d_matrix_copy[i][col]>p):
                d_matrix_copy[i][col]=1
    if (napravlenie=="min"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]>=-q):
                d_matrix_copy[i][col]=0
            if ((d_matrix_copy[i][col]>=-p) and (d_matrix_copy[i][col]<-q)):
                d_matrix_copy[i][col]=0.5
            if (d_matrix_copy[i][col]<-p):
                d_matrix_copy[i][col]=1

#V-образная c интервалом
def v_kind_interval(d_matrix_copy, col, parametr, napravlenie):
    num_rows = len(d_matrix_copy)
    q=float(parametr[parametr.find("q:")+2:parametr.find("p:")])
    p=float(parametr[parametr.find("p:")+2])
    if (napravlenie=="max"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]<=q):
                d_matrix_copy[i][col]=0
            if ((d_matrix_copy[i][col]>q) and (d_matrix_copy[i][col]<=p)):
                d_matrix_copy[i][col]=(float(d_matrix_copy[i][col])-float(q))/(float(p)-float(q))
            if (d_matrix_copy[i][col]>p):
                d_matrix_copy[i][col]=1
    if (napravlenie=="min"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]>=-q):
                d_matrix_copy[i][col]=0
            if ((d_matrix_copy[i][col]>=-p) and (d_matrix_copy[i][col]<-q)):
                d_matrix_copy[i][col]=(abs(float(d_matrix_copy[i][col]))-abs(float(q)))/(abs(float(p))-abs(float(q)))
            if (d_matrix_copy[i][col]<-p):
                d_matrix_copy[i][col]=1

#Гаусова
def gausova(d_matrix_copy, col, parametr, napravlenie):
    num_rows = len(d_matrix_copy)
    s=float(parametr[parametr.find("s:")+2:])
    if (napravlenie=="max"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]<=0):
                d_matrix_copy[i][col]=0
            else:
                d_matrix_copy[i][col]=1-exp((-d_matrix_copy[i][col]*d_matrix_copy[i][col])/(2*s*s))
            
    if (napravlenie=="min"):
        for i in range(0,num_rows):
            if (d_matrix_copy[i][col]>=0):
                d_matrix_copy[i][col]=0
            else:
                d_matrix_copy[i][col]=1-exp((-d_matrix_copy[i][col]*d_matrix_copy[i][col])/(2*s*s))