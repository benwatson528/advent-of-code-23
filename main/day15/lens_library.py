def solve_p1(init_seq) -> int:
    return sum(hash_algo(seq) for seq in init_seq)


def solve_p2(init_seq) -> int:
    boxes = [[] for _ in range(256)]
    for seq in init_seq:
        if '=' in seq:
            box_num = hash_algo(seq.split('=')[0])
            focal_length = int(seq.split('=')[1])
            found = False

            for i, lens in enumerate(boxes[box_num]):
                if lens[0].split('=')[0] == seq.split('=')[0]:
                    boxes[box_num][i] = (seq, focal_length)
                    found = True
                    break
            if not found:
                boxes[box_num].append((seq, focal_length))
        else:  # - in seq
            box_num = hash_algo(seq[:-1])
            found_i = -1
            for i, lens in enumerate(boxes[box_num]):
                if lens[0].split('=')[0] == seq[:-1]:
                    found_i = i
                    break
            if found_i >= 0:
                boxes[box_num].pop(found_i)

    score = 0
    for box_num, box in enumerate(boxes):
        for lens_position, lens in enumerate(box):
            score += (box_num + 1) * (lens_position + 1) * lens[1]
    return score


def hash_algo(seq):
    current_val = 0
    for c in seq:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    return current_val
