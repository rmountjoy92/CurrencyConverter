import unittest
from app import currency_converter


class TestCurrencyConverter(unittest.TestCase):
    def test_get_symbols(self):
        # make sure symbols are a list
        self.assertTrue(isinstance(currency_converter.symbols, list))
        # make sure each list item is a string
        for symbol in currency_converter.symbols:
            self.assertTrue(isinstance(symbol, str))

    def test_convert_currency(self):
        # mock user input
        base_currency = "USD"
        target_currency = "CAD"
        currency_amount = 5000

        # run the conversion
        converted_currency_amount = currency_converter.convert_currency(
            base_currency, target_currency, currency_amount
        )
        # verify converted amounted is correct
        self.assertTrue(
            converted_currency_amount
            == "{:.2f}".format(currency_amount * currency_converter.rate.get("CAD"))
        )
