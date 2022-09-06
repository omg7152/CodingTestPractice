templist = [10, 20, 30]
print(templist)
print(templist.index(20)) # 해당값 인덱스 찾기

templist.append(40) # 리스트 뒤에 해당값 추가
print(templist)

templist.insert(1, 50) # 해당값의 특정 인덱스에 추가(원래 그자리에 있던 값은 한칸씩 밀려남)
print(templist)

templist.pop() # 제일 뒤에있는 값 하나 제거
print(templist)

templist.append(20)
print(templist.count(20)) # 리스트 내에 해당 값이 몇개 있는지

templist2 = [50, 40, 30, 20, 10] 
templist2.sort() # 리스트 정렬
print(templist2) 

templist2.reverse() # 리스트 순서 뒤집기
print(templist2) 

templist2.clear() # 리스트 초기화
print(templist2)

templist3 = ["Apple", 20, True] # 다양한 자료형도 가능
print(templist3)

templist4 = ["Banana", 30, False]
templist3.extend(templist4) #리스트 확장
print(templist3)


