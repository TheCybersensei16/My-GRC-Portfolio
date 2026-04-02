import numpy as np
import matplotlib.pyplot as plt

# FAIR Monte Carlo Simulation - Simple Example for Cyber Risk
np.random.seed(42)

# Example: Data Breach Risk for Indian Fintech
n_simulations = 10000

# Loss Event Frequency (LEF) - times per year
lef = np.random.poisson(1.2, n_simulations)   # 1.2 breaches expected per year

# Loss Magnitude (LM) in INR - Single Loss Event
lm = np.random.lognormal(mean=13.5, sigma=1.2, size=n_simulations)  # ~₹4.5 Cr mean

# Annual Loss Expectancy (ALE)
ale = lef * lm

print(f"Expected Annual Loss (ALE): ₹{ale.mean():,.0f}")
print(f"99th Percentile Worst Case: ₹{np.percentile(ale, 99):,.0f}")

# Optional: Plot
plt.hist(ale, bins=50, color='skyblue')
plt.title('Monte Carlo Simulation - Annual Cyber Loss (FAIR Model)')
plt.xlabel('Loss in INR')
plt.ylabel('Frequency')
plt.savefig('FAIR_Simulation_Result.png')
plt.show()
