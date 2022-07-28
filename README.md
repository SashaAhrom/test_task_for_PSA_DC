# task_for_PSA_DC(test task)
## Description
```
The script removes all typing.cast() calls from the code, that is,
if somewhere in the project module an expression with a cast of the type is used:
var2 = cast(<some type>, var1)
then replace it with:
var2 = var1
```
## Running a project in dev mode
```
- git clone git@github.com:SashaAhrom/test_task_for_PSA_DC.git
- cd test_task_for_PSA_DC
- python main.py <directory path> (other directories can be specified through a space)
```
## System requirements
```
Python 3.7
```
