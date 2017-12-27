#!/usr/bin/python

import base64, json
from urllib import parse, request

# 输出内容:user=admin&password=admin
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0FsdmluOTk5OS9wYWMyL21hc3Rlci9zc2NvbmZpZy50eHQ="
# url = "aHR0cHM6Ly9jb2RpbmcubmV0L3UvQWx2aW45OTk5L3AvaXAvZ2l0L3Jhdy9tYXN0ZXIvc3Njb25maWcudHh0"

req = request.Request(url='%s%s%s' % (url, '?', ''), headers=header_dict)
res = request.urlopen(req)
res = res.read()

done = base64.b64decode(res.decode(encoding='utf-8'))
ssrStr = str(done, 'utf-8')
ssrStr = ssrStr.replace('\\r', '')
ssrStr = ssrStr.replace('\\n', '')
ssrStr = ssrStr.replace('\\t\\t', '\\t')

# textJson = json.loads(ssrStr)
# print(ssrStr['configs'])
print(ssrStr)

with open('D:\\ssr.json', 'a') as f:
    f.write(ssrStr)
