#Daily Temperatures

# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait
# until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
# [1, 1, 4, 2, 1, 1, 0, 0].

T = [73, 74, 75, 71, 69, 72, 76, 73]

#Solution
def solution(T):
    stack = []  # store the index of T
    result = [0] * len(T)
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result

print(solution(T)) #[1, 1, 4, 2, 1, 1, 0, 0]