from flask_restx import Resource, reqparse
from app import restx
from app.currency_converter import CurrencyConverter

currency_converter_api = restx.namespace(
    "currency_converter", "All API routes related to converting currency"
)


# ----------------
# /symbols
# ----------------
@currency_converter_api.route("/symbols")
@currency_converter_api.doc(
    description="Get symbols for all supported base currencies.",
    responses={200: "(json list) Supported currency symbols", 500: "Error"},
)
class Symbols(Resource):
    def get(self):
        converter = CurrencyConverter()
        symbols = converter.get_symbols()
        if converter.error:
            return {"error": converter.error}, 500
        return symbols


# ----------------
# /convert_currency
# ----------------
convert_currency_parser = reqparse.RequestParser()
convert_currency_parser.add_argument(
    "base_currency",
    required=True,
    type=str,
    help=(
        "The currency symbol for the currency to be converted from. "
        "See /currency_converter/symbols endpoint for symbol options"
    ),
)
convert_currency_parser.add_argument(
    "target_currency",
    required=True,
    type=str,
    help=(
        "The currency symbol for the currency to be converted to. "
        "See /currency_converter/symbols endpoint for symbol options"
    ),
)
convert_currency_parser.add_argument(
    "currency_amount", required=True, type=int, help="the currency amount to convert"
)


@currency_converter_api.route("/convert_currency")
@currency_converter_api.expect(convert_currency_parser)
@currency_converter_api.doc(
    description=(
        "Convert a currency amount by supplying a base currency, "
        "target currency and amount"
    ),
    responses={200: "(int) converted currency amount", 500: "Error"},
)
class ConvertCurrency(Resource):
    def post(self):
        args = convert_currency_parser.parse_args()
        converter = CurrencyConverter()
        converted_currency_amount = converter.convert_currency(
            args.get("base_currency").upper(),
            args.get("target_currency").upper(),
            args.get("currency_amount"),
        )
        if converter.error:
            return {"error": converter.error}, 500
        return converted_currency_amount
