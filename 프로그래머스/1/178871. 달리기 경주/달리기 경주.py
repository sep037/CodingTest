def solution(players, callings):
    players_dict = {name: n for n ,name in enumerate(players)}
    for callplayer in callings : 
        n = players_dict[callplayer]
        
        players[n-1], players[n] = players[n], players[n-1]
        players_dict[players[n]] = n
        players_dict[players[n-1]] = n-1
        
    return players
