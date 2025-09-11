#student name: Hansen Yang

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list, chopstickMutex: multiprocessing.Semaphore): 
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks 
    """
    def eatForAWhile():   #simulates philosopher eating time with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
    
    def thinkForAWhile(): #simulates philosopher thinking time with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

    for _ in range(20): #to make testing easier, instead of a forever loop we use a finite loop
        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers
        
        chopstickMutex.acquire()    # mutex to ensure that the both chopstick available. philosopher check if both are available
        if chopstick[rightChopstick].acquire(block = False): # if resource not available return False (instead of waiting), avoiding deadlock
            if chopstick[leftChopstick].acquire(block = False):
                chopstickMutex.release() # philosopher let go of the lock so other can check
                print(f"DEBUG: philosopher{id} has chopstick{leftChopstick} and chopstick{rightChopstick}")
                
                eatForAWhile()  #use this line as is
                
                print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
                chopstick[rightChopstick].release()
                print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
                chopstick[leftChopstick].release()
            else:
                # If right chopstick is not available, release the right one
                chopstick[rightChopstick].release()
                chopstickMutex.release()  #release mutex to allow other trial
        else:
            chopstickMutex.release()  #release mutex if right chopstick is not available

        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5

    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    chopstickMutex = multiprocessing.Semaphore(1) # mutex semamphore to ensure a philosopher picks up both chopsticks at the same time

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList, chopstickMutex)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()
