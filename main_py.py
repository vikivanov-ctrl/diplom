from flask import Flask, request, render_template, Response
from MyPythonModules.Pareto_func import Pareto
from MyPythonModules.pairwise import pairwise_row_differences
from MyPythonModules.prefer_func import usual, u_kind, v_kind, level_kind,v_kind_interval, gausova
from MyPythonModules.agregate_fun import agregate
from MyPythonModules.flow_fun import flow, flow_plus, flow_minus, clear_flow
from copy import deepcopy


#Главная страница
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main_html():
    
    return render_template('main.html')

#Получаем данные из js
@app.route('/result', methods=['GET', 'POST'])
def result():
    #Обработать информацию которая пришла
    if request.method=="POST":
        information=request.data
        information=information.decode()
        information=information[1:-1]
        result_info.clear()
        PROMETHEEII(information)
        return Response(status=200)
    #отобразить информацию
    else:
        if len(result_info[0])==1:
            return render_template("result_pareto.html", pareto=result_info[0])
        return render_template('result.html',rang=result_info[0], pairwise=result_info[1], 
                                prefer=result_info[2], agregat=result_info[3],
                                index=result_info[4], kriteri=result_info[5], alt=result_info[6],
                                flow=result_info[7], flow_plus=result_info[8], flow_minus=result_info[9],
                                flow_clear=result_info[10])

