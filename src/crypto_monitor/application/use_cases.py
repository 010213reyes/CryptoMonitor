"""Casos de uso de la aplicación."""


"""
Casos de uso de la aplicación.

Esta capa coordina la comunicación entre la interfaz
(Streamlit) y la infraestructura (CoinGecko).

La interfaz nunca debe acceder directamente al cliente HTTP.
"""

from __future__ import annotations

from typing import List

from crypto_monitor.domain.entities import Cryptocurrency
from crypto_monitor.infrastructure.coingecko_client import CoinGeckoClient


class CryptoService:
    """
    Servicio principal de la aplicación.

    Contiene los casos de uso disponibles para la interfaz.
    """

    def __init__(
        self,
        client: CoinGeckoClient,
    ) -> None:

        self._client = client

    def get_market(
        self,
        currency: str = "usd",
        limit: int = 20,
    ) -> List[Cryptocurrency]:
        """
        Obtiene las principales criptomonedas del mercado.
        """

        return self._client.get_market(
            currency=currency,
            per_page=limit,
        )

    def search_coin(
        self,
        coin_id: str,
        currency: str = "usd",
    ) -> Cryptocurrency:
        """
        Busca una criptomoneda por su identificador.
        """

        return self._client.get_coin(
            coin_id=coin_id.lower().strip(),
            currency=currency,
        )

    def top_gainers(
        self,
        limit: int = 10,
    ) -> List[Cryptocurrency]:
        """
        Devuelve las criptomonedas con mayor crecimiento.
        """

        market = self.get_market(limit=100)

        market.sort(
            key=lambda coin: coin.price_change_percentage_24h,
            reverse=True,
        )

        return market[:limit]

    def top_losers(
        self,
        limit: int = 10,
    ) -> List[Cryptocurrency]:
        """
        Devuelve las criptomonedas con peor rendimiento.
        """

        market = self.get_market(limit=100)

        market.sort(
            key=lambda coin: coin.price_change_percentage_24h,
        )

        return market[:limit]

    def filter_by_market_cap(
        self,
        minimum: float,
    ) -> List[Cryptocurrency]:
        """
        Filtra criptomonedas por capitalización.
        """

        market = self.get_market(limit=100)

        return [
            coin
            for coin in market
            if coin.market_cap >= minimum
        ]