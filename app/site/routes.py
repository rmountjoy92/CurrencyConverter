from flask import render_template, request, jsonify
from app import currency_converter
from . import site


@site.route("/", methods=["GET"])
def index():
    if currency_converter.error:
        return currency_converter.error, 500
    return render_template("index.html", symbols=currency_converter.symbols)


@site.route("/convert_currency", methods=["POST"])
def convert_currency():
    try:
        currency_amount = float(request.form.get("currency_amount"))
    except ValueError:
        return jsonify(data={"error": "Currency amount must be a number."})

    converted_currency_amount = currency_converter.convert_currency(
        request.form.get("base_currency"),
        request.form.get("target_currency"),
        currency_amount,
    )
    if currency_converter.error:
        resp = jsonify(data={"error": currency_converter.error})
        currency_converter.error = None
        return resp
    else:
        return jsonify(
            data={
                "result": (
                    f"Result: {converted_currency_amount} "
                    f"{request.form.get('target_currency')}"
                )
            }
        )
