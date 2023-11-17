<?php
	if (isset($_GET['text'])) {
		$text = $_GET['text'];
		$output = shell_exec("figlet " . $text);
	}
?>
<!DOCTYPE html>
<head>
	<title>Cool Banner</title>
</head>
<body>
	<h1>Buat banner mu dengan gaya! - Cool Banner</h1><br>
	<form action="" method="get">
	  <label for="text">Text:</label>
	  <input type="text" name="text"><br><br>
	  <input type="submit" value="Go!">
	</form><br>
	<pre><?php echo $output; ?></pre>
</body>
</html>
