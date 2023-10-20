
def iter_tools(m, n):
    sorted_list_A = sorted(set(m))
    sorted_list_B = sorted(set(n))

    pairs = [ (a, b) for a in sorted_list_A for b in sorted_list_B]

    pairs_str = ' '.join(f"({a}, {b})" for a, b in pairs)

    return pairs_str

m = list(map(int, input().rstrip().split()))

n = list(map(int, input().rstrip().split()))

result = iter_tools(m, n)

print(result)
