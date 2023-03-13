# PyPing

Pyping is a simple python module which allow you to use the **ping()** function which returns you a boolean value which significate if the pinged Ip Address is existing or is reachable.

----

## How to **install** `PyPing` module:

First, **clone** this repository using **git clone**:

`git clone https://github.com/MelCanoe/PyPing.git`

Next simply **run** the **setup.py** python file using the **install** parameter:

`python3 setup.py install`

PyPing **is now installed** and you can just **delete** the repository's folder by using this command:

`rm -rf <repository-name>` or if you didn't rename it `rm -rf PyPing`

----

## `PyPing` module **usage**:

First, **import PyPing** at the top of your python script:

`import pyping`

To **ping an Ip Address**, use the **ping()** function:

```
import pyping
pingResult = pyping.ping("127.0.0.1")
```

You can now **see the ping result** with the python's **print()** function:

```
import pyping
pingResult = pyping.ping("127.0.0.1")
print(pingResult)
```

----

# Credits:

### Author : [MelCanoe](https://github.com/MelCanoe) (github profil)
### Release Date : 13/03/2023
### Used language : Python3 3.10.6
