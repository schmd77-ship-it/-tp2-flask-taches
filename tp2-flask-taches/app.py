from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [
    {"id": 1, "nom": "Tantely Sch", "email": "schmd77@gmail.com"},
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        email = request.form.get("email", "").strip()

        if nom and email:
            new_id = max((student["id"] for student in students), default=0) + 1
            students.append({"id": new_id, "nom": nom, "email": email})

        return redirect(url_for("index"))

    return render_template("index.html", students=students)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_student(id):
    global students
    students = [student for student in students if student["id"] != id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
