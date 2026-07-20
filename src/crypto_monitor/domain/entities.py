"""Entidades y objetos de valor del dominio."""


from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Crypto:
    """
    Representa una criptomoneda.
    """

    id: str
    symbol: str
    name: str


@dataclass(slots=True)
class MarketData:
    """
    Información de mercado de una criptomoneda.
    """

    crypto: Crypto

    current_price: float

    price_change_percentage_24h: float

    market_cap: float

    total_volume: float

    last_updated: datetime