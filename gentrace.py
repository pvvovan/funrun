import json


def get_func(id):
        if id == "0xFFFFFFFF":
                return "idle"
        if id == "0x00010000":
                return "task1"
        if id == "0x00010001":
                return "func1"
        if id == "0x00020000":
                return "task2"
        if id == "0x00020002":
                return "func2"
        if id == "0x00020003":
                return "func3"
        return "none"

def get_core(id):
        if id == "idle":
                return "idle"
        if id == "task1":
                return "Core 1"
        if id == "func1":
                return "Core 1"
        if id == "task2":
                return "Core 2"
        if id == "func2":
                return "Core 2"
        if id == "func3":
                return "Core 2"
        return "none"

def get_task(id):
        if id == "idle":
                return "idle"
        if id == "task1":
                return "Task1"
        if id == "func1":
                return "Task1"
        if id == "task2":
                return "Task2"
        if id == "func2":
                return "Task2"
        if id == "func3":
                return "Task2"
        return "none"


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
        func = get_func(stamps[i].split(" ")[1])
        epoch = {
                "name": func,
                "cat": "foo",
                "ph": "X",
                "ts": curr / 1000,
                "dur": (curr - prev)/1000,
                "pid": get_core(func),
                "tid": get_task(func)
        }
        epoch_raw = json.dumps(epoch)
        print(epoch_raw + ",")
        i += 1
        if i == end:
                break
