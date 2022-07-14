scale = list(map(int, input().split()))

not_ascending = False
not_descending = False
for i, v in enumerate(scale):
    if v != i + 1:
        not_ascending = True
    if v != 8 - i:
        not_descending = True

if not not_ascending and not_descending:
    print('ascending')
elif not not_descending and not_ascending:
    print('descending')
else:
    print('mixed')