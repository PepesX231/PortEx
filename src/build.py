"""Build index.html from the template and the embedded assets.

Usage:  python src/build.py
The template uses {{placeholders}}; data.json maps each placeholder to a data URI.
"""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tpl = open(os.path.join(ROOT, 'src', 'port-express.tpl.html'), encoding='utf-8').read()
data = json.load(open(os.path.join(ROOT, 'src', 'data.json'), encoding='utf-8'))
for k, v in data.items():
    tpl = tpl.replace('{{' + k + '}}', v)
left = re.findall(r'\{\{\w+\}\}', tpl)
assert not left, f'unfilled placeholders: {left}'
html = ('<!doctype html>\n<html lang="th">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n</head>\n<body>\n'
        + tpl + '\n</body>\n</html>\n')
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html', len(html) // 1024, 'KB')
