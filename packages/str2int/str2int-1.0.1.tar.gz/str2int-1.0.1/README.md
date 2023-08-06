# Str2Int

My first pip module. 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Str2Int.

```bash
pip install str2int
```

## Usage

```python
from .str2int import str2int
#Just random string of letters and numbers
randomstuff = "I2In3h22j3 -2"
#Use str2int(string) to output only numbers
numonly = str2int(randomstuff)
print(numonly) #['2', '3', '22', '3', '-2']
```

## What's it about
Well it's just there to take away everything but numbers from a string
## License
[MIT](https://choosealicense.com/licenses/mit/)