# Simple List

This module makes it easy to make lists that are interactable using the keyboard (arrow keys). 

##### There might still be some bugs when using a Windows OS. Open an [issue](https://github.com/reynirf/Simple-List/issues) if you find one! :) #####
** **
# Setup:
```
$ pip3 install ... (coming soon)
```

# Usage:

```python
import SimpleList
_list = SimpleList(True) # True if you wanna clear window on init
```

Take a look at [general_example](https://github.com/reynirf/Simple-List/blob/master/general_example.py) or [menu_example](https://github.com/reynirf/Simple-List/blob/master/menu_example.py) for working and simple examples. 


# Methods:
TODO: write a documentation for all available methods
** **
* **SimpleList.choose_one(question, alternatives, key, get_index, go_back)**
    * question - string (required)
    * alternatives - list (required)
    * key - string (optional) | default: answer
    * get_index - boolean (optional) | default: False
    * go_back - string (optional) | default: False
* **SimpleList.single_list(alternative)**
    * alternative - string (required)
* **SimpleList.clear_window()**
* **SimpleList.delete_last_lines(n)**
    * n - int (optional) | default: 1
* **SimpleList.color.return_colored(text, color)**
    * text - string (required)
    * color - string (required) | examples: 'red', 'blue', 'cyan', 'bold', 'underline' or 'yellow'



