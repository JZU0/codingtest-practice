def find_layers(N):
    if N == 1:
        return 1
    layer = 1
    max_in_layer = 1
    while max_in_layer < N:
        max_in_layer += 6 * layer
        layer += 1
    return layer

N = int(input())
print(find_layers(N))