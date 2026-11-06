from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="RS Vježba 1 – Backend (jelovnik)")

# CORS: dopušta frontendu (s druge adrese na Renderu) slanje zahtjeva ovom backendu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class NovoJelo(BaseModel):
    naziv: str
    cijena: float


# "Baza podataka" u memoriji – briše se pri svakom ponovnom pokretanju servera
jelovnik = [
    {"id": 1, "naziv": "Pizza Margherita", "cijena": 9.5},
    {"id": 2, "naziv": "Fuži s tartufima", "cijena": 14.0},
    {"id": 3, "naziv": "Istarska maneštra", "cijena": 7.0},
]


@app.get("/")
def pocetna():
    return {"poruka": "Pozdrav s backenda! Backend radi."}


@app.get("/jelovnik")
def dohvati_jelovnik():
    return jelovnik


@app.get("/jelovnik/{jelo_id}")
def dohvati_jelo(jelo_id: int):
    for jelo in jelovnik:
        if jelo["id"] == jelo_id:
            return jelo
    raise HTTPException(status_code=404, detail="Jelo nije pronađeno")


@app.post("/jelovnik", status_code=201)
def dodaj_jelo(novo: NovoJelo):
    novi_id = max((j["id"] for j in jelovnik), default=0) + 1
    jelo = {"id": novi_id, "naziv": novo.naziv, "cijena": novo.cijena}
    jelovnik.append(jelo)
    return jelo
