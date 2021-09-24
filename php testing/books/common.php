<?php
// common.php - файл с общими данными и функциями
$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
$dbbase = "books";

function GetTable($table, $where)
{
	// Сделать глобальные переменные с данными по доступу к базе
	// доступными в данной функции
	global $dbhost, $dbuser, $dbpass, $dbbase;
	// Создаём объект типа "соединение с MySQL"
	$connection = new mysqli($dbhost, $dbuser, $dbpass, $dbbase);
	
	// Если возникла ошибка при подключении, пишем о ней и прекращаем работу скрипта
	if($connection->connect_error) die("Unable to connect to the database: ".
		$mysqli->connect_error);

	// Переменная с текстом запроса
	$query = "SELECT * FROM $table WHERE $where";
	
	// Делаем запрос к базе, сохраняем результат в переменную
	$result = $connection->query($query);
	
	// Если не удалось выполнить запрос, возвращаем пустой массив в качестве результата
	if($result == FALSE) return array();
	
	$objs = array();
	
	while($row = $result->fetch_assoc())
	{
		// Добавлять в массив в качестве элементов ассоциативные массивы(!),
		// где располагаются поля с данными по конкретной записи
		$objs[]=$row;
	}
	
	// Вернуть полученный массив записей
	return $objs;
}

function GetSimpleTable($table)
{
	// Сделать глобальные переменные с данными по доступу к базе
	// доступными в данной функции
	global $dbhost, $dbuser, $dbpass, $dbbase;
	// Создаём объект типа "соединение с MySQL"
	$connection = new mysqli($dbhost, $dbuser, $dbpass, $dbbase);
	
	// Если возникла ошибка при подключении, пишем о ней и прекращаем работу скрипта
	if($connection->connect_error) die("Unable to connect to the database: ".
		$mysqli->connect_error);

	// Переменная с текстом запроса
	$query = "SELECT ID, Name FROM $table";
	
	// Делаем запрос к базе, сохраняем результат в переменную
	$result = $connection->query($query);
	
	// Если не удалось выполнить запрос, возвращаем пустой массив в качестве результата
	if($result == FALSE) return array();
	
	$objs = array();
	
	while($row = $result->fetch_assoc())
	{
		// Добавлять в массив в качестве элементов ассоциативные массивы(!),
		// где располагаются поля с данными по конкретной записи
		$objs[]= array(
		    // слева - наши внутренние названия для скрипта
			// справа - названия столбцов в базе (с учётом регистра)
			"id" => $row["ID"],
			"name" => $row["Name"]
		);
	}
	
	// Вернуть полученный массив записей
	return $objs;
}

// Функция для генерации тэгов <option>
function GenerateOptions($objects)
{
	foreach($objects as $object)
	{
		$id = $object["id"];
		$name = $object["name"];
		
		echo "<option value=\"$id\">$name</option>";
	}
}

function InsertBook($name, $year, $ed, $pub, $topic)
{
	// Сделать глобальные переменные с данными по доступу к базе
	// доступными в данной функции
	global $dbhost, $dbuser, $dbpass, $dbbase;
	// Создаём объект типа "соединение с MySQL"
	$connection = new mysqli($dbhost, $dbuser, $dbpass, $dbbase);
	
	// Если возникла ошибка при подключении, пишем о ней и прекращаем работу скрипта
	if($connection->connect_error) die("Unable to connect to the database: ".
		$mysqli->connect_error);

	// Переменная с текстом запроса
	$query = "SELECT max(ID) FROM books";
	$result = $connection->query($query);
	if($result == FALSE) return false;
	else
	{
		$row = $result->fetch_array();
		$id = $row[0] + 1;
	}
		
	//echo $id;
	
	$query = "INSERT INTO books VALUES 
		($id, '$name', '$year', '$ed', '$pub', '$topic')";
		
		echo $query;
	
	// Делаем запрос к базе, сохраняем результат в переменную
	$result = $connection->query($query);
	
	// Если не удалось выполнить запрос, возвращаем пустой массив в качестве результата
	if($result == FALSE) return false;
	return true;
}

?>