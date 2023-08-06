# BRtools

[![pipy](https://img.shields.io/pypi/v/brtools.svg)](https://pypi.python.org/pypi/brtools)

Brazilian Validators

## Features

- CPF Validation with or without mask
- CNPJ Validation with or without mask

## Modes of use

- CPF

```python
#!/usr/bin/python
from python_brtools import validators

# With mask
validators.is_valid_cpf('386.438.283-19') # True

# Without mask
validators.is_valid_cpf('38643828319') # True
```

- CNPJ

```python
#!/usr/bin/python
from python_brtools import validators

# With mask
validators.is_valid_cnpj('40.158.686/0001-70') # True

# Without mask
validators.is_valid_cnpj('40158686000170') # True
```

# Author

[João Filho](https://joaofilho.dev)
[Github](https://github.com/drummerzzz)

# Credits

This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
