from pybind11_stubgen import structs


class Convertor:
    def __init__(self): ...

    def arg_self(self) -> structs.Argument:
        return structs.Argument(structs.Identifier("self"))
