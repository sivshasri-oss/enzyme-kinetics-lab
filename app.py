import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧪 Virtual Enzyme Kinetics Lab")

st.write("Simulate enzyme kinetics using the Michaelis-Menten model.")

# Sidebar controls
st.sidebar.header("Experiment Controls")

Vmax = st.sidebar.slider("Maximum Velocity (Vmax)", 0.1, 10.0, 2.0)
Km = st.sidebar.slider("Michaelis Constant (Km)", 0.1, 10.0, 1.0)
substrate_max = st.sidebar.slider("Max Substrate Concentration", 1, 100, 50)

# Substrate concentration range
S = np.linspace(0.1, substrate_max, 100)

# Michaelis-Menten equation
v = (Vmax * S) / (Km + S)

# Plot
fig, ax = plt.subplots()
ax.plot(S, v)
ax.set_xlabel("Substrate Concentration [S]")
ax.set_ylabel("Reaction Velocity (v)")
ax.set_title("Michaelis-Menten Curve")

st.pyplot(fig)

# Explanation
st.subheader("📖 Theory")
st.write("""
The Michaelis-Menten equation describes enzyme kinetics:

v = (Vmax [S]) / (Km + [S])

Where:
- Vmax = maximum reaction velocity
- Km = substrate concentration at half Vmax
""")

# Observation section
st.subheader("🔍 Observations")
st.write("Adjust the sliders to see how Vmax and Km affect the curve.")