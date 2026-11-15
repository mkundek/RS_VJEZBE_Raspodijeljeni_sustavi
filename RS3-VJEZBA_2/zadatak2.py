import asyncio

async def dohvati_korisnike():
    await asyncio.sleep(3)  
    korisnici = [
       {"id": 1, "ime": "Ana", "email": "ana@nesto.com"},
       {"id": 2, "ime": "Marko", "email": "marko@nesto.com"},
       {"id": 3, "ime": "Ivana", "email": "ivana@nesto.com"},
   ]
    print("Dohvaćeni korisnici:")
    return korisnici

async def dohvati_proizvode():
    await asyncio.sleep(5)  
    proizvodi = [
        {"id": 101, "naziv": "Laptop", "cijena": 899.99},
        {"id": 102, "naziv": "Tablet", "cijena": 599.99},
        {"id": 103, "naziv": "Telefon", "cijena": 29.99},
    ]
    print("Dohvaćeni proizvodi:")
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnike(), dohvati_proizvode())
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)

asyncio.run(main())