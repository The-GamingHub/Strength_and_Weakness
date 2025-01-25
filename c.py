import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define initial values for driving and restraining forces
# Driving Forces (Positive Factors)
driving_forces = {
    "Vision": 70,
    "Risk-Taking": 60,
    "Leadership": 65,
    "Customer Focus": 55,
    "Resilience": 50,
    "Networking": 60,
    "Motivation": 70,
}

# Restraining Forces (Negative Factors)
restraining_forces = {
    "Resistance to Change": 65,
    "Fear of Failure": 60,
    "Stakeholder Misalignment": 50,
    "Market Uncertainty": 55,
    "Limited Resources": 70,
    "Lack of Trust": 50,
    "Burnout": 60,
}

# Step 2: Define intervention strategies (Nudges and Balance Restoration)
nudge_effects = {
    "Vision": 2,
    "Risk-Taking": 3,
    "Leadership": 2,
    "Customer Focus": 3,
    "Resilience": 2,
    "Networking": 2,
    "Motivation": 3,
}

balance_effects = {
    "Resistance to Change": -3,
    "Fear of Failure": -2,
    "Stakeholder Misalignment": -2,
    "Market Uncertainty": -3,
    "Limited Resources": -2,
    "Lack of Trust": -2,
    "Burnout": -3,
}

# Step 3: Simulate the changes over time
iterations = 20
driving_force_values = []
restraining_force_values = []

for i in range(iterations):
    # Update driving forces using nudges
    for key in driving_forces:
        driving_forces[key] += nudge_effects[key] + np.random.randint(-1, 2)  # Random variation
    
    # Update restraining forces using balance interventions
    for key in restraining_forces:
        restraining_forces[key] += balance_effects[key] + np.random.randint(-1, 2)  # Random variation
    
    # Sum total forces
    total_driving_force = sum(driving_forces.values())
    total_restraining_force = sum(restraining_forces.values())
    
    # Store values for plotting
    driving_force_values.append(total_driving_force)
    restraining_force_values.append(total_restraining_force)

# Step 4: Plot the results
plt.figure(figsize=(12, 6))
plt.plot(driving_force_values, label='Driving Forces', color='green', linewidth=2)
plt.plot(restraining_force_values, label='Restraining Forces', color='red', linewidth=2)
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
plt.fill_between(range(iterations), driving_force_values, restraining_force_values,
                 where=(np.array(driving_force_values) > np.array(restraining_force_values)),
                 color='green', alpha=0.2, label='Positive Progress')
plt.fill_between(range(iterations), driving_force_values, restraining_force_values,
                 where=(np.array(driving_force_values) <= np.array(restraining_force_values)),
                 color='red', alpha=0.2, label='Negative Progress')

# Customizing plot
plt.title("Force Field Analysis Simulation: Entrepreneurial Traits and Progress")
plt.xlabel("Iterations (Time)")
plt.ylabel("Force Magnitude")
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()