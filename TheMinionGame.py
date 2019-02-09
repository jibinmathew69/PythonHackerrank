def minion_game(string):
    vowels = "AEIOU"
    st_score = 0
    ke_score = 0

    for i in range(len(string)):
        if string[i] in vowels:
            ke_score += len(string) - i
        else:
            st_score += len(string) - i

    if ke_score>st_score:
        print( "Kevin %s"%ke_score)
    elif ke_score<st_score:
        print( "Stuart %s"%st_score)
    else:
        print("Draw")