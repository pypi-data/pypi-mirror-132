# ini_config_parser

Provides convenient interface for easily managing multiple enviroments (ex: test, prod) just from one config.ini

### Usage

```python
# config_parser.py
ini_parser_singleton = IniParserSingleton().get_environment_as_cmd_arg()
config = ini_parser_singleton.config
```

```python
# config.py
from config_parser import config

PORT = config("PORT", int)
TOKEN = config("TOKEN")
```

```ini
; config.ini
[global]
PORT = 1000
TOKEN = ""

[prod]
PORT = 8000
TOKEN = "foo"

[test]
TOKEN = "bar"
```

Now if you run `python3 your_project.py prod`: PORT == 8000 and TOKEN == "foo"
If you run `python3 your_project.py test`: PORT == 1000 and TOKEN == "bar"

You can also get current environment from file:

```python
# config_parser.py
ini_parser_singleton = IniParserSingleton().get_environment_from_file(".env")
```
