import logging
from requests import get, exceptions


class CurrencyConverter:
    def __init__(self):
        """
        The currency converter. Responsible for providing the symbols of supported
        currencies, and calculating currency conversions. This class uses the API
        documented at: http://exchangeratesapi.io/
        """
        self.error = None
        self.symbols = None
        self.rate = None
        self.base_url = "https://api.exchangeratesapi.io/latest"

    def get_symbols(self):
        """
        This method retrieves the symbols for all supported currencies, e.g. for the
        US dollar currency, the symbol retrieved is 'USD', and saves them as an
        alphabetized list.

        :return symbols: (list<string>) The symbols returned from the API
        """
        try:
            resp = get(self.base_url).json()
        except exceptions.RequestException:
            logging.error(
                f"Failed to retrieve symbols from {self.base_url}", exc_info=True
            )
            self.error = f"Failed to retrieve symbols from {self.base_url}!"
            return

        symbols = sorted([symbol for symbol, rate in resp["rates"].items()])
        logging.info(f"Symbols collected from {self.base_url}")
        return symbols

    def convert_currency(self, base_currency, target_currency, currency_amount):
        """
        This method calculates a currency conversion, given the currency symbol you
        want to convert from, the currency symbol you are converting to,
        and the currency amount. It returns a decimal to the hundredths place.

        :param base_currency: (str) Symbol for the currency to convert from. e.g. USD
        :param target_currency: (str) Symbol for the currency to convert to. e.g. USD
        :param currency_amount: (float) Currency amount, accepts numbers with decimals,
         or without.

        :return converted_currency_amount: (float) Calculated result,
        with double padded 0
        """
        try:
            self.rate = get(
                f"{self.base_url}?base={base_currency}&symbols={target_currency}"
            ).json()["rates"]
            logging.info(f"Rates collected from {self.base_url}")

        except exceptions.RequestException:
            logging.error(
                f"Failed to retrieve rates from {self.base_url}", exc_info=True
            )
            self.error = f"Failed to retrieve rates from {self.base_url}!"

        converted_currency_amount = currency_amount * self.rate[target_currency]
        logging.info(
            f"Converted {currency_amount} {base_currency} to {target_currency}. "
            f"Result was: {converted_currency_amount}"
        )
        return "{:.2f}".format(converted_currency_amount)
