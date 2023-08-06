<p align="center"><img src="https://raw.githubusercontent.com/tquangsdh20/pyfreetts/master/.github/logo.svg"></p>

<p align="center"> <img src="https://github.com/tquangsdh20/pyfreetts/actions/workflows/test.yml/badge.svg?style=plastic"> <a href="https://codecov.io/github/tquangsdh20/pyfreetts/commit/5d0da7ae595f845c64742d9d64260d7018453856"><img src="https://codecov.io/gh/tquangsdh20/pyfreetts/branch/master/graphs/badge.svg?branch=master"></a></p>


## Features

- Support text to speech with many pretty voices options
- Support download file mp3 from TTS

## Installation
**Windows**
```
python -m pip install pyfreetts
```
**Linux**
```
pip install pyfreetts
```
**macOS**
```
sudo pip3 install pyfreetts
```
## How does it work?

### Setup Language for Converting

To setup language and voice using the method `setup_voice(language_code)`, where `language_code` :

- English US : `am`
- English UK : `br`
- Portuguese (Brazil): `pt-br`
- Portuguese (Portugal): `pt`
- The other languages : `ISO LANGUAGE CODE 639-1`

```python
from pyfreetts import Text2Speech

module = Text2Speech()
module.setup_voice("am")
module.convert("how are you?")
module.save_to_file("test.mp3")
module.close()
```

Output

```
>> All voices for your language:
>>    1. Joey - Male - SAPI5
>>    2. Justin - Male - SAPI5
>>    3. Matthew - Male - SAPI5
>>    4. Salli - Female - SAPI5
>>    5. Joanna - Female - SAPI5
>>    6. Ivy - Female - SAPI5
>> Make your choice: 3
```

<a href="https://github.com/tquangsdh20/mateco"><p align="center"><img src="https://img.shields.io/badge/Github-tquangsdh20-orange?style=social&logo=github"></p></a>