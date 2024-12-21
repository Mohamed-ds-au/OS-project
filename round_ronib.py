from process import Process

def roundRobin(processes_ls:list[Process], qt:int):
    it = 0
    ls = []
    for i in processes_ls:
        i.sb = i.burst_time

    while (len(processes_ls) != 0):
        p = processes_ls.pop(0)
        if (p.arrival_time <= it):
            if (len(p.runs) != 0):
                it = p.runs[-1][-1]

            if (p.burst_time > qt):
                p.burst_time -= qt
                it += qt
                p.runs.append([it-qt, it])
                processes_ls.append(p)
            else:
                it += p.burst_time
                p.runs.append([it-p.burst_time, it])
                p.burst_time = p.sb
                ct = p.runs[-1][1]
                st = p.runs[0][0]
                p.turnaround_time = ct - p.arrival_time
                p.waiting_time = p.turnaround_time - p.burst_time
                p.response_time = st - p.arrival_time
                ls.append(p)
        else:
            processes_ls.append(p)
            it+=1
            
    
    return ls


if __name__=='__main__':
    processes=[Process('p1',0,8),Process('p2',1,4),Process('p3',1,9),Process('p4',3,5)]
    processes2=[Process('p1',0,6),Process('p2',5,1),Process('p3',7,2),Process('p4',12,4)]
    x = roundRobin(processes2, 3)
    for i in x:
        print(i)
        print("#-----------------#")

