//Функция создания таблицы
function createTable()
{    
    alternativNow=1;
    // массивы
    howManykriteriNow.length=0;
    const check= new Array("K1_check","K2_check","K3_check","K4_check", "K5_check", "K6_check", "K7_check", "K8_check", "K9_check", "K10_check", "K11_check", "K12_check", "K13_check");
    const minMax=new Array("min","max");
    // родительский див и таблица
    var div=document.getElementById("div_alternativ_table");
    var table=document.createElement("table");
    table.setAttribute("class","alternativ_table");
    table.setAttribute("id","alternativ_table_id");
    //Проверяем была ли уже создана таблица
    if (isNewTable==false){
        var oldTable=document.getElementById("alternativ_table_id");
        oldTable.parentNode.removeChild(oldTable);
        isNewTable=true;
    }
    
    tr=table.insertRow();
    //лишняя ячейка для альтернатив
    tr.insertCell();
    var shet=1;
    for(i=0;i<check.length;i++)
    {   
        if(document.getElementById(check[i]).checked){
            //добавляем в глобальный массив
            howManykriteriNow.push("K"+(i+1));
    
            var td=tr.insertCell();
            td.appendChild(document.createTextNode("K"+(i+1)));

            // селект
            var select=document.createElement("select");
            select.setAttribute("id","K"+shet+"_"+"select");
            //1 опция
            var optionOne=document.createElement("option");
            optionOne.text=minMax[0];
            optionOne.value=minMax[0];
            select.appendChild(optionOne);
            //2 опция
            var optionTwo=document.createElement("option");
            optionTwo.text=minMax[1];
            optionTwo.value=minMax[1];
            select.appendChild(optionTwo);
            //добавили селект
            td.appendChild(select);
            shet+=1;
        }
    }
    if (howManykriteriNow.length==0)
    {
        return;
    }
    //первая альтернатива
    tr=table.insertRow();
    //лишняя ячейка для альтернатив
    var tdAlt=tr.insertCell();
    tdAlt.appendChild(document.createTextNode("A1"));
    tdAlt.setAttribute("class","table_");
    //создаем ячейки с инпутами
    shet=1;
    for(var i=0;i<check.length;i++)
    {   
        if(document.getElementById(check[i]).checked){
            

            //создаём ячейку
            var td=tr.insertCell();
            var input=document.createElement("input");
            input.setAttribute("type","number");
            input.setAttribute("class","input_number_alternativ");
            input.setAttribute("id","input_number_alternativ_A1"+"_"+shet);
            td.appendChild(input);
            shet+=1;
        }
    }

    div.appendChild(table);
    isNewTable=!isNewTable;
}

//Проверка весов важности
function weightFormatFun(weight)
{
    if (weight.value>1)
    {
        weight.value=1;
    }

    if (weight.value<0)
    {
        weight.value=0;
    }

}

//Функция добавления альтернативы
function addAlternativ()
{
    
    if (alternativNow==10)
    {
        alert("Максимальное количество альтернатив 10");
        return;
    }
    alternativNow=alternativNow+1;
    var table=document.getElementById("alternativ_table_id");
    tr=table.insertRow();
    var tdAlt=tr.insertCell();
    tdAlt.appendChild(document.createTextNode("A"+alternativNow));
    for (i=0;i<howManykriteriNow.length;i++)
    {
        var td=tr.insertCell();
        var input=document.createElement("input");
        input.setAttribute("type","number");
        input.setAttribute("class","input_number_alternativ");
        input.setAttribute("id","input_number_alternativ_A"+alternativNow+"_"+(i+1));
        td.appendChild(input);
    }
}

//Функция удаления альтернативы
function deleteAlternativ()
{   
    
    if (alternativNow==1)
    {
        alert("Минимальное количество альтернатив 1");
        return;
    }
    alternativNow=alternativNow-1;
    var table=document.getElementById("alternativ_table_id");
    var rowCount = table.rows.length;
    table.deleteRow(rowCount -1);
}

