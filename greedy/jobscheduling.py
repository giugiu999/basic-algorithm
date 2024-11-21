# ESTF
# idea: sort out starting time, min-heap store the current finishing time, iterate over each job
import heapq

class job:
    def __init__(self,id,s,f):
        self.id = id
        self.s =s
        self.f = f
def jobscheduling(jobs):
    jobs.sort(key=lambda x:x.s,reverse=False) # low to high
    machines=[]# f time for each machine, id
    schedule=[]#machine id <-> job
    for job in jobs:
        if machines and machines[0][0] <= job.s:
            end_time, machine_id = heapq.heappop(machines)
        else:
            machine_id = len(machines) + 1
        heapq.heappush(machines, (job.f, machine_id))
        schedule.append(machine_id)
    return len(machines), schedule

#testing
jobs = [
    job(1, 1, 4),
    job(2, 2, 6),
    job(3, 4, 7),
    job(4, 5, 9),
    job(5, 6, 8),
]
num_machines, schedule = jobscheduling(jobs)

print(f"Minimum number of machines required: {num_machines}")
print("job schedule:")
for i, jobs in enumerate(jobs):
    print(f"  job {jobs.id} (start: {jobs.s}, end: {jobs.f}) -> Machine {schedule[i]}")
