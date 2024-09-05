from typing import Final

__version__: Final[str]
PLAIN: int
PREFORMATTED: int
BULLETCHAR: str

class BaseParser:
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def parseFile(self, filename): ...
    def parseText(self, textBlock): ...
    def readLine(self, line) -> None: ...
    def endPara(self) -> None: ...
    def beginPre(self, stylename) -> None: ...
    def endPre(self) -> None: ...
    def image(self, filename) -> None: ...

class Parser(BaseParser):
    def vSpace(self, points) -> None: ...
    def pageBreak(self) -> None: ...
    def custom(self, moduleName, funcName) -> None: ...
    def nextPageTemplate(self, templateName) -> None: ...

def parseFile(filename): ...
def parseText(textBlock): ...
