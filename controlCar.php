<html>
        <head>
        </head>
        <?php
                if(isset($_POST['start']))
                {
                        print_r("da");
                        exec('sudo /usr/bin/python3 fullTest.py 2>&1');
                }
                else
                {
                        print_r("nu");
                }
        ?>

        <body>
                <form action="controlCar.php" method="post" >
                        <input type="submit" name="start"  value="Start">
                </form>
        </body>
</html>