//Функция выбора select
function selectFunction(sel) {
    var selectValue=sel.value;
    var cell=sel.parentNode;
    var row=cell.parentNode;
    switch(selectValue)
    {
        
        //Обычная
        case '1':
            if (row.cells.length==5)
            {
                row.deleteCell(-1);
            }
            break;

        //U-образная
        case '2':
            if (row.cells.length==5)
            {
                row.deleteCell(-1);
            }
            
            var td=row.insertCell();
            td.setAttribute("id",sel.id+"_last_cell");
            td.innerText="q:";
            var qNumber=document.createElement("input");
            qNumber.setAttribute("type","number");
            qNumber.setAttribute("class","input_number_kriteri");
            qNumber.setAttribute("id",sel.id+"_last_cell_qNumber");
            if (sel.id == ("function_preference_K4"))
            {
                qNumber.setAttribute("value",1024);
            }
            if (sel.id == ("function_preference_K5"))
            {
                qNumber.setAttribute("value",1024);
            }
            if (sel.id == ("function_preference_K6"))
            {
                qNumber.setAttribute("value",1024);
            }
            td.appendChild(qNumber);
            break;

        //V-образная
        case '3':
            if (row.cells.length==5)
            {
                row.deleteCell(-1);
            }
            var cell=sel.parentNode;
            var row=cell.parentNode;
            var td=row.insertCell();
            td.setAttribute("id",sel.id+"_last_cell");
            td.innerText="p:";
            var pNumber=document.createElement("input");
            pNumber.setAttribute("type","number");
            pNumber.setAttribute("class","input_number_kriteri");
            pNumber.setAttribute("id",sel.id+"_last_cell_pNumber");
            if (sel.id == ("function_preference_K1"))
            {
                pNumber.setAttribute("value",15);
            }
            td.appendChild(pNumber);
            break;

        //Уровневая 
        case '4':
            if (row.cells.length==5)
            {
                row.deleteCell(-1);
            }
            var cell=sel.parentNode;
            var row=cell.parentNode;
            var td=row.insertCell();
            td.setAttribute("id",sel.id+"_last_cell");
            td.innerHTML="p:";
            var pNumber=document.createElement("input");
            pNumber.setAttribute("type","number");
            pNumber.setAttribute("class","input_number_kriteri");
            pNumber.setAttribute("id",sel.id+"_last_cell_pNumber");
            if (sel.id == ("function_preference_K2")||(sel.id == ("function_preference_K3")))
            {
                pNumber.setAttribute("value",3);
            }

            if (sel.id == ("function_preference_K13"))
            {
                pNumber.setAttribute("value",24);
            }
            
            td.appendChild(pNumber);
            
            td.innerHTML+=" q:";
            var qNumber=document.createElement("input");
            qNumber.setAttribute("type","number");
            qNumber.setAttribute("class","input_number_kriteri");
            qNumber.setAttribute("id",sel.id+"_last_cell_qNumber");

            if (sel.id == ("function_preference_K2")||(sel.id == ("function_preference_K3")))
            {
                qNumber.setAttribute("value",1);
            }

            if (sel.id == ("function_preference_K13"))
            {
                qNumber.setAttribute("value",12);
            }
            td.appendChild(qNumber);
            break;

        //V-образная c интервалом безразличия
        case '5':
            if (row.cells.length==5)
            {
                row.deleteCell(-1);
            }
            var cell=sel.parentNode;
            var row=cell.parentNode;
            var td=row.insertCell();
            td.setAttribute("id",sel.id+"_last_cell");
            td.innerHTML="p:";
            var pNumber=document.createElement("input");
            pNumber.setAttribute("type","number");
            pNumber.setAttribute("class","input_number_kriteri");
            pNumber.setAttribute("id",sel.id+"_last_cell_pNumber");
            if ((sel.id == ("function_preference_K7"))||(sel.id == ("function_preference_K8"))||(sel.id == ("function_preference_K9"))||(sel.id == ("function_preference_K10"))||(sel.id == ("function_preference_K11"))||(sel.id == ("function_preference_K12")))
            {
                pNumber.setAttribute("value",3);
            }
            td.appendChild(pNumber);
            td.innerHTML+=" q:";
            var qNumber=document.createElement("input");
            qNumber.setAttribute("type","number");
            qNumber.setAttribute("class","input_number_kriteri");
            qNumber.setAttribute("id",sel.id+"_last_cell_qNumber");
            if ((sel.id == ("function_preference_K7"))||(sel.id == ("function_preference_K8"))||(sel.id == ("function_preference_K9"))||(sel.id == ("function_preference_K10"))||(sel.id == ("function_preference_K11"))||(sel.id == ("function_preference_K12")))
            {
                qNumber.setAttribute("value",1);
            }
            td.appendChild(qNumber);
            break;
        //Гауссова функция
        case '6':
            if (row.cells.length==5)
            {
                row.deleteCell(-1);
            }
            
            var td=row.insertCell();
            td.setAttribute("id",sel.id+"_last_cell");
            td.innerText="s:";
            var qNumber=document.createElement("input");
            qNumber.setAttribute("type","number");
            qNumber.setAttribute("class","input_number_kriteri");
            qNumber.setAttribute("id",sel.id+"_last_cell_sNumber");
            td.appendChild(qNumber);
            break;
    }
  }

