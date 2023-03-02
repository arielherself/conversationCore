# conversationCore: An HTTPS backend for ChatGPT API

## Usage

Sample request:

```json
{
  "key": "[Issued by server side]",
  "prompts": [
    {"role": "user", "content": "Hello! How are you?"}, 
    {"role": "assistant", "content": "I'm fine, thank you."}, 
    {"role": "user", "content": "What is the weather like today?"}
  ]
}
```

## Prerequisites

`openai>=0.27.0`. Use:

```
pip install -r requirements.txt
```

## Deploy

- `local_secrets.OPENAI_API_KEY`: Get it at https://platform.openai.com
- `trustedKeys`: One key for each line, used for authentication.
- `cert.pem`: SSL certificate
- `key.pem`: SSL key

The default port is `6088`. You can change it in `main.py`.

## Front-end Demo

https://arielherself.github.io/chatgpt
