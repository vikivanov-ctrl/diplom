import json
import numpy as np
from flask import Flask, request, render_template
from MyPythonModules.Pareto_func import Pareto
from MyPythonModules.pairwise import pairwise_row_differences
from MyPythonModules.prefer_func import usual, u_kind, v_kind, level_kind,v_kind_interval, gausova
from MyPythonModules.agregate_fun import agregate
from MyPythonModules.flow_fun import flow, flow_plus, flow_minus, clear_flow


#Главная страница
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main_html():
    return render_template('main.html')

#Получаем данные из js
@app.route('/result', methods=['GET', 'POST'])
def result():
    information=request.data
    information=information.decode()
    information=information[1:-1]
    #Выводим, что получили
    print (information)
    PROMETHEEII(information)
    return "1"

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
    for row in matrix:
        print(row)
    #Вычисляем разность
    d_matrix=pairwise_row_differences(matrix)
    print("d_matrix:")
    for row in d_matrix:
        print(row)
    #Функции предпочтения
    d_matrix_copy=d_matrix.copy()
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
    clear_flow_matrix_copy=clear_flow_matrix.copy()
    print("Clear_flow_matrix:")
    for el in clear_flow_matrix:
        print(el)
    

    #Итоговое ранжирование
    itog_rang=[]
    for i in range (len(clear_flow_matrix)):
        max_value = max(clear_flow_matrix_copy)
        ind=clear_flow_matrix_copy.index(max_value)
        itog_rang.append(nameAlternativ[ind])
        clear_flow_matrix_copy[ind]=-1000

    for el in itog_rang:
        print(el+">",end=" ")

    return 1

    

if __name__ == '__main__': 
    app.run(debug=True)