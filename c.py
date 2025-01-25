from flask import Flask, Response
import io
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def plot():
    try:
        # Initialize driving and restraining forces
        driving_forces = {
            "Vision": 70,
            "Risk-Taking": 60,
            "Leadership": 65,
            "Customer Focus": 55,
            "Resilience": 50,
            "Networking": 60,
            "Motivation": 70,
        }

        restraining_forces = {
            "Resistance to Change": 65,
            "Fear of Failure": 60,
            "Stakeholder Misalignment": 50,
            "Market Uncertainty": 55,
            "Limited Resources": 70,
            "Lack of Trust": 50,
            "Burnout": 60,
        }

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

        iterations = 20
        driving_force_values = []
        restraining_force_values = []

        # Simulation logic
        for _ in range(iterations):
            for key in driving_forces:
                driving_forces[key] += nudge_effects[key] + np.random.randint(-1, 2)

            for key in restraining_forces:
                restraining_forces[key] += balance_effects[key] + np.random.randint(-1, 2)

            total_driving_force = sum(driving_forces.values())
            total_restraining_force = sum(restraining_forces.values())

            driving_force_values.append(total_driving_force)
            restraining_force_values.append(total_restraining_force)

        # Plotting
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
        plt.title("Force Field Analysis Simulation: Entrepreneurial Traits and Progress")
        plt.xlabel("Iterations (Time)")
        plt.ylabel("Force Magnitude")
        plt.legend(loc='upper left')
        plt.grid(True, linestyle='--', alpha=0.6)

        # Save the plot to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()  # Free memory
        return Response(img.getvalue(), mimetype='image/png')

    except Exception as e:
        return f"An error occurred: {e}", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
