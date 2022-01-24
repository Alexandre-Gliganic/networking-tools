import asyncio
import discord
from src.tools.error import *

async def execute_prog(cmd: str,timeout: int = 10):
    """
    Execute a program and return the stdout and stderr as a tuple.
    returns: (stdout,stderr)
    """
    process = await asyncio.create_subprocess_shell(f"timeout {timeout} {cmd}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate()
    if process.returncode == 124: # timeout
        raise TimeoutError
    if process.returncode != 0:
        raise ErrorDuringProcess(process.returncode)
    res=stdout.decode()
    err=stderr.decode()

    return res,err


async def execute_prog_realtime(cmd: str,timeout: int = 10,msg: discord.Message = None):
    """
    Execute a program and edit the message in realtime.
    """
    process = await asyncio.create_subprocess_shell(f"timeout {timeout} {cmd}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    msg1 = "```py\n"
    
    while process.returncode is None:
        await asyncio.sleep(0.01)
        line = await process.stdout.readline()
        line = line.decode()
        if line:
            msg1 += line
            await msg.edit(content=msg1 + "```")

    while line := await process.stdout.readline():
        line = line.decode()
        if line:
            msg1 += line
            await msg.edit(content=msg1+ "```")

    if process.returncode == 124: # timeout
        raise TimeoutError
    if process.returncode != 0:
        err=""
        while line := await process.stderr.readline():
            line = line.decode()
            if line:
                err += line + "\n"
        raise ErrorDuringProcess(process.returncode,err)