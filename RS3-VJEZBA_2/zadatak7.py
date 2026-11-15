"""
korak po korak:
    asyncio.run() kreira event loop i pokrece main() funkciju
 
1. RASPOREDJIVANJE: U main() se s asyncio.create_task() stvaraju 3 Task objekta (Timer 1, 2 i 3).
   Oni se samo predaju event loop-u i stanje je PENDING. Još se ništa ne ispisuje. main() dolazi do await asyncio.gather(*timers):
   main() se SUSPENDIRA jer čeka da sva 3 taska završe i prepušta kontrolu event loop-u.

2. IZVRSAVANJE: Event loop pokreće taskove redom kojim su raspoređeni:
   - Timer 1 - RUNNING, ispiše se, dođe do await sleep(1) - SUSPENDED
   - Timer 2 - RUNNING, ispiše se, dođe do await sleep(1) - SUSPENDED
   - Timer 3 - RUNNING, ispiše se, dođe do await sleep(1) -  SUSPENDED
   Sva tri sada čekaju ISTOVREMENO, a event loop nema što raditi pa čeka 1 sekundu.

   U Sek. 1 i 2: Nakon 1 sek. sva tri se "probude" -RUNNING, svaki ispiše novu poruku
   i ponovno dođe do sleep(1) - SUSPENDED. Ovo se ponavlja svake sekunde.

   U sek. 3: Timer 1 izađe iz petlje, ispiše "Vrijeme je isteklo!" -DONE.
   Timer 2 i Timer 3 nastavljaju (ispišu poruku, pa SUSPENDED).
   
   U Sek. 5: Timer 2 ispiše "Vrijeme je isteklo!" -DONE. Ostao je samo Timer 3.
   U Sek. 7: Timer 3 ispiše "Vrijeme je isteklo!" -DONE.


3. DOVRSAVANJE: Sva 3 taska su DONE, asyncio.gather() je gotov i main() se nastavlja i zavrsava. 
asyncio.run() zavrsava event loop i oslobadja resurse.

ZAKLJUCAK: program se izvrsava 7 sekundi, jer se timeri izvrsavaju paralelno, a najduzi timer traje 7 sekundi.
Tajmeri se cekaju istovremen. Dok jedan task ceka na await, event loop izvrsava druge taskove.
"""
import asyncio


async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')


async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)


asyncio.run(main())
