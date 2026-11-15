import asyncio

async def secure_data(podaci):  
    await asyncio.sleep(3)
    return {
        "prezime": podaci["prezime"],
        "broj_kartice": hash(podaci["broj_kartice"]),
        "CVV": hash(podaci["CVV"])
    }

async def main():
    osjetljivi_podaci = [
        {"prezime": "Peric", "broj_kartice": "1234-5678-9012-3456","CVV": "123"},
        {"prezime": "Ivic", "broj_kartice": "9876-5432-1098-7654","CVV": "456"},
        {"prezime": "Horvat", "broj_kartice": "1111-2222-3333-4444","CVV": "789"}
    ]
    
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)       
    for rezultat in rezultati:  
        print(rezultat) 

asyncio.run(main())

