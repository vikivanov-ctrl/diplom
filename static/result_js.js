
function init()
{

    //Кнопка "Создать таблицу"
    buttonCreateTable=document.getElementById("button_save_result").addEventListener('click', function () {
        window.print();
    })
}

//начать скрипт после загрузки страницы
window.onload=init;