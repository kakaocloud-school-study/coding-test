from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    res: int = 0
    for i in range(len(cities)):
        city = cities[i].lower()
        if city in cache:
            res += 1
            cache.remove(city)
            cache.append(city)
        else:
            res += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
    return res
            