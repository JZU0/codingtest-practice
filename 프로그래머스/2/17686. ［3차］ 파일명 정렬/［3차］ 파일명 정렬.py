def split_file(file):
    head = ""
    number = ""
    tail = ""
    i = 0

    while i < len(file) and not file[i].isdigit():
        head += file[i]
        i += 1

    while i < len(file) and file[i].isdigit():
        number += file[i]
        i += 1

    tail = file[i:]

    return head, number, tail

def solution(files):
    sorted_files = sorted(
        files,
        key=lambda x: (split_file(x)[0].lower(), int(split_file(x)[1]))
    )
    return sorted_files

