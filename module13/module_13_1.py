import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament(participants):
    for task in [asyncio.create_task(start_strongman(name, power)) for name, power in participants.items()]:
        await task


asyncio.run(start_tournament({'Pasha': 3, 'Denis': 4, 'Apollon': 5}))
