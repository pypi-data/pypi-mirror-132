## What is it?
Package for clean text to alfabeth only, clean text to number only, clean name, split name, clean nik, validation format nik and text scoring similarity
## Installation
```shell
pip install claming
```
## How to use
### Import package
```python
from claming import Cleansing, Matching
```
### Define function
```python
clean = Cleansing()
match = Matching()
```
### Alfabeth only
user params case sensitive : upper, lower, capitalize or title, default is capitalize
```python
clean.alfabeth_only('+62 adalah kode negara Indonesia', case_sensitive='capitalize')
# Result
# Adalah kode negara indonesia
```
### Number only
user params output_type : int or str, default is int
```python
clean.number_only("+6281234123412", output_type='int')
# Result
# 6281234123412
```
### Clean name 
case sensitive : upper, lower, capitalize or title, default is upper
```python
clean.clean_name(' John D3ve.r  Smith')
# Result
# {'input': ' John D3ve.r  Smith', 'output': 'JOHN DVER SMITH'}
```
### Clean NIK
user params output_type : int or str, default is str
```python
clean.clean_nik(3212300808080003)
# Result
# {'input': '3212300808080003', 'output': '3212300808080003', 'description': 'NIK format is correct'}
```
### Split name
case sensitive : upper, lower, capitalize or title, default is upper <br />
num_split : number of split 2 or 3, default is 3  <br />
when num_split is 2 : then the first name will be the first word and the last name will be the second until the last word <br />
when num_split is 3 : then the first name will be the first word, the middle name will be the second word and the last name will be the third until the last word 
```python
clean.split_name(' John D3ve.r  Smith', num_split=3)
# Result
# {'original_name': ' John D3ve.r  Smith', 'full_name': 'JOHN DVER SMITH', 'first_name': 'JOHN', 'middle_name': 'DVER', 'last_name': 'SMITH'}

clean.split_name(' John D3ve.r  Smith', num_split=2)
# Result
# {'original_name': ' John D3ve.r  Smith', 'full_name': 'JOHN DVER SMITH', 'first_name': 'JOHN', 'last_name': 'DVER SMITH'}
```
### Text similarity
```python
match.exact_match('JOHN DVER SMITH', 'JOHN DVER SMITH')
# Result
# {'first_text': 'JOHN DVER SMITH', 'second_text': 'JOHN DVER SMITH', 'score': 1, 'max_score': 1}

match.levenshtein_match('JOHN DVER SMITH', 'JOHN DVER SMITH')
# Result
# {'first_text': 'JOHN DVER SMITH', 'second_text': 'JOHN DVER SMITH', 'score': 1.0, 'max_score': 1}

match.part_exact_match('JOHN DVER SMITH', 'JOHN DVER SMITH')
# Result
# {'first_text': 'JOHN DVER SMITH', 'second_text': 'JOHN DVER SMITH', 'score': 1.0, 'max_score': 1}

match.part_levenshtein_match('JOHN DVER SMITH', 'JOHN DVER SMITH')
# Result
# {'first_text': 'JOHN DVER SMITH', 'second_text': 'JOHN DVER SMITH', 'score': 3.0, 'max_score': 3}

match.all_method_match('JOHN DVER SMITH', 'JOHN DVER SMITH')
# Result
# {'first_text': 'JOHN DVER SMITH', 'second_text': 'JOHN DVER SMITH', 'first_text_clean': 'JOHN DVER SMITH', 'second_text_clean': 'JOHN DVER SMITH', 'exact_match': {'score': 1, 'max_score': 1}, 'levenshtein': {'score': 1.0, 'max_score': 1}, 'part_exact_match': {'score': 3, 'max_score': 3}, 'part_levenshtein': {'score': 3.0, 'max_score': 3}}
```