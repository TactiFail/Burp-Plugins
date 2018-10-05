<?php

ini_set('display_errors', 1);
error_reporting(E_ALL);

$key = pack('H*', "9320a6826a36c059da81d7c6ccb41ebfbc7f59de47a8d6dccfe95a9b7f2f97c1");

$iv = base64_decode($_GET['iv']);
$enc = base64_decode($_GET['enc']);

$plain = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, $key, $enc, MCRYPT_MODE_CBC, $iv);

$xml = (simplexml_load_string($plain));

?>
<html>
<head>
    <title>Base64 Truncate Demo</title>
</head>
<body>
<?php

if($xml->inner->role == 'administrator') {
    echo "<p>Welcome, sire</p>\n";
} else {
    echo "<p>Begone, peasant</p>\n";
}

?>
</body>
</html>
