import asyncio
import os
import time

from map_reduce import shuffle, reduce, map_async

async def main():
    lines: list[list[str]] = []
    path = os.path.join(os.path.dirname(__file__), "data", "pg2701.txt")
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            lines.append(line.lower())
            
    lists = await asyncio.gather(*[map_async(line) for line in lines])
    results = []
    for list in lists:
        results.extend(list)
    
    shuffled = shuffle(results)
    reduced = {}

    for k in shuffled.keys():
        reduced[k] = reduce(shuffled[k])
    print(reduced['the'])

if __name__ == "__main__":
    start = time.time()
    
    asyncio.run(main())
    print("Total time:", time.time() - start)
    