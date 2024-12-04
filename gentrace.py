import json

file_stamps = open("./stamp2plot.txt", "r")
stamps = file_stamps.readlines()
start = 0
end = len(stamps)

for stamp in stamps:
    if stamp.split(" ")[0] == "in" and start != 0:
        break
    start += 1

i = start
while True:
    curr = int(stamps[i].split(" ")[2].split("\n")[0], 16)
    prev = int(stamps[i-1].split(" ")[2].split("\n")[0], 16)
    epoch = {
        "name": stamps[i].split(" ")[1],
        "cat": "foo",
        "ph": "X",
        "ts": curr / 1000,
        "dur": (curr - prev)/1000,
        "pid": "Core 2",
        "tid": "Task3"
    }
    epoch_raw = json.dumps(epoch)
    print(epoch_raw, ",")
    i += 1
    if i == end:
        break
