
# PyTender

## Installation
```
pip install pytender
```
Requirement is [python-docx](https://python-docx.readthedocs.io/en/latest/), which is installed automatically.

*If you are on windows and don't have `lxml` (dependency of python-docx), download the appropriate [lxml.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) file and use `pip` to install it.*

## Usage
```
python -m pytender.gui
```
Then provide the details of the contract.
Documents will be created in the *'SOURCE'* sub-directory of the corresponding *project* directory.

*Tip: add a shortcut to* ```python -m pytender.gui``` *in your favourite directory.*

![Check Gif @ blob/PyTender.gif](https://github.com/pragyanone/pytender/blob/master/blob/PyTender.gif)

## License
[MIT](https://choosealicense.com/licenses/mit/)
