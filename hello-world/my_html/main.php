<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
   <style>
       h1{
           color: brown;
           font-family: 'Times New Roman', Times, serif;
        }
       p{
            border: 0px solid rgb(202, 241, 247)
        }
        a{
            border: 0px solid antiquewhite;
            
        }
        #p01{   
            font-size: 200%;
            background-color: aqua;
            color:seagreen;
        }
   </style>
</head>
<body>
    <h1>나만의 홈페이지</h1>

    <p style="color:brown; font-size: 100%;">네이버로 접속</p>
    <a href="http://www.naver.com" title="Go to naver">Visit naver</a>
    
    <p style="color:black">dht11 데이터 확인하기 txt</p>
    <p></p><a href="dht11_data.txt" title="데이터">show my data</a></p>

    <p id="dht111">dht11 데이터 phpadmin으로 확인하기</p>
    <a href="http://192.168.137.96/phpmyadmin/sql.php?server=1&db=mysql&table=customers&pos=0&token=736b0cc4618d20724e9ea7492f1fe802" title="dht11데이터">phpadmin으로 확인하기</a>

    <br>

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