from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def converter_get():
    return render_template("index.html", developer_name="Ramazan")


@app.route("/", methods=["POST"])
def converter_post():
    num = request.form["number"]
    if not num.isdecimal():
        return render_template("index.html", developer_name="Ramazan", not_valid="not_valid")

    elif not 0 < int(num) < 4000:
        return render_template("index.html", developer_name="Ramazan", not_valid="not_valid")

    else:
        numalpha = int(num)

        def convert(numalpha):
            roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                     50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
            num_roman = ""
            for i in roman.keys():
                num_roman += roman[i] * (numalpha//i)
                numalpha %= i
            return num_roman

    return render_template("result.html", developer_name="Ramazan", number_decimal=numalpha, number_roman=convert(numalpha))


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
