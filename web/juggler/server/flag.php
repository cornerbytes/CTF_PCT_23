<?php

$flag_file = fopen("/flag.txt", "r");
$flag = fgets($flag_file);
fclose($flag_file);

?>
