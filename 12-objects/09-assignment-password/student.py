class Password:
    def __init__(self, password: str):
        self.__password = password

    def verify(self, password: str) -> bool:
        return self.__password == password

