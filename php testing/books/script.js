var selectedBook = null;

// Заполняем <select> при загрузке страницы
function FillSelect()
{
	// Ресурс (страница), который пытаемся получать
	var request_url="getBooksJson.php";
	
	// Делаем асинхронный запрос на получение ресурса с веб-сервера
	// Второй аргумент - функция-обработчик, которая будет вызвана,
	// когда броузер получит от веб-сервера ответ
	$.getJSON(request_url, function(data, status)
	{
		// Для каждой записи в массиве данных (массив JSON)
		$.each(data, function(index, item)
		{
			// Создать в дереве DOM <option>
			var opt = document.createElement("option");
			// <option value=...
			opt.value = item.ID;
			// <option>...</option>
			opt.innerHTML = item.Title;
			// Добавить <option> как дочерний элемент
			// к <select id="book-select"></select>
			$("#book-select").append(opt);
		});
		// Синхронизируем маркер выбранной книги 
		// с выбранным значением в <select>
		selectedBook = $("#book-select").val();
	});
}

// Получаем данные по выбранной книге, отображаем их
function GetBook()
{
	// Обработка ошибок: Если книга не выбрана, 
	// тут же делаем возврат
	if(selectedBook == null) return;
	// Делаем запрос того же ресурса, но с id книги 
	// в качестве параметра
	var $req = "getBooksJson.php?id="+selectedBook;
	// Делаем асинхронный запрос по той же схеме, что и выше
	$.getJSON($req, function(data, status) {
		// Получаем ссылку на объект <div class="main-bookinfo">
		var div = $(".main-bookinfo");
		
		// Запускаем анимацию типа Fade Out с длительностью 400мс
		// После окончания анимации запускается функция обработчик
		
		// Делаем это для того, чтобы манипуляции с разметкой были
		// скрыты от пользователя
		div.fadeOut(400,function()
		{
			// Убираем все дочерние элементы из <div class="main-bookinfo">
			div.children().empty();
			// Создаём список <ul>
			var list = document.createElement("ul");
			// field - поля в Json, display - отображаемые подсказки
			var fields = [
				{field:"Title",display:"Название"},
				{field:"YearPublished",display:"Год издания"},
				{field:"Edition",display:"Издание"},
				{field:"Publisher",display:"Издатель"},
				{field:"Authors",display:"Автор(ы)"},
			];
			
			for(i=0;i<fields.length; i++)
			{
				// Создать <li> для текущего поля
				var entry = document.createElement("li");
				// Выставить ему текст в стиле:
				// Подсказка: Значение Поля
				// Пример: "Название: The C++ Programming Language"
				entry.innerHTML = fields[i].display+": "+data[0][fields[i].field];
				// Подшиваем <li> к <ul>
				list.append(entry);
			}
			
			// Подшиваем <ul> к <div>
			$(".main-bookinfo").append(list);
			// Делаем для <div> анимацию Fade In с длительностью 400мс
			// Тут дальнейшая обработка не нужна, поэтому обработчик не указан
			div.fadeIn(400);
		});
	});
}

// Когда документ будет полностью загружен
$(document).ready(function() {
	// Производим получение данных и настройку обработки событий
	
	// Наполняем <select>
	FillSelect();
	
	// При нажатии на кнопку получаем информацию по выбранной книге
	$("#select-button").click(function(){
		GetBook();
	});
	
	// Обработка событий: при смене выбранного элемента в <select>
	$("#book-select").change(function(){
		
		// Меняем переменную "выбранная книга" на value выбранного <option>
		// (который является ID книги)
		selectedBook = $(this).val();
	});
});