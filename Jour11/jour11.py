from pathlib import Path
import itertools

p = Path("Jour11\\input.txt")

lines = p.read_text(encoding="utf-8").splitlines()

flow = {}

visited = {""}
trimmed = {""}

for line in lines:
    machines = line.split(':')
    outputs = []
    for mac in machines[1].strip().split(' '):
        outputs.append(mac)
    flow[machines[0]] = outputs


def hasSonOut(device):
    totalpath = 0
    for output in flow[device]:
        if output == "out":
            return 1
        else:
            totalpath += hasSonOut(output)
        visited.add(output)
    return totalpath

def hasSonDac(device):
    totalpath = 0
    for output in flow[device]:
        if output == "dac":
            return 1
        elif output in trimmed:
            return 0
        else:
            
            totalpath += hasSonDac(output)
        visited.add(output)
    return totalpath

def hasSonFft(device):
    totalpath = 0
    for output in flow[device]:
        if output == "fft":
            return 1
        elif output in trimmed:
            continue
        else:
            totalpath += hasSonFft(output)
        visited.add(output)
    return totalpath


def pruneflow(flow : dict):
    flowcopy = {}
    for key in flow.keys():
        if key not in visited:
            flowcopy[key] = flow[key]
        else:
            trimmed.add(key)

    print(trimmed)
    return flowcopy



dacout = hasSonOut("dac")
visited.add("dac")
flow = pruneflow(flow)
#print(set(flow.keys()).intersection(visited))
fftdac = hasSonDac("fft")
visited.add("fft")
flow = pruneflow(flow)
#print(set(flow.keys()).intersection(visited))
svrfft = hasSonFft("svr")
#visited.add("svr")
#flow = pruneflow(flow)
#print(set(flow.keys()).intersection(visited))
#print(flow.keys())
print((dacout,fftdac,svrfft))
print(dacout*fftdac*svrfft)