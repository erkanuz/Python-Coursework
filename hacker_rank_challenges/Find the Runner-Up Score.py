if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()), reverse=True)
print(arr[arr.count(arr[0])])
