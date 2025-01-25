from flask import Flask, Response
import io

app = Flask(__name__)

@app.route('/')
def plot():
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Your existing plotting code
    iterations = 20
    driving_force_values = []
    restraining_force_values = []
    
    # Simulate changes (copy your simulation code here)

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

    # Return the plot as an image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return Response(img.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
