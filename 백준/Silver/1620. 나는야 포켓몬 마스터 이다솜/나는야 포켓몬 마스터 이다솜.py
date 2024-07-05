import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number_to_pokemon = {}
pokemon_to_number = {}

q = []
for i in range(1,N+1):
    pokemon = input().strip()
    number_to_pokemon[i] = pokemon
    pokemon_to_number[pokemon] = i

for _ in range(M):
    q.append(input().strip())

for w in q:    
    if w.isdigit():
        print(number_to_pokemon[int(w)])
    else:
        print(pokemon_to_number[w])