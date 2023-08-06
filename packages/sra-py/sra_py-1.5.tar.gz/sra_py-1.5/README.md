# sra_py
A python wrapper for [some-random-api](https://some-random-api.ml)

## Requirements
[Python 3.8.6 or more](https://python.org)  

## Installation
```cmd
pip install sra_py
```

## Examples
```py
# Random Dog Image

import sra_py as sra

dog = sra.dog()

print(dog)

#####

# Lyrics

import sra_py as sra

ly = sra.lyrics("song title goes here")
print(f'Title - {ly.title}\nAuthor - {ly.author}\n\n{ly.lyrics}')

#####

# Meme

import sra_py as sra
import os

m = sra.meme()
m.save("meme.png")
os.startfile("meme.png")
```

## Links
[Documentation](https://github.com/Atidipt123/sra_py/blob/main/docs/api.md)  
[Some Random API](https://some-random-api.ml)  
[PyPI](https://pypi.org/project/sra_py)