from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        file_name = request.form.get("file_name")
        context = request.form.get("context")

        with open(f"files/{file_name}.txt", "w") as f:
            f.write(context)

        return render_template("created.html", file_name=file_name)
        
    return render_template("main.html", title="DOP`ы")


@app.route("/all")
def all_files():
    files_lst = os.listdir("./files")

    return render_template('all.html', files=files_lst)


@app.route("/file/<path:file_name>")
def file_card(file_name):
    # Добавьте расширение .txt к file_name, если оно не включено в URL
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    path = f"./files/{file_name}"
    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "Файл не найден"
    return render_template('file_card.html', content=content, file_name=file_name)


