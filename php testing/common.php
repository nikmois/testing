<?php
include("config.php");

function ReadFruits($filename)
{
	// Результат: Массив для прочитанных из файла данных по фруктам
	$fruits = array();

	// Открываем файл
	$file = fopen($filename,"r");

	while(!feof($file))
	{
		// Считываем строчку из файла
		$line = fgets($file);
		// Делим её на составляющие по разделителю ("," - запятая)
		$fields = explode(",", $line);
		
		// Создаём ассоциативный массив с данными по одному фрукту
		// (прочитанными из отдельных полей)
		$fruit = array(
			"index" => $fields[0],
			"name" => $fields[1],
			"color" => $fields[2],
			"size" => $fields[3]
		);
		
		// Добавляем ассоциативный массив с данными по фрукту
		// в общий массив фруктов
		$fruits[]=$fruit;
	}
	
	// Закрываем файл
	fclose($file);
	// Возвращаем результат
	return $fruits;
}


// Функция, которая подключается к базе, и формирует список продуктов
// который и возвращает
function ReadProductsDb($id=null)
{
	// Делаем глобальные переменные доступными в контексте функции
	global $DB_HOST, $DB_USER, $DB_PASS, $DB_DATABASE;
	
	$products = array();
	
	// Создаём соединение с базой данных
	$conn = new mysqli($DB_HOST,$DB_USER,$DB_PASS,$DB_DATABASE);
	
	// Если возникла ошибка при соединении
	// останавливаем работу скрипта с текстом об ошибке
	if($conn->connect_error)
		die("Unable to connect to database");
	
	// Строка с SQL-запросом
	// При таком подходе мы уязвимы к SQL-injection
	// ?id="1; DROP DATABASE pcwares;"
	if(isset($id)) $query = "SELECT * FROM products WHERE ID=$id";
	else $query = "SELECT * FROM products";	
	
	// Выполняем запрос, сохраняем данные в переменную
	$result = $conn->query($query);
	
	// Крутимся в цикле до тех пор, пока в очереди
	// остаются строчки, полученные из базы
	while($data = $result->fetch_assoc())
	{
		// Добавляем полученные данные в возвратный массив
		$products[]=$data;
	}
	
	return $products;
}

function GetTableDb($table_name, $id=null)
{
	// Делаем глобальные переменные доступными в контексте функции
	global $DB_HOST, $DB_USER, $DB_PASS, $DB_DATABASE;
	
	$content = array();
	
	// Создаём соединение с базой данных
	$conn = new mysqli($DB_HOST,$DB_USER,$DB_PASS,$DB_DATABASE);
	
	// Если возникла ошибка при соединении
	// останавливаем работу скрипта с текстом об ошибке
	if($conn->connect_error)
		die("Unable to connect to database");
	
	// Строка с SQL-запросом
	// При таком подходе мы уязвимы к SQL-injection
	// ?id="1; DROP DATABASE pcwares;"
	if(isset($id)) $query = "SELECT * FROM $table_name WHERE ID=$id";
	else $query = "SELECT * FROM $table_name";	
	
	// Выполняем запрос, сохраняем данные в переменную
	$result = $conn->query($query);
	
	// Крутимся в цикле до тех пор, пока в очереди
	// остаются строчки, полученные из базы
	while($data = $result->fetch_assoc())
	{
		// Добавляем полученные данные в возвратный массив
		$content[]=$data;
	}
	
	return $content;
}

// manufacturer = 1
// producttype = 2
/*array(
	"manufacturer" => 1,
	"producttype" => 2
);*/

