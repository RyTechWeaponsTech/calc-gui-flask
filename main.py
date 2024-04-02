from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    def addition(n1, n2):
        return n1 + n2

    def substraction(n1, n2):
        return n1 - n2

    def multiplier(n1, n2):
        return n1 * n2

    def division(n1, n2):
        return n1 / n2

    def floor_division(n1, n2):
        return n1 // n2

    def modulus(n1, n2):
        return n1 % n2

    def sqrt(n1):
        return n1 ** (1/2)

    def cube_root(n1):
        return n1 ** (1/3)

    if request.method == "POST":

        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "addition":
            result = addition(num1, num2)
        elif operation == "substract":
            result = substraction(num1, num2)
        elif operation == "multiplier":
            result = multiplier(num1, num2)
        elif operation == "division":
            if num2 != 0:
                result = division(num1, num2)
            else:
                result = "Syntax Error"
        elif operation == "floor_division":
            if num2 != 0:
                result = floor_division(num1, num2)
            else:
                result = "Syntax Error"
        elif operation == "modulus":
            if num2 != 0:
                result = modulus(num1, num2)
            else:
                result = "Syntax Error"
        elif operation == "sqrt":
            result = sqrt(num1)
        elif operation == "cube_root":
            result = cube_root(num1)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
