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
- Install and activate the virtual environment
- Install dependencies from requirements.txt file
- pip install -r requirements.txt
- In the project folder, enter the command python3 homework.py
```
## System requirements
```
Python 3.7
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:SashaAhrom/test_task_for_PSA_DC.git
```

```
cd test_task_for_PSA_DC
```

Запустить проект:

```
python main.py <путь к каталогу> (через пробел возможно указать другие каталоги)
```
