# Weather CLI - Python

# Used 

https://darksky.net - for getting current weather & temperature. <br />
https://ipinfo.io/ - for getting location by IP. <br />
https://locationiq.com - for gettig coordinates of current location.

# Modules

Click - as parser for command line arguments, requests & json.

# Usage 

```python
python3 main.py current # May be inaccurate because of getting location by IP
```

# Or

```python
python3 main.py New-York # or any other city
```

# For better user experience

Add an alias to .bashrc via

```python
nano ~/.bashrc

# add this line in the end

alias weather='python3 path/to/script/main.py'

# and activate it

source ~/.bashrc
```

And use then via alias

```python
weather New-York
```

# Result example

```python
The weather in New-York is - Overcast
Temperature is - 4 C
```
