import json
import time


while True:
    with open('data/energy.json', 'r') as f:
        data = json.load(f)
    
    current_energy = data['current_energy']
    metabolic_rate = data['metabolic_rate']
    max_energy = data['max_energy']
    worker_count = data['worker_count']
    passive_gain = data['passive_gain']
    sensors_unlocked = data['sensors_unlocked']

    print(f'Current energy: {current_energy}')
    print(f'Max energy: {max_energy}')
    print(f'Metabolic rate: {metabolic_rate}')
    print(f'Worker count: {worker_count}')
    print(f'Passive gain: {passive_gain}')
    print(f'Sensors unlocked: {sensors_unlocked}')

    print('---')
    current_energy -= (metabolic_rate * worker_count)
    current_energy += passive_gain
    if current_energy > max_energy:
        current_energy = max_energy
    if current_energy < 0: 
        current_energy = 0
    print(f'Current energy (post metabolism): {current_energy}')

    data['current_energy'] = current_energy 

    with open('data/energy.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    time.sleep(2)