from flask import Flask, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("invitados.csv")

@app.route("/")
def home():
    return "Sistema RSVP funcionando"

@app.route("/rsvp")
def rsvp():

    guest_id = int(request.args.get("id"))

    guest = data[data["id"] == guest_id].iloc[0]

    nombre = guest["nombre"]

    return f"""
    <h1>Hola {nombre}</h1>

    <p>¿Confirmas tu asistencia?</p>

    <a href="/confirmar?id={guest_id}&resp=si">Sí asistiré</a><br><br>

    <a href="/confirmar?id={guest_id}&resp=no">No podré asistir</a>
    """

@app.route("/confirmar")
def confirmar():

    guest_id = int(request.args.get("id"))
    resp = request.args.get("resp")

    guest = data[data["id"] == guest_id].iloc[0]

    if resp == "si":

        return f"""
        <h1>Gracias por confirmar 🎉</h1>

        <p>Dirección del evento:</p>
        <p>Salón Magnolia</p>

        <p>Tu mesa:</p>
        <h2>Mesa {guest["mesa"]}</h2>
        """

    else:

        return """
        <h1>Gracias por avisarnos</h1>
        <p>Esperamos verte pronto.</p>
        """

app.run(host="0.0.0.0", port=10000)
