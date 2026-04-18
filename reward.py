import json

print("Congratulations! You've completed a task and earned 20 energy points!")
with open('data/energy.json', 'r') as f:
        data = json.load(f)

data['current_energy'] += 20
if data['current_energy'] > data['max_energy']:
    data['current_energy'] = data['max_energy']

with open('data/energy.json', 'w') as f:
    json.dump(data, f, indent=4)
print(f'Your current energy is now: {data["current_energy"]}')