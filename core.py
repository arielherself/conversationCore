import json
import openai
import local_secrets

openai.api_key = local_secrets.OPENAI_API_KEY
def FALLBACK(*args, **kwargs):
    return wrap({'message': 'Not permitted'})

wrap = lambda d: [bytes(json.dumps(d), encoding='utf8')]

def authentication(fallback_func):
    def authDec(func):
        def c(key, *args, **kwargs):
            with open('trustedKeys', encoding='utf8') as f:
                keys = [l.strip() for l in f.readlines()]
            if key in keys:
                return func(*args, **kwargs)
            else:
                return fallback_func(*args, **kwargs)
        return c
    return authDec

@authentication(fallback_func=FALLBACK)
def chat(prompts: list):
    response = dict(openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=prompts))
    return wrap({'message': response['choices'][0]['message']['content']})