import sys


class item:
    value = 0
    priority = 0

### array based PQ
### descending order priority queue
# Time Complexity:
# Space Complexity: 
class PQ: 

    pq_array = [None] * (100000)

    starting_index = -1

    """
    Adding a value to the pq based on priority
    Time Complexity: O(1)
    """
    @staticmethod
    def enqueue(value, priority):
        
        # increase the index
        PQ.starting_index += 1

        # insert the element
        PQ.pq_array[PQ.starting_index] = item()
        PQ.pq_array[PQ.starting_index].value = value
        PQ.pq_array[PQ.starting_index].priority = priority 
    
    """
    Function to check the top element
    @return returns -1 if not found
    Time Complexity: O(N) -> loops till the end of starting_index
    """
    @staticmethod 
    def peek():
        largest_prio = -sys.maxsize
        ind = -1

        # check for the element with highest priority 
        # check if pq is larger than one
        i = 0
        while(i <= PQ.starting_index):
            if largest_prio == PQ.pq_array[i].priority and ind > -1 and PQ.pq_array[i].value > PQ.pq_array[ind].value:
                ind = i
            elif largest_prio < PQ.pq_array[i].priority:
                largest_prio = PQ.pq_array[i].priority
                ind = i
                
            i += 1

        return ind 
    
    """
    Removing the value with the high priority 
    Time Complexity: O(N) -> loops till the end of starting_index worst case
    """
    @staticmethod
    def dequeue():

        # find the position of the element with the highest priority 
        ind = PQ.peek()

        i = ind
        while i < PQ.starting_index:
            PQ.pq_array[i] = PQ.pq_array[i + 1]
            i += 1

        PQ.starting_index -= 1

    """
    testing
    """
    @staticmethod
    def main( args):

        # inserting new elements by priority 
        PQ.enqueue(10, 2)
        PQ.enqueue(14, 4)
        PQ.enqueue(16, 4)
        PQ.enqueue(12, 3)


        ind = PQ.peek()
        # should be 16,4 
        print(ind, PQ.pq_array[ind].value, PQ.pq_array[ind].priority, sep = ",")

        PQ.dequeue()
        # should dequeue 16 4 -> highest priority with largest value

        # check top element
        ind = PQ.peek()
        print(ind, PQ.pq_array[ind].value, PQ.pq_array[ind].priority, sep = ",")
        # should be 14 4 

        PQ.dequeue()

        ind = PQ.peek()
        print(ind, PQ.pq_array[ind].value, PQ.pq_array[ind].priority, sep = ",")


if __name__ == "__main__":

    PQ.main([])
