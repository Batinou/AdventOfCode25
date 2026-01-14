from pathlib import Path


p = Path("Jour5\\input.txt")
lines = [line.strip() for line in p.read_text(encoding="utf-8").splitlines()]
sep_idx = lines.index("")


range_lines = lines[:sep_idx]
id_lines = lines[sep_idx+1:]


ranges = []
for i, raw in enumerate(range_lines, start=1):
    parts = raw.split("-")
    start = int(parts[0].strip())
    end = int(parts[1].strip())
    ranges.append((start,end))


ids = []
for i in id_lines:
    ids.append(int(i))


def merge_ranges(rangestomerge):

    merged = []
    sortedranges = sorted(rangestomerge)

    for begin, end in sortedranges:
        if merged and merged[-1][1] >= begin:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([begin, end])

    return merged

totalfresh = 0
totalidfresh = 0

fixedranges = merge_ranges(ranges)
for i in ids:
    for onerange in fixedranges:
        if onerange[0] <= i <= onerange[1]:
            totalfresh += 1
            break

for onerange in fixedranges:
    totalidfresh += onerange[1] - onerange[0] + 1

print(totalfresh)
print(totalidfresh)