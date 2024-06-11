
print(f'ZkSync Checker\n')

with open('zk_eligible.txt') as f: zk_eligible = {address_data.split(':')[0].lower(): address_data.split(':')[1] for address_data in f.read().splitlines()}
with open('addresses.txt') as f: addresses = f.read().splitlines()

total = 0
for address in addresses:
    points = zk_eligible.get(address.lower()) or "0"
    print(f'{address}: {points} points')
    total += int(points)


input(f'\nTotal points: {total}\n\n> Exit')
