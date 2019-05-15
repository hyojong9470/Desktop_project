<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

    <form method="post">
    <button name="LightON" value="on">LightON</button> 
    <button name="LightOFF" value="off">LightOFF</button> 

    </form>

    <p></p>

    <?php
    if (isset($_POST["LightON"])) {
    exec("sudo python3 /var/www/html/LEDON.py");
    }

    if (isset($_POST["LightOFF"])) {
    exec("sudo python3 /var/www/html/LEDOFF.py");
    }
    ?>
    
</body>
</html>
