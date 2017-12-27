#!/usr/bin/python

import base64

copyright = "test"

# 转成bytes string
bytesString = copyright.encode(encoding="utf-8")
print(bytesString)

# base64 编码
encodestr = base64.b64encode(bytesString)
print(encodestr)
print(encodestr.decode())

# 解码
decodestr = base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0FsdmluOTk5OS9wYWMyL21hc3Rlci9zc2NvbmZpZy50eHQ='.encode())
print(decodestr.decode())