//Функция начала алгоритма
function startAlgoritm()
{
    //Забираем из select данные
    for(var i=0;i<howManykriteriNow.length;i++)
    {   
        var nameId="function_preference_"+howManykriteriNow[i];
        var selectData=document.getElementById(nameId);
        var selectValue=selectData.value;
        switch(selectValue)
        {
            case '1':
                whatInSelect.push(selectValue);
                break;
            case '2':
                qNumber=document.getElementById(nameId+"_last_cell_qNumber");
                whatInSelect.push(selectValue+' '+"q:"+qNumber.value);
                // Проверка на пустоту
                if (qNumber.value.trim().length===0){
                    alert("Пропущен параметр функции предпочтения");
                    return;
                }
                break;
            case '3':
                pNumber=document.getElementById(nameId+"_last_cell_pNumber");
                whatInSelect.push(selectValue+' '+"p:"+pNumber.value);
                // Проверка на пустоту
                if (pNumber.value.trim().length===0){
                    alert("Пропущен параметр функции предпочтения");
                    return;
                }
                break;
            case '4':
                    qNumber=document.getElementById(nameId+"_last_cell_qNumber");
                    pNumber=document.getElementById(nameId+"_last_cell_pNumber");
                    whatInSelect.push(selectValue+' '+"q:"+qNumber.value+' '+"p:"+pNumber.value);
                    // Проверка на пустоту
                    if ((qNumber.value.trim().length===0) || (pNumber.value.trim().length===0)){
                        alert("Пропущен параметр функции предпочтения");
                        return;
                    }
                    break;
            case '5':
                qNumber=document.getElementById(nameId+"_last_cell_qNumber");
                pNumber=document.getElementById(nameId+"_last_cell_pNumber");
                whatInSelect.push(selectValue+' '+"q:"+qNumber.value+' '+"p:"+pNumber.value);
                // Проверка на пустоту
                if ((qNumber.value.trim().length===0) || (pNumber.value.trim().length===0)){
                    alert("Пропущен параметр функции предпочтения");
                    return;
                }
                break;
            case '6':
                sNumber=document.getElementById(nameId+"_last_cell_sNumber");
                whatInSelect.push(selectValue+' '+"s:"+sNumber.value);
                console.log(sNumber.value);
                // Проверка на пустоту
                if (sNumber.value.trim().length===0){
                    alert("Пропущен параметр функции предпочтения");
                    return;
                }
                break;
        }
    }

    //Забираем данные из альтернатив
    for(var i=0;i<alternativNow;i++)
    {
        for(var j=0;j<howManykriteriNow.length;j++)
        {
            whatInAlternativ.push(document.getElementById("input_number_alternativ_A"+(i+1)+"_"+(j+1)).value);
            //Проверка на пропуск ячейки
            if (whatInAlternativ[whatInAlternativ.length-1]=='')
            {
                minAndMaxSelect.length=0;
                whatInAlternativ.length=0;
                whatInSelect.length=0;
                weightKriteri.length=0;
                nameAlternativ.length=0;
                weightSumCheck=0;
                alert("Пропущено значение альтернативы");
                isSend=false;
                return;
            }
            //Проверка на отрицательное значение    
            if (whatInAlternativ[whatInAlternativ.length-1]<0)
                {
                    minAndMaxSelect.length=0;
                    whatInAlternativ.length=0;
                    whatInSelect.length=0;
                    weightKriteri.length=0;
                    nameAlternativ.length=0;
                    weightSumCheck=0;
                    alert("Отрицательное значение альтернативы недопустимо");
                    isSend=false;
                    return;
                }
        }
    }
    console.log(whatInAlternativ)
    //Забираем min max
    for(var i=0;i<howManykriteriNow.length;i++)
    {
        minAndMaxSelect.push(document.getElementById("K"+(i+1)+"_"+"select").value);
    }

    //Забираем веса важности
    for(var i=0;i<howManykriteriNow.length;i++)
    {
        weightKriteri.push(document.getElementById("input_weight_"+howManykriteriNow[i]).value);
        weightSumCheck+=Number(document.getElementById("input_weight_"+howManykriteriNow[i]).value);
    }
    //Забираем название альтернатив
    for(var i=0;i<alternativNow;i++)
    {
        nameAlternativ.push("A"+(i+1));
    }
    //Проверяем сумму весов
    if ((weightSumCheck<0.999) || (weightSumCheck>1.010))
    {
        console.log(weightSumCheck);
        minAndMaxSelect.length=0;
        whatInAlternativ.length=0;
        whatInSelect.length=0;
        weightKriteri.length=0;
        nameAlternativ.length=0;
        weightSumCheck=0;
        alert("Сумма весов важности должна быть равна единице");
        isSend=false;
        return;
    }
    //Отдаём питону
    const url="/result";
    const xhr=new XMLHttpRequest();
    sender=JSON.stringify(howManykriteriNow.toString()+"/"+weightKriteri.toString()+"/"+minAndMaxSelect.toString()+"/"+whatInAlternativ.toString()+"/"+whatInSelect.toString()+"/"+nameAlternativ.toString());
    xhr.open('POST',url);
    xhr.send(sender);
    isSend=true;
    //Создаём вкладку для Результатов
    var li=document.getElementById("finish_page");
    if (document.getElementById("a_finish_page"))
    {
        li.removeChild(document.getElementById("a_finish_page"));
    }
    if (isSend==true)
    {
        var a=document.createElement("a");
        a.setAttribute("href","/result");
        a.setAttribute("id","a_finish_page");
        a.setAttribute("target","_blank");
        a.appendChild(document.createTextNode("Результат"));
        li.appendChild(a);
    }
    //Чистим после отправки массивы
    minAndMaxSelect.length=0;
    whatInAlternativ.length=0;
    whatInSelect.length=0;
    weightKriteri.length=0;
    nameAlternativ.length=0;
    weightSumCheck=0;
}

