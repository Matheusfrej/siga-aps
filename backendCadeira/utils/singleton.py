from typing import Any


class SingletonMetaclass(type):
    ''' Classes that have this as a metaclass can only be instantiated once '''
    _instance = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]