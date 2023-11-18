<?php

include('flag.php');
if (isset($_POST['secret'])){
    if ( md5($_POST['secret']) == 0 ){
        echo("お帰りーボッス!。これフラッグ上げます<br>");
        echo($flag . '<br><br>');
    }else{
        echo("NO　です<br><br>");
    }
}
highlight_file(__FILE__);
?>

<!DOCTYPE html>
<head>
    <title>PHP マアジック</title>
</head>

<body>
<form action="" method="POST">
<p>Secret?</p>
<input type="text" name="secret">
<input type="submit" value="Submit">
</form>
</html>
