from abc import ABC, abstractmethod

class SymbolMap(ABC):
    """Отображение «символ->something»"""

    @abstractmethod
    def at(self, symbol: str):
        """Получение значения (образа) по символу (прообразу)."""
        raise NotImplementedError

    @abstractmethod
    def items(self):
        """Получить контейнер, содержащий все пары вида (символ, значение)
        из отображения.
        """
        raise NotImplementedError

    @abstractmethod
    def values(self):
        """Все значения (образы) в отображении."""
        raise NotImplementedError

    @abstractmethod
    def keys(self):
        """Все символы, являющиеся прообразами некоторого образа."""
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        """Получить количество прообразов в отображении."""
        raise NotImplementedError
