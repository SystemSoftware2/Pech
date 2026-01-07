from kernel.kernel import *
import uasyncio as asyncio

proc_code1 = '''
print(f"USER: Started with PID {pid}")

request = {
    "cmd": "write",
    "path": "/home/log.txt",
    "data": "cool message!",
    "client_pid": pid,
    "reply_pipe": 1
}
request2 = {
    "cmd": "cat",
    "path": "/home/log.txt",
    "client_pid": pid,
    "reply_pipe": 1
}

print(f"USER: Writing and reading /home/log.txt via pipe 0...")

await send(0, request, pid)
await recv(1, pid)

await send(0, request2, pid)
data = await recv(1, pid)

print(f"USER: Result from FS: {data}")
'''

if __name__ == "__main__":
    create_proc(proc_code1, 1)
    boot()

    asyncio.run(scheduler())

