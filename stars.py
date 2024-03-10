def stars(arr):
    return list(map(lambda x: x.rjust(len(max(arr, key=len)), "*"), arr))


arr = input().split()
print(*stars(arr), sep="\n")

