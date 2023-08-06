<p align='center'><img src='https://github.com/aye20054925/SudoGDZ/blob/main/png/Logo.png?raw=true'></p>
<h1 align='center'>SudoGDZ (Unstable)</h1>
<p align='center'>
	<img src="https://img.shields.io/badge/version-0.1.1-orange">
	<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/sudogdz">
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/aye20054925/sudogdz">
</p>
<p align='center'>Parser of everything from the Russian reshebnik GDZ.RU</p>

## Install
To start learning about cheating, you need to execute one great command
```bash
pip install sudogdz
```

## Using and examples
### Get books and copybooks from GDZ.ru
To start using you have to import sudogdz into your project
```python
import sudogdz
```
Lets get a list of algebra textbooks for 7 Class and print textbook name and authors?
##### script.py
```python
import sudogdz as gdz

schoolitems = gdz.getSchoolItems() # ["matematika", "english", "russkii_yazik", "algebra", ...]

for i in gdz.get('books', schoolclass=7, schoolitem=schoolitems[3], json=True):
    print(f'{i["name"]}\n{i["authors"]}')
```

### Get information about book / copybook
Soon
### Get answers for book / copybook
Soon

## Build from source
In order to build a library from source, you need to install some dependencies
```bash
pip install -r requirements.txt
```
Since the library uses flit to easily build the library, you need to enter the following command
```bash
flit build
```
If you need to not only build, but also install the compiled library, enter
```bash
flit install
```