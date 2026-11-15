import asyncio, time 

async def fetch_data(param):  
    print(f"Nesto radim s {param}...")
    await asyncio.sleep(param) 
    print(f"Dovrsio sam s {param}.")
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Fetch 1 uspjesno zavrsio.")
    await asyncio.sleep(1) # dajemo event loop-u vremena da dovrsi task2 
    return [result1]

t1 = time.perf_counter()
results = asyncio.run(main())
t2 = time.perf_counter()    
print(results)
print(f"Vrijeme izvrsavanja: {t2 - t1: .2f} sekundi.")