# 컨셉 못 잡았음
# 이분 탐색 -> 최소 블루레이 크기 X를 찾아야 하고, 이것을 1씩 올리는 것보다 절반씩 줄여가는 게 훨씬 빠르기 O(logN) 때문 (브루트포스 (O(N))는 너무 오래 걸림)
# 떠올리기 어렵다, 심지어 left, right가 index도 아님 ㅠ

# 실버1이지만 일단 패스하고 진도

N, M = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]

def binary_search(lst, left, right):

    while left <= right:

        median = (left + right) // 2
        
        sum_lesson = 0
        sum_lesson_list = []
        lesson_list = []
        lesson_tmp = []
        for lesson in lst:
            sum_lesson += lesson
            lesson_tmp.append(lesson)
            if sum_lesson >= median:
                sum_lesson_list.append(sum_lesson)
                sum_lesson = 0
                lesson_list.append(lesson_tmp)
                lesson_tmp = []
        if lesson_tmp:
            lesson_list.append(lesson_tmp)
        
        print(f"\nMEDIAN : {median}")
        print(f"LESSON_LIST : {lesson_list}")
        print(f"LESSON_SUM : {[sum(lessons) for lessons in lesson_list]}")

        if len(sum_lesson_list) == M:
            print("correct!")
            return median
        elif len(sum_lesson_list) > M:
            print(f"> median {median} is too small.")
            left = median + 1
        else:
            right = median - 1

binary_search(lst, max(lst), sum(lst))