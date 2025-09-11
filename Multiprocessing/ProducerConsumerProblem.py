# Student names: Hansen Yang
 
import threading
import queue
import time, random

# global Variable
num_item = 5 # used in producerWorker

def consumerWorker (queue) -> None:
    """target worker for a consumer thread"""
    while True:
        item = queue.get()
        if item is None:  # sentinel value to signal consumer to exit
            queue.task_done()
            break

        print(f"Consumer {threading.current_thread().name} consumed: {item}")
        
        time.sleep(round(random.uniform(.1, .3), 2))  # Random delay (100 to 300 ms)
        
        queue.task_done()  # Mark task as done
  
def producerWorker(queue) -> None:
    """target worker for a producer thread"""

    for i in range(num_item):  
        # Create a random number integer type
        item = random.randint(1, 100)
        print(f"Producer {threading.current_thread().name} produced: {item}")
        
        # insert an item to queue
        queue.put(item)

        # Delay for every item creation
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

if __name__ == "__main__":
    # Shared buffer/queue
    buffer = queue.Queue()
    
    # Variables
    num_producer = 4
    num_consumer = 5
    
    producer_threads = []
    consumer_threads =[]

    # Create producer threads
    for i in range(num_producer):
        t1 = threading.Thread(target=producerWorker, args=(buffer,))
        producer_threads.append(t1)
        t1.start()
    
    # Create consumer threads
    for i in range(num_consumer):
        t2 = threading.Thread(target=consumerWorker, args=(buffer,))
        consumer_threads.append(t2)
        t2.start()

    # wait for producer processes to finish
    for i in producer_threads:
        i.join()

    # Add sentinel values to signal consumers to exit
    for i in range(num_consumer):
        buffer.put(None)

    # wait for buffer process to finish
    buffer.join()
    print("Producer and consumer have processed all items ")
