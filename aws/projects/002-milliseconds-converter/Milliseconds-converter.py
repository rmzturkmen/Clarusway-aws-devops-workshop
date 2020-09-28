# Milliseconds Converter Application (Python Flask)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def converter_get():
    return render_template("index.html", developer_name="Ramazan", not_valid=False)


@app.route("/", methods=["POST"])
def converter_post():
    num = request.form["number"]
    
    if num.isalpha():
        return render_template("index.html", developer_name="Ramazan", not_valid="not_valid")
        
    elif num.isnumeric():
        numalpha = int(num)
        
        if numalpha < 1:
            return render_template("index.html", developer_name="Ramazan", not_valid="not_valid")
            
        
        elif numalpha >0:
            hour = numalpha // (1000*60*60)
            minute = (numalpha - hour * (1000*60*60)) // (1000*60)
            sec = (numalpha - hour * (1000*60*60) - minute * (1000*60)) // (1000)
            result = (f'{hour} hour/s'*(hour != 0) + f' {minute} minute/s'*(minute != 0) +
                  f' {sec} second/s' * (sec != 0) or f'just {num} millisecond/s' * (numalpha < 1000))
            return render_template("result.html", developer_name="Ramazan", milliseconds=numalpha, not_valid=True, result=result)
    

if __name__ == "__main__":
      #app.run(debug=True)
      app.run(host='0.0.0.0', port=80)
