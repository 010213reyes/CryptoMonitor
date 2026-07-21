"""Componentes reutilizables de la interfaz."""


"""
Reusable UI components for the Crypto Monitor application.

This module contains all visual components used by the Streamlit
interface. Components must remain free of business logic and
focus exclusively on rendering data.
"""

from __future__ import annotations

from typing import Iterable

import pandas as pd
import streamlit as st

from crypto_monitor.domain.entities import CryptoCurrency


class DashboardComponents:
    """
    Collection of reusable Streamlit UI components.
    """

    @staticmethod
    def render_page_title(title: str, subtitle: str | None = None) -> None:
        """
        Render the page title and optional subtitle.

        Args:
            title: Main page title.
            subtitle: Optional descriptive text.
        """
        st.title(title)

        if subtitle:
            st.caption(subtitle)

    @staticmethod
    def render_error(message: str) -> None:
        """
        Display an error message.

        Args:
            message: Error text.
        """
        st.error(message)

    @staticmethod
    def render_warning(message: str) -> None:
        """
        Display a warning message.

        Args:
            message: Warning text.
        """
        st.warning(message)

    @staticmethod
    def render_info(message: str) -> None:
        """
        Display an informational message.

        Args:
            message: Information text.
        """
        st.info(message)

    @staticmethod
    def render_success(message: str) -> None:
        """
        Display a success message.

        Args:
            message: Success text.
        """
        st.success(message)

    @staticmethod
    def render_loading(message: str = "Loading data..."):
        """
        Display a loading spinner.

        Args:
            message: Loading message.

        Returns:
            Streamlit spinner context manager.
        """
        return st.spinner(message)

    @staticmethod
    def render_metrics(
        total_assets: int,
        average_change: float,
        total_market_cap: float,
        total_volume: float,
    ) -> None:
        """
        Render dashboard metrics.

        Args:
            total_assets: Number of cryptocurrencies.
            average_change: Average 24h variation.
            total_market_cap: Total market capitalization.
            total_volume: Total trading volume.
        """
        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            label="Assets",
            value=f"{total_assets}"
        )

        col2.metric(
            label="Avg 24h Change",
            value=f"{average_change:.2f}%"
        )

        col3.metric(
            label="Market Cap",
            value=f"${total_market_cap:,.0f}"
        )

        col4.metric(
            label="Volume",
            value=f"${total_volume:,.0f}"
        )

    @staticmethod
    def render_crypto_table(
        cryptocurrencies: Iterable[CryptoCurrency]
    ) -> None:
        """
        Render cryptocurrency data table.

        Args:
            cryptocurrencies: Collection of cryptocurrency entities.
        """
        rows = []

        for crypto in cryptocurrencies:
            rows.append(
                {
                    "Name": crypto.name,
                    "Symbol": crypto.symbol.upper(),
                    "Price": f"${crypto.current_price:,.4f}",
                    "24h %": round(crypto.price_change_percentage_24h, 2),
                    "Market Cap": f"${crypto.market_cap:,.0f}",
                    "Volume": f"${crypto.total_volume:,.0f}",
                    "Updated": crypto.last_updated,
                }
            )

        dataframe = pd.DataFrame(rows)

        st.dataframe(
            dataframe,
            use_container_width=True,
            hide_index=True,
        )

    @staticmethod
    def render_empty_state(message: str) -> None:
        """
        Render empty state message.

        Args:
            message: Empty state text.
        """
        st.info(message)

    @staticmethod
    def render_divider() -> None:
        """
        Render a visual divider.
        """
        st.divider()