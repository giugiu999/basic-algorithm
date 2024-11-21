#EFTF
class job:
    def __init__(self,id,s,f):
        self.id = id
        self.s =s
        self.f = f
def activitySelection(jobs):
    jobs.sort(key=lambda x:x.f,reverse=False)
    schedule=[]
    f_time = 0
    for job in jobs:
        if job.s >= f_time:
            schedule.append(job)
            f_time=job.f
    return schedule

#testing
jobs = [
    job(1, 1, 4),
    job(2, 2, 6),
    job(3, 4, 7),
    job(4, 5, 9),
    job(5, 6, 8),
]
schedule = activitySelection(jobs)
print(f"the largest num is {len(schedule)}")
print(f"selected jobs:")
for jobs in schedule:
    print(f"job{jobs.id} start from {jobs.s} end at {jobs.f}")