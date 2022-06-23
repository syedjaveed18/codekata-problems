n = input()
goals = list(map(int,input().split()))
net_goal_rate = []
for goal in goals:
    net_goal_rate.append(goal - sum(goals[-3:]))
print(' '.join([str(net_goal) for net_goal in net_goal_rate]))
