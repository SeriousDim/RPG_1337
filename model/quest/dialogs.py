from dataclasses import dataclass


@dataclass
class DialogRemark:
    remark: str
    speaker: str


@dataclass
class DialogsPart:
    dialogs: list[DialogRemark]
