### shell

``` shell
from amhhandler import shell


cmd = "ls /tmp"
result = shell.run(cmd)
print(result)

```

### mysql

``` shell
from amhhandler import mysql


dbconfig = {"host":"127.0.0.1","port":3306, "user":"admin", "password":"123456", "db":"mysql"}

dbHandler = mysql.Conn(**dbconfig)
sql = "select * from mysql.user where user='admin';"
result = dbHandler.select(sql)

```

### ding ding robot


### logging
