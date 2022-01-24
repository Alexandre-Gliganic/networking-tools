import errno

class ErrorDuringProcess(Exception):
    def __init__(self,code: int,err: str, *args: object) -> None:
        self.code = code
        self.err = err
        #print(*args)
        super().__init__("Process exited with code " + str(code))