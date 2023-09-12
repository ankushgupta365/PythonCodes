class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap)   #{-4, -2,1}
        time = 0
        q = deque() #[cnt, nextTime]

        #remove larget number from heap and it to queue, which will be covered into the next iteration
        while maxHeap or q: 
            time+=1
            if maxHeap:
                cnt =1+ heapq.heappop(maxHeap)  #executing one task
                if cnt: #if count become zero then all types of that letters are done executing
                    q.append([cnt, time+n])   #pushing available count after executing and ideal time when next execution
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])   #adding to heap to execute on next iteration
        return time

        