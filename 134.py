class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        leave = []
        for i in range(len(gas)):
            leave.append(gas[i] - cost[i])
        for i in range(len(leave)):
            if leave[i] >= 0:
                temp = i
                sum = 0
                yiquan = False
                while sum >= 0:
                    sum += leave[temp]
                    temp += 1

                    if temp == len(gas):
                        temp = 0
                        yiquan = True
                    if i == temp and yiquan:
                        return i
        return -1

sol=Solution()
sol.canCompleteCircuit([3,3,4],[3,4,4])