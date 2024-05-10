def solution(phone_book):
    phone_book.sort()
    answer = True
    
    for i in range(0, len(phone_book)):
        j = i+1
        if (j<len(phone_book) and phone_book[j].find(phone_book[i])==0):
            answer = False 
            break
    return answer