import asyncio
import re
from collections import defaultdict


def map(line: list[str]) -> list[tuple[str, int]]:
    result = []
    words = line.split(" ")
    for word in words:
        word = re.sub(r'[^a-zA-Z]', '', word)

        if not word:
            continue
        result.append((word, 1))
    return result


async def map_async(li: list[str]):
    return await asyncio.to_thread(map, li)

def shuffle(lines: list[tuple[str, int]]) -> dict[str, list[int]]:
    data: dict[str, list[int]] = defaultdict(list)
    for word, _ in lines:
        data[word].append(1)
    return data


def reduce(collection: list[int]) -> int:
    return len(collection)
