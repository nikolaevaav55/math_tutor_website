const buttons = document.querySelectorAll('button'); // получаем NodeList с кнопками

/**
* Функция счетчика
*/
function count() {
  let counter = 0;
  return function() {
    return counter+=1;
  };
}

for (let button of buttons) {
  const counter = count(); // создаем отдельный инстанс функции счетчика для каждой кнопки
  button.addEventListener('click', function() {
    this.textContent = counter(); // прибавляем +1 к счетчику внутри counter
  });
}