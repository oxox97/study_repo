# 가능한 것 중, 가장 빨리 끝나는 회의실을 다음에 잡기
# 포인트) 끝나는 시간 같은 경우 시작 시간 빠른 것부터! e.g. (1,2) 다음에 (2,2) (반대는 최대 아님)

N = int(input())
meeting_time = [list(map(int, input().split())) for _ in range(N)]
sorted_meet = sorted(meeting_time, key=lambda x: (x[1], x[0]))  # sorted : key, lambda

def get_meeting_cnt(sorted_mee):
    cnt = 1
    meet = sorted_meet[0]
    #print(meet)
    while True:
        available = [i for i in sorted_meet if i[0] >= meet[1]]  # 끝나는 시간 다음에 시작할 수 있는 미팅 목록
        if not available:
            return cnt
        meet = available[0]
        cnt += 1
        #print(available)

answer = get_meeting_cnt(meeting_time)
print(answer)


# 시간 복잡도 해결 필요
def get_meeting_cnt(meetings):
    # (끝나는 시간, 시작 시간) 기준으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    cnt = 0
    current_end = 0
    for start, end in meetings:
        # 지금 배정할 수 있는 회의라면 배정
        if start >= current_end:
            cnt += 1
            current_end = end
    return cnt

N = int(input())
meeting_time = [list(map(int, input().split())) for _ in range(N)]
answer = get_meeting_cnt(meeting_time)
print(answer)