from pybind11_stubgen import structs


class Convertor:
    def __init__(self): ...

    @staticmethod
    def arg_self() -> structs.Argument:
        return structs.Argument(structs.Identifier("self"))
