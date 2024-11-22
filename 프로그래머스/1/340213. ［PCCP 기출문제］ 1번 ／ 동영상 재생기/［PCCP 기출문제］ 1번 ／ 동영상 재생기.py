def solution(video_len, pos, op_start, op_end, commands):
    # 시간 문자열을 초 단위로 변환
    def to_seconds(mm_ss):
        mm, ss = map(int, mm_ss.split(":"))
        return mm * 60 + ss

    # 초를 MM:SS 형식의 문자열로 변환
    def to_mmss(seconds):
        mm = seconds // 60
        ss = seconds % 60
        return f"{mm:02d}:{ss:02d}"

    # 입력값들을 초 단위로 변환
    video_length = to_seconds(video_len)
    current_pos = to_seconds(pos)
    opening_start = to_seconds(op_start)
    opening_end = to_seconds(op_end)

    for command in commands:
        # 오프닝 구간 건너뛰기
        if opening_start <= current_pos < opening_end:
            current_pos = opening_end
        if command == "prev":
            # 10초 전 이동, 시작점 아래로 내려가지 않도록 처리
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            # 10초 후 이동, 동영상 길이를 초과하지 않도록 처리
            current_pos = min(video_length, current_pos + 10)
        # 오프닝 구간 건너뛰기
        if opening_start <= current_pos < opening_end:
            current_pos = opening_end

    # 결과를 MM:SS 형식으로 변환하여 반환
    return to_mmss(current_pos)
