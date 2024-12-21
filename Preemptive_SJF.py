from process import Process

def preemptive_sjf(process_list: list):
    # Gantt_Chart list
    gantt_chart = []
    
    # dictionary holds the start and end time for each process execution
    time_intervals = {}    

    # define a list containing a completed processes
    completed_process = []

    # define a dictionary containing burst times of the processes to save them
    initial_burst_times = {}
    for p in process_list:
        initial_burst_times[p.p_id] = p.burst_time
    
    # initial time (first arrival time)
    t = sorted(process_list, key=lambda process: process.arrival_time)[0].arrival_time

    while len(process_list) != 0:
        # available processes in a specified time
        available = []

        for p in process_list:
            if p.arrival_time <= t:
                available.append(p)

        t += 1

        if len(available) != 0:
            # sort the available processes by the burst_time
            available.sort(key=lambda process: process.burst_time)
            process = available[0]
            gantt_chart.append(process.p_id)
            process_list.remove(process)
            
            # updating the burst time of the process
            process.burst_time -= 1

            if process.burst_time == 0:
                process.burst_time = initial_burst_times[process.p_id]
                
                # Completion Time
                CT = t

                # Turnaround Time
                process.turnaround_time = CT - process.arrival_time

                # Waiting Time
                process.waiting_time = process.turnaround_time - process.burst_time

                completed_process.append(process)

            else:
                process_list.append(process)


    # the first arrival time
    first_arrival_time = sorted(completed_process, key=lambda process: process.arrival_time)[0].arrival_time
    
    # define boundaries for time intervals when a process was executed 
    min_time_boundary = first_arrival_time
    max_time_boundary = min_time_boundary + 1

    for i in range(len(gantt_chart)):
        if (i == len(gantt_chart) - 1) or (gantt_chart[i] != gantt_chart[i+1]): 
            if gantt_chart[i] not in time_intervals:
                time_intervals[gantt_chart[i]] = []
            
            time_intervals[gantt_chart[i]].append([min_time_boundary, max_time_boundary])
            min_time_boundary = max_time_boundary

        max_time_boundary += 1 
    
    for p in completed_process:
        # assign the list of time intervals to runs list for each process 
        p.runs = time_intervals[p.p_id]

        # Response time
        p.response_time = p.runs[0][0] - p.arrival_time

    return completed_process

if __name__ == '__main__':
    '''
    Testing :D
    '''
    # initialze the processes objects
    p1 = Process('P1', 10, 10)
    p2 = Process("p2", 0, 12)
    p3 = Process("p3", 3, 8)
    p4 = Process("p4", 5, 4)
    p5 = Process("p5", 12, 6)

# define the process_list (list of objects)
    process_list = [p1, p2, p3, p4, p5]
    result = preemptive_sjf(process_list)

    for p in result:
        print(f'{p}\n----------------------------------------')