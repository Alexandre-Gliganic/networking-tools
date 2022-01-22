class ErrorDuringProcess(Exception):
    def __init__(self,code: int, *args: object) -> None:
        self.code = code
        print(*args)
        super().__init__("Process exited with code " + str(code))