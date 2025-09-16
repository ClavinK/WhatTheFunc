# WhatTheFunc

This library helps programmers understand what a function, method, or attribute does by asking ChatGPT to explain it in layman's terms. Must use your own OpenAI API key.

## Features

- **Explain Code**: Get simple explanations for code elements using ChatGPT.
- **API Key Management**: Easily set your own OpenAI API key for secure access.

## Installation

```bash
pip install what-the-func
```

## Usage

```python
from what_the_func import WTF

wtf = WTF("your api key")
or
set OPENAI_API_KEY as an environment variable and leave WTF() blank

response = wtf.wtfunc("np.shape()")
print(response)

```

## Requirements

- Python 3.7+
- OpenAI API key
- OpenAI

## License

MIT
