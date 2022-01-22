import asyncio
import discord
async def execute_prog(cmd: str,timeout: int = 10):
    
    process = await asyncio.create_subprocess_shell(f"timeout {timeout} {cmd}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate()
    if process.returncode == 124: # timeout
        raise TimeoutError
    if process.returncode != 0:
        raise TypeError(stderr.decode(),process.returncode)
    res=stdout.decode()
    err=stderr.decode()

    return res,err,process.returncode


async def execute_prog_realtime(cmd: str,timeout: int = 10,msg: discord.Message = None):
    process = await asyncio.create_subprocess_shell(f"timeout {timeout} {cmd}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    start_msg = msg.content + "```py\n"
    new_msg = ""
    
    while process.returncode is None:
        await asyncio.sleep(0.01)
        line = await process.stdout.readline()
        line = line.decode().strip()
        if line:
            new_msg += line + "\n"
            await msg.edit(content=start_msg + new_msg + "```")

    while line := await process.stdout.readline():
        line = line.decode().strip()
        if line:

            new_msg += line + "\n"
            await msg.edit(content=start_msg + new_msg + "```")

    if process.returncode == 124: # timeout
        raise TimeoutError
    if process.returncode != 0:
        err=""
        while line := await process.stderr.readline():
            line = line.decode().strip()
            if line:
                err += line + "\n"
                await msg.edit(content=start_msg + new_msg + err + "```")
        raise TypeError(process.returncode)
    
    return process.returncode