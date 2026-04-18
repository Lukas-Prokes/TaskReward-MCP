import json
from mcp.server.fastmcp import FastMCP

server = FastMCP("TaskReward")

@server.tool()
def get_current_energy():
    with open('data/energy.json', 'r') as f:
        data = json.load(f)
    return data['current_energy'], data['max_energy'], data['metabolic_rate']

@server.tool()
def take_payment(amount, reason):
    with open('data/energy.json', 'r') as f:
        data = json.load(f)
    data['current_energy'] += amount
    if data['current_energy'] > data['max_energy']:
        data['current_energy'] = data['max_energy']

    with open('data/energy.json', 'w') as f:
        json.dump(data, f, indent=4)

    return f"Payment of {amount} taken for {reason}. Current energy: {data['current_energy']}, Max energy: {data['max_energy']}, Metabolic rate: {data['metabolic_rate']}"


@server.tool()
def get_upgrade(upgrade, increase_by):
    with open('data/energy.json', 'r') as f:
        data = json.load(f)
    if upgrade == "max_energy":
        cost = int((increase_by * 2) + (data["max_energy"] * 0.2))
        if data['current_energy'] >= cost:
            data['current_energy'] -= cost
            data['max_energy'] += increase_by
            result = f"Max energy increased by {increase_by}. Current energy: {data['current_energy']}, Max energy: {data['max_energy']}, Metabolic rate: {data['metabolic_rate']}"
        else:
            result = f"Not enough energy for upgrade. Cost: {cost}, Current energy: {data['current_energy']}"

    elif upgrade == "worker_count":
        cost = int((increase_by * 5) + (data["worker_count"] * 10))
        if data['current_energy'] >= cost:
            data['current_energy'] -= cost
            data['worker_count'] += increase_by
            result = f"Worker count increased by {increase_by}. Current energy: {data['current_energy']}, Max energy: {data['max_energy']}, Worker count: {data['worker_count']}"
        else:
            result = f"Not enough energy for upgrade. Cost: {cost}, Current energy: {data['current_energy']}"

    elif upgrade == "passive_gain":
        cost = int((increase_by * 3) + (data["passive_gain"] * 5))
        if data['current_energy'] >= cost:
            data['current_energy'] -= cost
            data['passive_gain'] += increase_by
            result = f"Passive gain increased by {increase_by}. Current energy: {data['current_energy']}, Max energy: {data['max_energy']}, Passive gain: {data['passive_gain']}"
        else:
            result = f"Not enough energy for upgrade. Cost: {cost}, Current energy: {data['current_energy']}"

    elif upgrade == "unlock_sensors":
        cost = 250
        if data['sensors_unlocked']:
            result = f"Sensors already unlocked. Current energy: {data['current_energy']}, Max energy: {data['max_energy']}, Sensors unlocked: {data['sensors_unlocked']}"
        else:
            if data['current_energy'] >= cost:
                data['current_energy'] -= cost
                data['sensors_unlocked'] = True
                result = f"Sensors unlocked. Current energy: {data['current_energy']}, Max energy: {data['max_energy']}, Sensors unlocked: {data['sensors_unlocked']}"
            else:
                result = f"Not enough energy for upgrade. Cost: {cost}, Current energy: {data['current_energy']}"

    with open('data/energy.json', 'w') as f:
        json.dump(data, f, indent=4)
    return result

if __name__ == "__main__":
    server.run()