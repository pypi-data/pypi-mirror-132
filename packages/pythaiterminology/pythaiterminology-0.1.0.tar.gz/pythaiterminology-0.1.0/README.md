<div align="center">
  <img src="https://github.com/khunfloat/pythaiterminology/blob/main/PyThaiTerminology_logo.jpg" widtd=250 height=250/>
  <h1>PyThaiTerminology : Thai terminology corpus library</h1>
  <!--<a href="https://pypi.python.org/pypi/pythainlp"><img alt="pypi" src="https://img.shields.io/pypi/v/pythainlp.svg"/></a>--!>
  <a href="https://www.python.org/downloads/release/python-370/"><img alt="Python 3.7" src="https://img.shields.io/badge/python-3.7-blue.svg"/></a>
  <a href="https://colab.research.google.com/github/PyThaiNLP/tutorials/blob/master/source/notebooks/pythainlp_get_started.ipynb"><img alt="Google Colab Badge" src="https://badgen.net/badge/Launch%20Quick%20Start%20Guide/on%20Google%20Colab/blue?icon=terminal"/></a>
</div>

## Installation

Use the package manager pip to install PyThaiTerminology.

```bash
pip install pythaiterminology
```

## Usage

```python
import pythaiterminology.corpus as ptt

# returns 'frozenset({'พิทาโกรัส', 'คอร์ด', 'คอมพลีเมนต์', 'แคลคูลัส', ...})'
ptt.math_terminology()

# returns 'frozenset({'โปรตอน', 'รังสีแกมมา', 'รังสีอินฟาเรด', 'อิเล็กตรอน', ...})'
ptt.physics_terminology()

# returns 'frozenset({'อัลดีไฮด์', 'โลหะอัลคาไล', 'บัฟเฟอร์', 'แคโทด', ...})'
ptt.chemical_terminology()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
