class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                oldHigh = stack.pop()
                answer[oldHigh] = i - oldHigh
            stack.append(i)
        return answer


            