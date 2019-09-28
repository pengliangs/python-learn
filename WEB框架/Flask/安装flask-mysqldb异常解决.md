```lua
(.env) D:\github\python-learn>pip install mysqlclient
Collecting mysqlclient
  Using cached https://files.pythonhosted.org/packages/4d/38/c5f8bac9c50f3042c8f05615f84206f77f03db79781db841898fde1bb284/mysqlclient-1.4.4.tar.gz
Building wheels for collected packages: mysqlclient
  Building wheel for mysqlclient (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: 'd:\github\python-learn\.env\scripts\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\EDZ\\AppData\\Local\\Temp\\pip-install-o5hjvxxu\\mysqlclient\\setup.py'"'"'; __file__='"'"'C:\\Users\\EDZ\\AppData\\Local\\Temp\\pip-install-o5hjvxxu\\mysqlclient\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d 'C:\Users\EDZ\AppData\Local\Temp\pip-wheel-z2a5uad2' --python-tag cp37
       cwd: C:\Users\EDZ\AppData\Local\Temp\pip-install-o5hjvxxu\mysqlclient\
  Complete output (24 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build\lib.win32-3.7
  creating build\lib.win32-3.7\MySQLdb
  copying MySQLdb\__init__.py -> build\lib.win32-3.7\MySQLdb
  copying MySQLdb\_exceptions.py -> build\lib.win32-3.7\MySQLdb
  copying MySQLdb\compat.py -> build\lib.win32-3.7\MySQLdb
  copying MySQLdb\connections.py -> build\lib.win32-3.7\MySQLdb
  copying MySQLdb\converters.py -> build\lib.win32-3.7\MySQLdb
  copying MySQLdb\cursors.py -> build\lib.win32-3.7\MySQLdb
  copying MySQLdb\release.py -> build\lib.win32-3.7\MySQLdb
  copying MySQLdb\times.py -> build\lib.win32-3.7\MySQLdb
  creating build\lib.win32-3.7\MySQLdb\constants
  copying MySQLdb\constants\__init__.py -> build\lib.win32-3.7\MySQLdb\constants
  copying MySQLdb\constants\CLIENT.py -> build\lib.win32-3.7\MySQLdb\constants
  copying MySQLdb\constants\CR.py -> build\lib.win32-3.7\MySQLdb\constants
  copying MySQLdb\constants\ER.py -> build\lib.win32-3.7\MySQLdb\constants
  copying MySQLdb\constants\FIELD_TYPE.py -> build\lib.win32-3.7\MySQLdb\constants
  copying MySQLdb\constants\FLAG.py -> build\lib.win32-3.7\MySQLdb\constants
  running build_ext
  building 'MySQLdb._mysql' extension
  error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
  ----------------------------------------
  ERROR: Failed building wheel for mysqlclient
  Running setup.py clean for mysqlclient
Failed to build mysqlclient
Installing collected packages: mysqlclient
  Running setup.py install for mysqlclient ... error
    ERROR: Command errored out with exit status 1:
     command: 'd:\github\python-learn\.env\scripts\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\EDZ\\AppData\\Local\\Temp\\pip-install-o5hjvxxu\\mysqlclient\\setup.py'"'"'; __file__='"'"'C:\\Users\\EDZ\\AppData\\Local\\Temp\\pip-install-o5hjvxxu\\mysqlclient\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\EDZ\AppData\Local\Temp\pip-record-kszsdfd1\install-record.txt' --single-version-externally-managed --compile --install-headers 'd:\github\python-learn\.env\include\site\python3.7\mysqlclient'
         cwd: C:\Users\EDZ\AppData\Local\Temp\pip-install-o5hjvxxu\mysqlclient\
    Complete output (24 lines):
    running install
    running build
    running build_py
    creating build
    creating build\lib.win32-3.7
    creating build\lib.win32-3.7\MySQLdb
    copying MySQLdb\__init__.py -> build\lib.win32-3.7\MySQLdb
    copying MySQLdb\_exceptions.py -> build\lib.win32-3.7\MySQLdb
    copying MySQLdb\compat.py -> build\lib.win32-3.7\MySQLdb
    copying MySQLdb\connections.py -> build\lib.win32-3.7\MySQLdb
    copying MySQLdb\converters.py -> build\lib.win32-3.7\MySQLdb
    copying MySQLdb\cursors.py -> build\lib.win32-3.7\MySQLdb
    copying MySQLdb\release.py -> build\lib.win32-3.7\MySQLdb
    copying MySQLdb\times.py -> build\lib.win32-3.7\MySQLdb
    creating build\lib.win32-3.7\MySQLdb\constants
    copying MySQLdb\constants\__init__.py -> build\lib.win32-3.7\MySQLdb\constants
    copying MySQLdb\constants\CLIENT.py -> build\lib.win32-3.7\MySQLdb\constants
    copying MySQLdb\constants\CR.py -> build\lib.win32-3.7\MySQLdb\constants
    copying MySQLdb\constants\ER.py -> build\lib.win32-3.7\MySQLdb\constants
    copying MySQLdb\constants\FIELD_TYPE.py -> build\lib.win32-3.7\MySQLdb\constants
    copying MySQLdb\constants\FLAG.py -> build\lib.win32-3.7\MySQLdb\constants
    running build_ext
    building 'MySQLdb._mysql' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
    ----------------------------------------
ERROR: Command errored out with exit status 1: 'd:\github\python-learn\.env\scripts\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\EDZ\\AppData\\Local\\Temp\\pip-install-o5hjvxxu\\mysqlclient\\setup.py'"'"'; __file__='"'"'C:\\Users\\EDZ\\AppData\\Local\\Temp\\pip-install-o5hjvxxu\\mysqlclient\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\EDZ\AppData\Local\Temp\pip-record-kszsdfd1\install-record.txt' --single-version-externally-managed --compile --install-headers 'd:\github\python-learn\.env\include\site\python3.7\mysqlclient' Check the logs for full command output.
```

# 安装 flask-mysqldb

```
pip install flask-mysqldb
```

抛出如上异常，貌似是版本不不对应导致的；

解决办法:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

下载python当前版本对应版本客户端 cp后面对应的版本号

执行:
```
pip install D:xx/xx/mysqlclient-1.4.4-cp37-cp37m-win32.whl
```
