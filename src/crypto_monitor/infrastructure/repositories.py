"""Implementaciones concretas de repositorios."""

"""
Repositorio que implementa el acceso a datos utilizando CoinGecko.
"""

from __future__ import annotations

from typing import Any

from crypto_monitor.domain.entities import CryptoCurrency
from crypto_monitor.domain.ports import CryptoRepository
from crypto_monitor.infrastructure.coingecko_client import CoinGeckoClient


class CoinGeckoRepository(CryptoRepository):
    """
    Implementación concreta del repositorio de criptomonedas.

    Obtiene los datos desde CoinGecko y los transforma
    en entidades del dominio.
    """

    def __init__(self, client: CoinGeckoClient) -> None:
        self._client = client

    def get_market_data(self) -> list[CryptoCurrency]:
        """
        Recupera las criptomonedas más importantes.

        Returns
        -------
        list[CryptoCurrency]
        """

        response = self._client.get_markets()

        cryptos: list[CryptoCurrency] = []

        for item in response:
            cryptos.append(
                self._build_entity(item)
            )

        return cryptos

    @staticmethod
    def _build_entity(data: dict[str, Any]) -> CryptoCurrency:
        """
        Convierte un diccionario recibido por la API
        en una entidad del dominio.
        """

        return CryptoCurrency(
            name=data.get("name", ""),
            symbol=data.get("symbol", "").upper(),
            current_price=float(data.get("current_price", 0.0)),
            price_change_percentage_24h=float(
                data.get("price_change_percentage_24h") or 0.0
            ),
            market_cap=float(data.get("market_cap", 0.0)),
            total_volume=float(data.get("total_volume", 0.0)),
            last_updated=data.get("last_updated", ""),
        ) 