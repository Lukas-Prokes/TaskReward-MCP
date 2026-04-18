import json
import time


while True:
    with open('data/energy.json', 'r') as f:
        data = json.load(f)
    
    current_energy = data['current_energy']
    metabolic_rate = data['metabolic_rate']
    max_energy = data['max_energy']

    print(f'Current energy: {current_energy}')
    print(f'Max energy: {max_energy}')
    print(f'Metabolic rate: {metabolic_rate}')

    print('---')
    current_energy -= metabolic_rate
    if current_energy < 0:
        current_energy = 0
    print(f'Current energy (post metabolism): {current_energy}')

    data['current_energy'] = current_energy 

    with open('data/energy.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    time.sleep(2)