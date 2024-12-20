def nonPreemptive(problem: list):
    current=0
    result=[]
    while problem:
        available=[]
        for i in problem:
            if i[2] <=current:
                available.append(i)
        if available:
            sj=available[0]
            for i in available:
                if i[1] < sj[1]:
                    sj=i
            problem.remove(sj)
            pName, burst_time, arrival_time = sj
            
            start_time = max(current, arrival_time)
            complete_time = start_time + burst_time
            turnaround_time = complete_time - arrival_time
            waiting_time = turnaround_time - burst_time
            response_time = start_time - arrival_time

            current = complete_time
            
            result.append([
                pName, burst_time, arrival_time, 
                start_time, complete_time, 
                turnaround_time, waiting_time, 
                response_time
            ])
        else:
            current_time += 1
    return result




if __name__ == "__main__":
    
    problem = [
        ["p1", 10, 10],
        ["p2", 12, 0],
        ["p3", 8, 3],
        ["p4", 4, 5],
        ["p5", 6, 12]
    ]

    result = nonPreemptive(problem)

    for p in result:
        print(p)