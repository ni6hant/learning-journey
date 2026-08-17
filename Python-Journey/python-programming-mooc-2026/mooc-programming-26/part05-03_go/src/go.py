# Write your solution here

def who_won(game_board:list):
    player1_count = 0
    player2_count = 0
    for row in game_board:
        for item in row: 
            if item==1:
                player1_count+=1
            elif item==2:
                player2_count+=1
            else:
                continue
    if player1_count < player2_count:
        return 2
    elif player1_count > player2_count:
        return 1
    else:
        return 0

if __name__ == "__main__":
    test_cases = (([[1,2,1],[0,0,1],[2,1,0]], 1), ([[1,2,2,2],[0,0,0,1],[0,0,2,1]], 2), ([[1,2,2,2],[2,1,1,1],[0,2,1,0]], 0))
    for test in test_cases:
        print(test[0],test[1])
        print(who_won(test[0]))