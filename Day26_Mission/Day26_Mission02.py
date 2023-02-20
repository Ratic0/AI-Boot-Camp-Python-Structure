import random
count1, count2 = 0, 0

def seq_search(ary, f_data):
    pos = -1
    global count1
    for i in range(len(ary)):
        count1 += 1
        if ary[i] == f_data:
            pos = i
            break
    return pos

def bin_search(ary, f_data): ##이건 정렬된 데이터 오름차순
    global count2
    start = 0
    end = len(ary) - 1
    while start <= end:
        count2 += 1
        mid = (start+end)//2
        if ary[mid] == f_data:
            return mid
        elif ary[mid] < f_data:
            start = mid + 1
        else:
            end = mid - 1
    return -1

raw_array = [random.randint(0, 999999) for _ in range (1000000)]
sort_array = sorted(raw_array)
print(f"비정렬 배열(100만개) --> {raw_array[0:5:1]} ~~~~ {raw_array[len(raw_array)-6:-1]}")
print(f"정렬 배열(100만개) --> {sort_array[0:5:1]} ~~~~ {sort_array[len(raw_array)-6:-1]}")

seq_search(raw_array, 9999)
print(f"순차 검색(비정렬 데이터) --> {count1}회")
bin_search(sort_array, 9999)
print(f"이진 검색(정렬 데이터) --> {count2}회")