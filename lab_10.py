import random
import threading
import multiprocessing
import time

# I/O bound task, Simulates network delay w/ sleep
def io_task(thread_id):
    print(f"Thread {thread_id} starting I/O task")
    time.sleep(random.uniform(1, 3))
    print(f"Thread {thread_id} completed I/O task")

# CPU bound task, Computes sum of squares
def cpu_task(process_id):
    print(f"Process {process_id} starting CPU task")
    result = sum(i * i for i in range(1, 5000000))  # Computes SS
    print(f"Process {process_id} completed CPU task with result: {result}")
    return result

# Threading
def run_threading():
    threads = []
    start_time = time.time()
    
    # Creates 3 threads
    for i in range(3):
        thread = threading.Thread(target=io_task, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    return end_time - start_time

# Multiprocessing 
def run_multiprocessing():
    processes = []
    start_time = time.time()
    # Creates 3 processes
    for i in range(3):
        process = multiprocessing.Process(target=cpu_task, args=(i,))
        processes.append(process)
        process.start()
    
    # Wait for processes to complete
    for process in processes:
        process.join()
    
    end_time = time.time()
    return end_time - start_time

def main():
    print("Running Threading (I/O-bound) Tasks...")
    threading_time = run_threading()
    print(f"Threading completed in {threading_time:.2f} seconds\n")
    
    print("Running Multiprocessing (CPU-bound) Tasks...")
    multiprocessing_time = run_multiprocessing()
    print(f"Multiprocessing completed in {multiprocessing_time:.2f} seconds\n")
    
    # Performance comparison
    print("Performance Comparison:")
    print(f"Threading (I/O-bound) took {threading_time:.2f} seconds")
    print(f"Multiprocessing (CPU-bound) took {multiprocessing_time:.2f} seconds")
    print(f"Threading was {multiprocessing_time/threading_time:.2f}x faster" 
          if threading_time < multiprocessing_time 
          else f"Multiprocessing was {threading_time/multiprocessing_time:.2f}x faster")

if __name__ == "__main__":
    main()