function init(){

    //Кнопка "Создать таблицу"
    buttonCreateTable=document.getElementById("button_create_table");
    buttonCreateTable.onclick=function(){createTable();}

    //Кнопка "Добавить альтернативу"
    buttonCreateAlternativ=document.getElementById("button_add_alternativ");
    buttonCreateAlternativ.onclick=function(){addAlternativ();}

    //Кнопка "Убрать альтернативу"
    buttonDeleteAlternativ=document.getElementById("button_delete_alternativ");
    buttonDeleteAlternativ.onclick=function(){deleteAlternativ();}

    //Кнопка "Начать вычисления"
    buttonStartAlgoritm=document.getElementById("button_start_algoritm");
    buttonStartAlgoritm.onclick=function(){startAlgoritm();}

    //Вызываем onchange для шаблонов
    for(var i=0;i<13;i++)
    {
        selectFunction(document.getElementById("function_preference_K"+(i+1)));
    }
}

//массив с выбранными критериями
let howManykriteriNow=new Array();
//проверка создана ли таблица уже?
var isNewTable=true;
//проверка для создания вкладки Результаты
var isSend=false;
//Данные из select в kriteri_table
let whatInSelect=new Array();
//Данные из Alternatives
let whatInAlternativ=new Array();
//Min max
let minAndMaxSelect=new Array();
//Веса важности
let weightKriteri=new Array();
//Количество альтернатив сейчас
var alternativNow=1;

//Название Альтернатив
let nameAlternativ=new Array();

//Проверка весов
var weightSumCheck=0;
//начать скрипт после загрузки страницы
window.onload=init;