# Winged-Python
![main](https://github.com/micheltlutz/Winged-Python/actions/workflows/python-package.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/micheltlutz/Winged-Python/graph/badge.svg?token=UvaQd65VVD)](https://codecov.io/gh/micheltlutz/Winged-Python)
[![codebeat badge](https://codebeat.co/badges/b0a28fb9-ffba-4214-980f-a4333781f98f)](https://codebeat.co/projects/github-com-micheltlutz-winged-python-main)

# =============

Winged-Python is an innovative Domain-Specific Language (DSL) library for efficient HTML writing in Python. Mirroring its Swift counterpart, Winged-Python is based on the DSL concept, focusing on simplification and specificity in HTML generation. Using the Composite design pattern, the library enables developers to construct HTML structures in a logical, organized, and reusable manner.

This library is created to be fully independent, not requiring integration with specific server frameworks or front-end libraries. This offers developers the freedom to use Winged-Python across a variety of projects, from simple static pages to complex web applications, keeping the code clean, readable, and efficient.

## Usage Example


## Contributing

To contribute, it's simple, follow the guidelines below to prepare your development environment

## Create environment

User OS terminal or IDE terminal

### Linux or macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### Windows

```bash
.\venv\Scripts\activate.bat
```

```bash
.\venv\Scripts\activate.ps1`
```

## Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

## Basic Usage

```python

from winged.HTML.div import Div
from winged.HTML.h import H
from winged.HTML.table import Table
from winged.HTML.string import String

divC = Div(("class", "container"))

h = H("1")
h.add(String("Hello World"))
divC.add(h)

table = Table()
table.add_table_headers(["Name", "Age", "Height", "Location"])  # Define headers

table.add_row()
table.add_in_row(String("John"))
table.add_in_row(String("25"))
table.add_in_row(String("1.80"))
table.add_in_row(String("New York"))

table.add_row()
table.add_in_row(String("Maria"))
table.add_in_row(String("23"))
table.add_in_row(String("1.50"))
table.add_in_row(String("New Jersey"))

divC.add(table)

print(divC.generate())
```

## Output

```html
<div class="container">
  <h1>Hello World</h1>
  <table>
    <thead>
      <th>Name</th>
      <th>Age</th>
      <th>Height</th>
      <th>Location</th>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>25</td>
        <td>1.80</td>
        <td>New York</td>
      </tr>
      <tr>
        <td>Maria</td>
        <td>23</td>
        <td>1.50</td>
        <td>New Jersey</td>
      </tr>
    </tbody>
  </table>
</div>
```


## TODO

- [ ] Make documentation with Sphinx
