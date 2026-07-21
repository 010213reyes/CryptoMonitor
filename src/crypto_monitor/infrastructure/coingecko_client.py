"""Cliente HTTP para la API de CoinGecko."""

"""
Cliente HTTP para consumir la API pública de CoinGecko.

Esta capa pertenece a infraestructura, por lo tanto es la única
que conoce detalles de HTTP, URLs, requests y JSON.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

import requests

from crypto_monitor.domain.entities import Cryptocurrency


class CoinGeckoClient:
    """
    Cliente para consumir la API pública de CoinGecko.
    """

    BASE_URL = "https://api.coingecko.com/api/v3"

    def __init__(
        self,
        timeout: int = 15,
    ) -> None:

        self._timeout = timeout

        self._session = requests.Session()

        self._session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": "CryptoMonitor/1.0"
            }
        )

    def get_market(
        self,
        currency: str = "usd",
        per_page: int = 20,
        page: int = 1,
    ) -> list[Cryptocurrency]:
        """
        Obtiene el listado de criptomonedas.
        """

        endpoint = f"{self.BASE_URL}/coins/markets"

        params = {
            "vs_currency": currency,
            "order": "market_cap_desc",
            "per_page": per_page,
            "page": page,
            "sparkline": "false"
        }

        response = self._session.get(
            endpoint,
            params=params,
            timeout=self._timeout,
        )

        response.raise_for_status()

        payload = response.json()

        return [
            self._to_entity(item)
            for item in payload
        ]

    def get_coin(
        self,
        coin_id: str,
        currency: str = "usd",
    ) -> Cryptocurrency:
        """
        Devuelve una sola criptomoneda.
        """

        endpoint = f"{self.BASE_URL}/coins/markets"

        params = {
            "vs_currency": currency,
            "ids": coin_id,
            "sparkline": "false"
        }

        response = self._session.get(
            endpoint,
            params=params,
            timeout=self._timeout,
        )

        response.raise_for_status()

        payload = response.json()

        if not payload:
            raise ValueError(
                f"No existe la criptomoneda '{coin_id}'."
            )

        return self._to_entity(payload[0])

    @staticmethod
    def _to_entity(
        data: dict[str, Any]
    ) -> Cryptocurrency:
        """
        Convierte un diccionario JSON en una entidad.
        """

        return Cryptocurrency(

            id=data["id"],

            symbol=data["symbol"],

            name=data["name"],

            current_price=float(data["current_price"]),

            price_change_percentage_24h=float(
                data.get(
                    "price_change_percentage_24h",
                    0.0,
                )
            ),

            market_cap=float(data["market_cap"]),

            total_volume=float(data["total_volume"]),

            last_updated=datetime.fromisoformat(
                data["last_updated"].replace("Z", "+00:00")
            ),
        )