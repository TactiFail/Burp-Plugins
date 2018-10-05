<?php

$somexml = <<<EOF
<outer>
    <inner>
        <username>tactifail</username>
        <password>hunter2spooky4me</password>
        <role>administrator</role>
    </inner>
</outer>
EOF;

$key = pack('H*', "9320a6826a36c059da81d7c6ccb41ebfbc7f59de47a8d6dccfe95a9b7f2f97c1");

$iv_size = mcrypt_get_iv_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC);

$iv = mcrypt_create_iv($iv_size, MCRYPT_RAND);
$enc = mcrypt_encrypt(MCRYPT_RIJNDAEL_128, $key, $somexml, MCRYPT_MODE_CBC, $iv);

$iv = urlencode(base64_encode($iv));
$enc = urlencode(base64_encode($enc));

$url = "sso_signin.php?iv=$iv&enc=$enc";

?>
<html>
<head>
    <title>Base64 Truncate Demo</title>
    <meta http-equiv="refresh" content="5;<?php echo $url; ?>">
</head>
<body>
    <p>You will be automatically redirected in 5 seconds...</p>
</body>
</html>
