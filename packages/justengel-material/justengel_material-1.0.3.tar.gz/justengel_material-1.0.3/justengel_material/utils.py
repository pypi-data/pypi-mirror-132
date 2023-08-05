from typing import ClassVar
from dataclasses import dataclass


__all__ = ['Link', 'Message']


@dataclass
class Link:
    name: str
    href: str = '#'


@dataclass
class Message:
    msg_type: str
    msg: str

    MESSAGE_TYPES: ClassVar = {
        'debug': "rounded yellow",
        'info': "rounded light-blue",
        'success': "rounded green",
        'warning': "orange",
        'error': "red",
        }

    @property
    def msg_class(self):
        return self.MESSAGE_TYPES.get(str(self.msg_type).lower(), 'rounded light-blue')
