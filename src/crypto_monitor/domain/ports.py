"""Contratos del dominio para el acceso a datos."""


from abc import ABC
from abc import abstractmethod

from .entities import MarketData


class CryptoRepository(ABC):
    """
    Contrato para cualquier fuente de datos de criptomonedas.
    """

    @abstractmethod
    def get_market_data(
        self,
        crypto_id: str,
    ) -> MarketData:
        """
        Obtiene la información de mercado de una criptomoneda.
        """
        raise NotImplementedError