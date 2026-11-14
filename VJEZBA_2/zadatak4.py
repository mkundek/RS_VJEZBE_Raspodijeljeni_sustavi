import asyncio
async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f'Broj {broj} je paran.'
    else:
        return f'Broj {broj} je neparan.'

async def main():
  brojevi = [broj for broj in range(1, 11)]
  print("Brojevi:", brojevi)

  zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in brojevi]

  rezultati = await asyncio.gather(*zadaci)
  for rezultat in rezultati:
    print(rezultat)

asyncio.run(main())