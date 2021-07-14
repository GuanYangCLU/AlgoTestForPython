def solution(total_money, total_damage, costs, damages):
    ratios = sorted([(i/j, i, j) for i, j in zip(damages, costs)], reverse=True)
    money_counter = 0
    damage_counter = 0
    for val, damage, money in ratios:
        if money_counter + money < total_money:
            damage_counter += damage
        # check if pass
        if damage_counter > total_damage:
            return True
    else:
        return False
    

total_money = 5
total_damage = 10
costs = [4, 5, 1]
damages = [1, 2, 3]

print(solution(total_money, total_damage, costs, damages))
