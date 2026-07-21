"""
Entidades del dominio.

Este módulo contiene únicamente modelos de negocio.
No debe depender de Streamlit, requests ni de ninguna
librería externa de infraestructura.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Cryptocurrency:
    """
    Representa una criptomoneda obtenida desde el proveedor
    de datos.

    Attributes
    ----------
    id:
        Identificador interno utilizado por CoinGecko.

    symbol:
        Símbolo de la criptomoneda.

    name:
        Nombre completo.

    current_price:
        Precio actual en USD.

    price_change_percentage_24h:
        Variación porcentual en las últimas 24 horas.

    market_cap:
        Capitalización de mercado.

    total_volume:
        Volumen negociado.

    last_updated:
        Fecha y hora de la última actualización.
    """

    id: str

    symbol: str

    name: str

    current_price: float

    price_change_percentage_24h: float

    market_cap: float

    total_volume: float

    last_updated: datetime

    @property
    def is_positive(self) -> bool:
        """
        Indica si la variación de precio es positiva.
        """
        return self.price_change_percentage_24h >= 0

    @property
    def formatted_symbol(self) -> str:
        """
        Devuelve el símbolo en mayúsculas.
        """
        return self.symbol.upper()

    @property
    def formatted_price(self) -> str:
        """
        Devuelve el precio con formato monetario.
        """
        return f"${self.current_price:,.2f}"

    @property
    def formatted_market_cap(self) -> str:
        """
        Capitalización de mercado legible.
        """
        return f"${self.market_cap:,.0f}"

    @property
    def formatted_volume(self) -> str:
        """
        Volumen negociado legible.
        """
        return f"${self.total_volume:,.0f}"

    @property
    def formatted_change(self) -> str:
        """
        Variación porcentual con signo.
        """
        return f"{self.price_change_percentage_24h:+.2f}%"

    @property
    def formatted_last_updated(self) -> str:
        """
        Fecha de actualización legible.
        """
        return self.last_updated.strftime("%Y-%m-%d %H:%M:%S")