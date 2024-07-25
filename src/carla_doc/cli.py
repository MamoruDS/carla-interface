from .utils.logging import LogLevel


class Args:
    # @alias=i
    input_root: str

    patches_root: str

    extra_root: str

    # @alias=o
    output_root: str

    # @alias=l
    level: LogLevel = LogLevel.WARNING
