import unittest
from . import CurrencyConverter


class TestCurrencyConverter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # initialize the converter
        cls.currency_converter = CurrencyConverter()

    def test_get_symbols(self):
        # get symbols
        symbols = self.currency_converter.get_symbols()
        # make sure symbols are a list
        self.assertTrue(isinstance(symbols, list))
        # make sure each list item is a string
        for symbol in symbols:
            self.assertTrue(isinstance(symbol, str))

    def test_convert_currency(self):
        # mock user input
        base_currency = "USD"
        target_currency = "CAD"
        currency_amount = 5000

        # run the conversion
        converted_currency_amount = self.currency_converter.convert_currency(
            base_currency, target_currency, currency_amount
        )
        # verify converted amounted is correct
        self.assertTrue(
            converted_currency_amount
            == "{:.2f}".format(
                currency_amount * self.currency_converter.rate.get("CAD")
            )
        )
