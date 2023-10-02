from dataclasses import dataclass

@dataclass
class ProcessSchedule:
    start_time: int
    end_time: int

@dataclass
class Dependency:
    pid1: int
    pid2: int

class Scheduler:
    def __init__(self, processes: list[ProcessSchedule], dependencies: list[Dependency]):
        self.processes = processes
        self.dependencies = dependencies

    # print output using 'print()'
    def print_schedule(self):
        processes = self.processes
        dependencies = self.dependencies
        n = len(processes)

        # Create a list to track dependencies for each process
        process_dependencies = {pid: [] for pid in range(n)}
        reverse_dependencies = {}
        
        for dep in dependencies:
            if dep.pid2 in reverse_dependencies:
                reverse_dependencies[dep.pid2].append(dep.pid1)
            else:
                reverse_dependencies[dep.pid2] = [dep.pid1]
    

        # Populate the process_dependencies list
        for dep in dependencies:
            if dep.pid1 in process_dependencies:
                process_dependencies[dep.pid1].append(dep.pid2)
            else:
                process_dependencies[dep.pid1] = [dep.pid2]
                
        
       
        schedule = []

        while len(schedule) < n:
            scheduled = False
            for pid in range(n):
                if pid not in schedule and all(dep in schedule for dep in process_dependencies[pid]):
                    schedule.append(pid)
                    scheduled = True
            if not scheduled:
                return "IMPOSSIBLE"

        for pid in schedule:
            lowest_start_time = processes[pid].start_time
            for dependency in process_dependencies[pid]:
                lowest_start_time = max(lowest_start_time, processes[dependency].start_time+1)
            
            highest_end_time = processes[pid].end_time
            
            for dependency in process_dependencies[pid]:
                lowest_start_time = max(lowest_start_time, processes[dependency].start_time+1)
            print(pid, lowest_start_time, processes[pid].end_time)
  


if __name__ == "__main__":
    import sys

    read_line = lambda: sys.stdin.readline().split()

    first_line = read_line()
    T = int(first_line[0])
    for _ in range(T):
        line = read_line()
        N = int(line[0])
        M = int(line[1])

        processes: list[ProcessSchedule] = []
        dependencies: list[Dependency] = []

        for _ in range(N):
            line = read_line()
            start_time = int(line[0])
            end_time = int(line[1])
            process_schedule = ProcessSchedule(start_time, end_time)
            processes.append(process_schedule)

        for _ in range(M):
            line = read_line()
            pid1 = int(line[0])
            pid2 = int(line[1])
            dependency = Dependency(pid1, pid2)
            dependencies.append(dependency)

        scheduler = Scheduler(processes, dependencies)
        scheduler.print_schedule()