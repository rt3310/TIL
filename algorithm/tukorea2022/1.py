n = int(input())
sits = input()

holder = []
i = 0
while i < n:
    if sits[i] == 'S':
        holder.append('*')
        holder.append(sits[i])
        i += 1
    else:
        holder.append('*')
        holder.append(sits[i])
        holder.append(sits[i+1])
        i += 2
holder.append('*')

count = 0
for i in range(1, len(holder)-1):
    if holder[i] == '*':
        continue
    
    if holder[i-1] == '*':
        holder[i-1] = '0'
        count += 1
        continue
    
    if holder[i+1] == '*':
        holder[i+1] = '0'
        count += 1
        continue

print(count)