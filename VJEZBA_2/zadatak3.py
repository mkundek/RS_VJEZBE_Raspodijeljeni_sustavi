import asyncio

baza_korisnika =[
    {"korisnicko_ime": "mirko123", "email": "mirko123@gmail.com"},
    {"korisnicko_ime": "ana_anic", "email": "aanic@gmail.com"},
    {"korisnicko_ime": "maja_0x", "email": "majaaaaa@gmail.com"},
    {"korisnicko_ime": "zdeslav032", "email": "deso032@gmail.com"}
]
baza_lozinka =[
    {"korisnicko_ime": "mirko123","lozinka": "lozinka123"},
    {"korisnicko_ime": "ana_anic", "lozinka": "super_teska_lozinka "},
    {"korisnicko_ime": "maja_0x", "lozinka": "s324SDFfdsj234"},
    {"korisnicko_ime": "zdeslav032", "lozinka": "deso123"}
]
async def autorizacija (korisnik_iz_baze, lozinka):
    await asyncio.sleep(2)
    ime = korisnik_iz_baze["korisnicko_ime"]
    for zapis in baza_lozinka:
        if zapis["korisnicko_ime"] == ime and zapis["lozinka"] == lozinka:
            return f'Korisnik {ime} : Autorizacija uspješna!'
    return f'Korisnik {ime} : Autorizacija neuspješna!'

async def autentikacija(korisnik):
    await asyncio.sleep(3)
    for korisnik_iz_baza in baza_korisnika:
        if korisnik_iz_baza["korisnicko_ime"] == korisnik["korisnicko_ime"] and korisnik_iz_baza["email"] == korisnik["email"]:
            return await autorizacija(korisnik_iz_baza, korisnik["lozinka"])
    return f'Korisnik {korisnik["korisnicko_ime"]} : korisnik nije pronadjen!'

async def main():
    korisnik = {
        "korisnicko_ime": "pero",
        "email": "pero@gmail.com",
        "lozinka": "nesto"

       # "korisnicko_ime": "mirko123", 
       # "email": "mirko123@gmail.com",
       # "lozinka": "lozinka123"
    }
    rezultat = await autentikacija(korisnik) 
    print(rezultat)

asyncio.run(main())