function GetTableWhere($table_name,$filter=null)
{
	// Делаем глобальные переменные доступными в контексте функции
	global $DB_HOST, $DB_USER, $DB_PASS, $DB_DATABASE;
	
	$content = array();
	
	// Создаём соединение с базой данных
	$conn = new mysqli($DB_HOST,$DB_USER,$DB_PASS,$DB_DATABASE);
	
	// Если возникла ошибка при соединении
	// останавливаем работу скрипта с текстом об ошибке
	if($conn->connect_error)
		die("Unable to connect to database");
	
	// Строка с SQL-запросом
	// При таком подходе мы уязвимы к SQL-injection
	// ?id="1; DROP DATABASE pcwares;"
	//if(isset($id)) $query = "SELECT * FROM $table_name WHERE ID=$id";
	//else $query = "SELECT * FROM $table_name";
	$query = "SELECT * FROM $table_name";

	// Если обозначены значения фильтра, тогда формируем SELECT с WHERE
	if($filter != null && !empty($filter))
	{
		$query.=" WHERE "; // "SELECT * FROM products WHERE "
		
		$last = count($filter)-1;
		
		// Вариант 1: quick hack через foreach
		/*$ctr = 0;
		foreach($filter as $key => $value)
		{
			$query.="$key=$value"; 
			if($ctr++ < $last) $query.=" AND ";
			// Итерация 1: "SELECT * FROM products WHERE manufacturer=1"
			// Итерация 2: "SELECT * FROM products WHERE manufacturer=1 AND producttype=2"
		}*/
		
		// Вариант 2: for с применением итератора по массиву
		for($i = 0; $i < $last; $i++)
		{
			$query.= key($filter)."=".current($filter)." AND ";
			next($filter);
		}
		$query.= key($filter)."=".current($filter);
		// SELECT * FROM products WHERE manufacturer=1 AND producttype=2
	}
	
	// Выполняем запрос, сохраняем данные в переменную
	$result = $conn->query($query);
	
	if(!$result) 
	{
		echo "Query: $query\n";
		die("Query error: ".$coon->error);
	};
	
	// Крутимся в цикле до тех пор, пока в очереди
	// остаются строчки, полученные из базы
	while($data = $result->fetch_assoc())
	{
		// Добавляем полученные данные в возвратный массив
		$content[]=$data;
	}
	
	return $content;
}

function InsertProduct($product)
{
	$name = $product["Name"];
	$sku = $product["SKU"];
	$manuf = $product["Manufacturer"];
	$type = $product["Type"];
	$msrp = $product["MSRP"];
	$warranty = $product["Warranty"];
	$imgurl = $product["ImgURL"];
	$infourl = $product["InfoURL"];
	$desc = $product["Description"];
	
	// Делаем глобальные переменные доступными в контексте функции
	global $DB_HOST, $DB_USER, $DB_PASS, $DB_DATABASE;
	
	// Создаём соединение с базой данных
	$conn = new mysqli($DB_HOST,$DB_USER,$DB_PASS,$DB_DATABASE);
	
	// Если возникла ошибка при соединении
	// останавливаем работу скрипта с текстом об ошибке
	if($conn->connect_error)
		die("Unable to connect to database");
	
	// Строка с SQL-запросом
	$query = "INSERT INTO products (Name, SKU, Manufacturer, ProductType, MSRP, Warranty, 
		ImageURL, InfoURL, Description) 
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
		
	// Использование prepared statements вместо query() со строкой запроса -
	// вариант с защитой от SQL-injection 
	
	// Компилируем запрос
	$prepared_statement = $conn->prepare($query);
	
	// Привязываем данные к запросу
	$prepared_statement->bind_param("ssiidisss", $name, $sku, $manuf, 
		$type, $msrp, $warranty, $imgurl, $infourl, $desc);
	
	// Выполняем запрос, сохраняем данные в переменную
	//$result = $conn->query($query);
	$result = $prepared_statement->execute();
	
	// Если возникла ошибка при запросе выводим
	if(!$result) die("Query error: ".$conn->error);
	
	// Закрываем соединение
	$conn->close();
}

/*$products = array(
	array("ID"=>1, "Name"=>"Core i9-11900K", "Manufacturer"=>1),
	array("ID"=>2, "Name"=>"Core i7-11700K", "Manufacturer"=>1)
);*/

function PrintTable($data)
{
	// Это шаблон, на основе которого формируем HTML-разметку таблицы
	$table_html = "<table>
		<thead>
			<tr>{header}			</tr>
		</thead>
		<tbody>{rows}		</tbody>
</table>";
	
	// Здесь формируем заголовок таблицы
	//$header.="<th>ID</th>"
	$header = "\n";
	
	// Здесь формируем записи таблицы
	$rows = "\n";
	
	// Берём первую запись по счёту, проходим по её полям (ключам ассоциативного массива)
	// и формируем на их основе заголовок таблицы
	foreach($data[0] as $key => $value)
	{
		$header.="\t\t\t\t<th>$key</th>\n";
	}
	
	// Задание: сформировать строки таблицы (с данными)
	foreach($data as $entry)
	{
		$rows.="\t\t\t<tr>\n";
		foreach($entry as $key => $value)
		{
			$rows.="\t\t\t\t<td>$value</td>\n";
		}
		$rows.="\t\t\t</tr>\n";
	}
	
	// Производим замену {header} в шаблоне на содержимое $header
	$table_html = str_replace("{header}",$header,$table_html);
	$table_html = str_replace("{rows}",$rows,$table_html);
	
	// В конце возвращаем результат
	return $table_html;
}
?>