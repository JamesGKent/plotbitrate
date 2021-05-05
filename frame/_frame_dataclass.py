import dataclasses


@dataclasses.dataclass
class Frame:
    __slots__ = ["time", "size", "pict_type", "key_frame"]
    time: float
    size: int
    pict_type: str
    key_frame: bool

    @staticmethod
    def get_fields():
        return [f.name for f in dataclasses.fields(Frame)]
