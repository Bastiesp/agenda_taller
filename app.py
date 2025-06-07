from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print("Se accedió a la ruta '/'")
    if request.method == "POST":
        database.insertar_cita(
            request.form["cliente"],
            request.form["vehiculo"],
            request.form["matricula"],
            request.form["telefono"],
            request.form["servicio"],
            request.form["fecha_cita"],
            request.form["proximo_servicio"]
        )
        return redirect(url_for("index"))
    return render_template("index.html")

if __name__ == "__main__":
    print("Ejecutando servidor Flask...")
    database.create_table()
    app.run(debug=True)