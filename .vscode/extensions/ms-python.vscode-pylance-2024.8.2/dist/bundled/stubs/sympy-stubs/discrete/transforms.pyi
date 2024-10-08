from typing import Any

def fft(seq, dps=...) -> list[Any] | Any: ...
def ifft(seq, dps=...) -> list[Any] | Any: ...
def ntt(seq, prime) -> list[int] | list[Any | int] | Any: ...
def intt(seq, prime) -> list[int] | list[Any | int] | Any: ...
def fwht(seq) -> list[Any] | Any: ...
def ifwht(seq) -> list[Any] | Any: ...
def mobius_transform(seq, subset=...) -> list[Any] | Any: ...
def inverse_mobius_transform(seq, subset=...) -> list[Any] | Any: ...
