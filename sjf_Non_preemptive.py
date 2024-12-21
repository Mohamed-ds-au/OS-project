from process import Process
def sjf_nonpreemptive(problem: list):
        current=0
        result=[]
        while problem:
            available=[]
            for i in problem:
                if i.arrival_time <=current:
                    available.append(i)
            if available:
                sj=available[0]
                for i in available:
                    if i.burst_time < sj.burst_time:
                        sj=i
                        
                problem.remove(sj)
                
                process = Process(sj.p_id, sj.arrival_time, sj.burst_time)
                
                start_time = max(current, process.arrival_time)
                complete_time = start_time + process.burst_time
                process.runs.append([start_time,complete_time])
                process.turnaround_time = complete_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                process.response_time = start_time - process.arrival_time

                current = complete_time
                
                result.append([
                    process.p_id, process.arrival_time, process.burst_time,
                    process.runs, 
                    process.turnaround_time, process.waiting_time, 
                    process.response_time
                ])
            else:
                current += 1
        return result
    




if __name__ == "__main__":
    processes=[Process("p1", 10, 10),Process('p2',0,12),Process("p3", 3, 8),Process("p4", 5, 4),Process("p5", 12, 6)]
    
    for p in sjf_nonpreemptive(processes):
        print(p)