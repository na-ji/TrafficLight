from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
from typing import TypeVar

if TYPE_CHECKING:
    from trafficlight.proto import Proto


class BaseOutput(metaclass=ABCMeta):
    @abstractmethod
    async def start(self) -> None:
        pass

    @abstractmethod
    async def add_record(self, rpc_id: int, rpc_status: int, protos: list[Proto]):
        pass


AnyOutput = TypeVar("AnyOutput", bound=BaseOutput)