import random

def bin_search(ary, f_data) :
    start = 0
    end = len(ary)-1
    while start <= end:
        mid = (end+start)//2
        if f_data == ary[mid]: ##걸릴때까지 계속 체크
            return mid
        elif f_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


data_array = ['코카콜라','츄파츕스', '도시락', '삼각김밥', '레쓰비캔커피', '바나나맛우유']
item_array = [random.choice(data_array) for i in range(20)]
sort_array = sorted(item_array)
set_array = set(sort_array)

print(f"#오늘 판매된 전체 물건(중복O, 정렬X)--> {item_array}")
print(f"#오늘 판매된 전체 물건(중복O, 정렬O)--> {sort_array}")
print(f"#오늘 판매된 물품 종류(중복x) --> {set_array}")

print_list = []
for product in set_array:
    count = 0
    p = 0

    while p != -1:
        p = bin_search(sort_array, product) # 찾았으면 index 리턴, 아니면 -1 리턴
        if p != -1 :
            count += 1
            del(sort_array[p])
    print_list.append([count, product])

print()
print(f"결산 결과 ==> {print_list}")



