import json
from wsgiref.simple_server import make_server
import urllib.parse
import re
import core
import ssl

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'application/json'), 
                              ('Access-Control-Allow-Origin', '*'), 
                              ('Access-Control-Allow-Credentials', 'true'), 
                              ('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, HEAD'),
                              ('Access-Control-Max-Age', '3600'),
                              ('Access-Control-Allow-Headers', 'access-control-allow-origin, authority, content-type, version-info, X-Requested-With')])
    if env.get('CONTENT_LENGTH', 0) == '':
        return [b'']
    else:
        request_body = env['wsgi.input'].read(int(env.get('CONTENT_LENGTH', 0)))
        print(env)
        json_str = request_body.decode('utf8')
        json_str = re.sub('\'', '\"', json_str)
        print(json_str)
        json_dict = json.loads(json_str)
        key = json_dict['key']
        prompts = json_dict['prompts']
        return core.chat(key, prompts)

if __name__ == '__main__':
    port = 6088
    httpd = make_server('0.0.0.0', port, app)
    httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='cert.pem', keyfile='key.pem', ssl_version=ssl.PROTOCOL_TLS)
    httpd.serve_forever()
