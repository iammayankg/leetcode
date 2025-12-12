class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentionCount = [0]*numberOfUsers
        eventsParsed = []
        for e in events:
            m = e[0]
            t = int(e[1])
            target = None
            if m == "MESSAGE":
                if e[2] != "ALL" and e[2] != "HERE":
                    target = list([int(x[2:]) for x in e[2].split(" ")])
                else:
                    target = e[2]
            else:
                target = int(e[2])
            eventsParsed.append((m, t, target))
                
        eventsParsed.sort(key=lambda x: (x[1], x[0]=="MESSAGE"))
        offline = defaultdict(lambda: math.inf) #time
        globalMentions = 0
        for e in eventsParsed:
            msg, time, target = e
            if msg == "MESSAGE":
                if target == "ALL":
                    globalMentions += 1
                elif target == "HERE":
                    for i in range(numberOfUsers):
                        if offline[i] == math.inf or time < offline[i] or time >= offline[i] + 60:
                            mentionCount[i] += 1
                else:
                    for i in target:
                        mentionCount[i] += 1
            else:
                offline[target] = time

        return [m + globalMentions for m in mentionCount]