def PROMETHEEII(information):
    #Делим по разделителю /
    information=information.split("/")
    #Какие критерии
    kriteri=information[0].split(",")
    #Веса важности
    weight=information[1].split(",")
    #Направления критериев
    minMax=information[2].split(",")
    #Значения альтернатив
    alternativs=information[3].split(",")
    #Функции предпочтения
    fun_prefer=information[4].split(",")
    #Количество альтернатив и какие альтернативы
    nameAlternativ=information[5].split(",")
    #Тестируем принт
    print(kriteri)
    print(weight)
    print(fun_prefer)
    print(minMax)
    print(alternativs)
    print(nameAlternativ)

    # Создаем матрицу альтернатив
    matrix=[]
    
    schet=0
    while(schet!=(len(alternativs))):
        row=[]
        for i in range(len(kriteri)):
            row.append(float(alternativs[schet]))
            schet+=1
        matrix.append(row)
    #Выводим матрицу
    print("Original_matrix:")
    for row in matrix:
        print(row)
    #Смотрим есть ли Парето оптимальные строки
    Pareto(matrix,minMax,nameAlternativ)
    print("Alternativ_after_pareto:")
    print(nameAlternativ)
    print("Pareto:")
    #Если после Парето осталось 1 альтернатива возвращаем
    if len(nameAlternativ)==1:
        result_info.append(nameAlternativ)
        return 1
    for row in matrix:
        print(row)
    matrix_copy=matrix.copy()
    #Вычисляем разность
    d_matrix=pairwise_row_differences(matrix_copy)
    print("d_matrix:")
    for row in d_matrix:
        print(row)
    #Функции предпочтения
    d_matrix_copy=deepcopy(d_matrix)
    schet_prefer=0
    for i in fun_prefer:
        i_match=i[0]
        match i_match:
          case "1":
               usual(d_matrix_copy,schet_prefer,minMax[schet_prefer])
               schet_prefer+=1 
          case "2":
                u_kind(d_matrix_copy,schet_prefer,i,minMax[schet_prefer])
                schet_prefer+=1 
          case "3":
                v_kind(d_matrix_copy,schet_prefer,i,minMax[schet_prefer])
                schet_prefer+=1
          case "4":
                level_kind(d_matrix_copy,schet_prefer,i,minMax[schet_prefer])
                schet_prefer+=1 
          case "5":
                v_kind_interval(d_matrix_copy,schet_prefer,i,minMax[schet_prefer])
                schet_prefer+=1 
          case "6":
                gausova(d_matrix_copy,schet_prefer,i,minMax[schet_prefer])
                schet_prefer+=1 
    
    #Матрица с предпочтениями
    print("d_matrix_prefer:")
    for row in d_matrix_copy:
        print(row)
    #Забираем в итоговый масив
    matrix_prefer=deepcopy(d_matrix_copy)
    #Вычисление агрегированных индексов
    matrix_agregate=agregate(d_matrix_copy,weight)
    print("Agrigate_matrix:")
    for row in matrix_agregate:
        print(row)

    #Вычисляем поток
    flow_matrix=flow(matrix_agregate, len(nameAlternativ))
    print("Flow_matrix:")
    for row in flow_matrix:
        print(row)
    
    #Вычисляем поток +
    flow_plus_matrix=flow_plus(flow_matrix)
    print("Flow_plus_matrix:")
    for el in flow_plus_matrix:
        print(el)

    #Вычисляем поток -
    flow_minus_matrix=flow_minus(flow_matrix)
    print("Flow_minus_matrix:")
    for el in flow_minus_matrix:
        print(el)
    
    #Чистый поток
    clear_flow_matrix=clear_flow(flow_plus_matrix,flow_minus_matrix)
    print("Clear_flow_matrix:")
    for el in clear_flow_matrix:
        print(el)
    

    #Итоговое ранжирование
    itog_rang=[]
    original_index={}
    for i in range(len(nameAlternativ)):
        original_index["A"+str(i+1)]=clear_flow_matrix[i]
    original_index=sorted(original_index.items(), key= lambda x: x[1], reverse=True)
    original_index_sort=dict(original_index)
    #Проверка полученного словаря
    print(original_index)
    print(original_index_sort)

    for key in original_index_sort:
        itog_rang.append(key)
    
    itog_rang_string=''
    for el in itog_rang:
        itog_rang_string+=el
        if (itog_rang.index(el)+1)!= len(itog_rang):
            if  original_index_sort[el]==original_index_sort[itog_rang[(itog_rang.index(el)+1)]]:
                itog_rang_string+='='
            else:
                itog_rang_string+='>'

    print(itog_rang_string)
    #Добавляем итговое ранжирование
    result_info.append(itog_rang_string)
    #Корректируем и добавляем матрицу попарных сравнений
    for i in range(len(d_matrix)):
        for j in range(len(d_matrix[i])):
            d_matrix[i][j]= "{:.{}f}".format(d_matrix[i][j], 2) 
    result_info.append(d_matrix)

   
    #Корректируем и добавляем матрицу предпочтений
    for i in range(len(matrix_prefer)):
        for j in range(len(matrix_prefer[i])):
            matrix_prefer[i][j]= "{:.{}f}".format(matrix_prefer[i][j], 3) 
    result_info.append(matrix_prefer)
    #Корректируем и добавляем агрегированные индексы предпочтения
    for i in range(len(matrix_agregate)):
        matrix_agregate[i]= "{:.{}f}".format(matrix_agregate[i], 3) 
    result_info.append(matrix_agregate)
    
    
    #Добавляем индексы для таблицы разностей
    nameAlternativ_table=[]
    for i in range (len(nameAlternativ)):
        for j in range(len(nameAlternativ)):
            if i!=j:
                nameAlternativ_table.append("A"+str(i+1)+","+" A"+str(j+1))
    result_info.append(nameAlternativ_table)

     #Добавляем к критериям агрегир. индекс
    kriteri.append("π(a,b)")
    result_info.append(kriteri)

     #Добавляем название альтернатив
    result_info.append(nameAlternativ)
    
    #Корректируем и добавляем матрицу потока
    for i in range(len(flow_matrix)):
        for j in range(len(flow_matrix[i])):
            flow_matrix[i][j]= "{:.{}f}".format(flow_matrix[i][j], 3) 
    result_info.append(flow_matrix)

    #Корректируем и добавляем матрицу положительного потока
    for i in range(len(flow_plus_matrix)):
        flow_plus_matrix[i]= "{:.{}f}".format(flow_plus_matrix[i], 3) 
    result_info.append(flow_plus_matrix)

    #Корректируем и добавляем матрицу отрицательного потока
    for i in range(len(flow_minus_matrix)):
        flow_minus_matrix[i]= "{:.{}f}".format(flow_minus_matrix[i], 3) 
    result_info.append(flow_minus_matrix)

     #Корректируем и добавляем матрицу чистого потока
    for i in range(len(clear_flow_matrix)):
        clear_flow_matrix[i]= "{:.{}f}".format(clear_flow_matrix[i], 3) 
    result_info.append(clear_flow_matrix)
    return 1

    
#Глобальные переменные
result_info=[]
if __name__ == '__main__': 

    app.run(debug=True)