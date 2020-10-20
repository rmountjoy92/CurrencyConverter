from flask import render_template, request, jsonify
from app.currency_converter import CurrencyConverter
from . import site


@site.route("/", methods=["GET"])
def index():
    converter = CurrencyConverter()
    symbols = converter.get_symbols()
    if converter.error:
        return converter.error, 500
    return render_template("index.html", symbols=symbols)


@site.route("/convert_currency", methods=["POST"])
def convert_currency():
    try:
        currency_amount = float(request.form.get("currency_amount"))
    except ValueError:
        return jsonify(data={"error": "Currency amount must be a number."})

    converter = CurrencyConverter()
    converted_currency_amount = converter.convert_currency(
        request.form.get("base_currency"),
        request.form.get("target_currency"),
        currency_amount,
    )
    if converter.error:
        return jsonify(data={"error": converter.error})
    else:
        return jsonify(
            data={
                "result": (
                    f"Result: {converted_currency_amount} "
                    f"{request.form.get('target_currency')}"
                )
            }
        )
