# WhatTheFunc

This library helps programmers understand what a function, method, or attribute does by asking ChatGPT to explain it in layman's terms. Must use your own OpenAI API key.

## Features

- **Explain Code**: Get simple explanations for code elements using ChatGPT.
- **API Key Management**: Easily set your own OpenAI API key for secure access.

## Installation

```bash
pip install whatthefunc
```

## Usage

```python
from whatthefunc import WTF
from dotenv import load_dotenv # don't forget to import

wtf = WTF("Hardcoded API key")
# or set OPENAI_API_KEY as an environment variable and leave WTF() blank. (Preferred method)

response = wtf.wtfunc("np.shape()")
print(response)

```

## Requirements

- Python 3.7+
- OpenAI API key
- OpenAI
- Python Dotenv

## License

MIT
