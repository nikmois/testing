function FillManufSelect()
{
	// Сделать асинхронный запрос на получение данных в JSON к серверу
	// function(data,status) - функция-обработчик, которая будет запущена,
	// когда данные будут получены с сервера (через неопределённое время)
	$.getJSON("getManufacturers.php", function(data,status){
		// Получаем ссылку на <select>
		var sel = $("#select-manuf");
		
		for(var i=0; i<data.length; i++)
		{
			// Создаём новый элемент <option></option>
			var opt = $(document.createElement("option"));
			
			// <option>Intel</option>
			opt.text(data[i]["Name"]);
			
			// <option value="1">Intel</option>
			opt.val(data[i]["ID"]);
			
			// Присоединить <option> в качестве дочернего к <select>
			sel.append(opt);
		}
	});
}

// Задание 2: По аналогии сделать динамическую подгрузку типов продуктов