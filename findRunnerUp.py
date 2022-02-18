n = int(input())
arr = map(int, input().split())

arr = sorted(list(dict.fromkeys(arr)), reverse=True)
print(arr[1])

arr = sorted(set(arr), reverse=True)
print(arr[1])

print(sorted(set(arr))[-2])
#get the last second item

print("The list of numbers: {}".format(' '.join(str(arr))))