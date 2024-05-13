def solution(genres, plays):
    play_hash = {}
    for i in range(len(plays)):
        if not genres[i] in play_hash:
            play_hash[genres[i]] = {i:plays[i]}
        else:
            play_hash[genres[i]][i] = plays[i]
        
    genre_sums = {genre: sum(plays.values()) for genre, plays in play_hash.items()}
    
    sorted_genres = sorted(genre_sums.keys(), key=lambda x: (-genre_sums[x], x))

    priority_indices = []
    for genre in sorted_genres:
        sorted_songs = sorted(play_hash[genre].items(), key=lambda x: (-x[1], x[0]))
        count = 0
        for index, _ in sorted_songs:
            if count < 2:
                priority_indices.append(index)
                count += 1
    return priority_indices

    