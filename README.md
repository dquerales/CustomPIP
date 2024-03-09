# CustomPIP

*This is an example about how to publish a python package using Github*

## Installation
```
!pip install git+https://github.com/dquerales/CustomPIP.git
```

### Usage

```
from pyexample.utils import read_dataframe
```

```
import pandas as pd
df = pd.DataFrame()
read_dataframe(df)
```

### Colab

Example using colab: https://colab.research.google.com/drive/1syFqje61sUIy6B3rdkRmLQZqtgwqS13Q?authuser=0#scrollTo=NhOATuHH7PKJ


## How to make a pip file

1. Install setuptools using:

```
pip install setuptools
```

2. create setup.py with the following template:
```
from setuptools import setup

setup(
    name='pyexample',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/dquerales/CustomPIP',
    author='Daniel Querales',
    author_email='dquerales@gmail.com',    
    packages=['pyexample'],
    install_requires=['pandas>=1.5.3',
                      ],
)    
```

3. Change directory to the same place as setup.py
```
cd current_directory
```

4. Verify if everything is Ok:
   
```
pip install .
```

5. Try uninstall the package
```
pip uninstall pyexample
```

# Contact me
Daniel Querales - d.querales@gmail.com
