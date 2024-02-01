import time

import alpc
import alpc2
import secrets


printable_chars = [chr(byte) for byte in range(0, 128) if chr(byte).isprintable()]
data = []
for i in range(0, 10000):
    s = ''
    for j in range(0, 3):
        s += secrets.SystemRandom().choice(printable_chars)
    data.append(s)
    
print('starting speed test\n')

t0 = time.time()
for s in data:
    result = alpc.encode(s)
print('alpc: ' + str(time.time() - t0))

t0 = time.time()
for s in data:
    result = alpc2.encode(s)
print('alpc2: ' + str(time.time() - t0))
