<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style>
        table, th, td {
           border: 1px solid black;
           padding: 10px;
           border-collapse: collapse;
        }
        </style>
    </head>
    <body>
       <center>
          <h1>C300 Temperature & Humidity & Pressure</h1>
          <table>
             <tr>
               <th>Date</th>
               <th>Time</th>
               <th>Temperature</th>
               <th>Pressure</th>
               <th>Humidity</th> 
             </tr>
             <?php 
		$username = "pi"; 
		$password = "c300"; 
		$database = "mydb"; 
		$mysqli = new mysqli("localhost", $username, $password, $database); 
		$query = "SELECT * FROM data";

		if ($result = $mysqli->query($query)) {
		    while ($row = $result->fetch_assoc()) {
			$field1name = $row["date"];
			$field2name = $row["time"];
			$field3name = $row["temperature"];
			$field4name = $row["pressure"];
			$field5name = $row["humidity"]; 

			echo '<tr> 
				  <td>'.$field1name.'</td> 
				  <td>'.$field2name.'</td> 
				  <td>'.$field3name.'</td> 
				  <td>'.$field4name.'</td> 
				  <td>'.$field5name.'</td> 
			      </tr>';
		    }
		    $result->free();
		} 
	     ?>
          </table>
       </center>
    </body>
</html>
