
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="3D IC Thermal Simulator", layout="centered")
st.title("🔥 3D IC Thermal Estimator (Celsius-style Demo Tool)")

st.markdown("""
This is a **demo simulation tool** that estimates the junction temperature of a 3D IC 
based on basic thermal parameters. It's designed to resemble a simplified version of 
Cadence Celsius Thermal Solver for academic presentations.
""")

st.sidebar.header("🛠️ Input Parameters")

tim_thickness = st.sidebar.slider("TIM Thickness (mm)", 0.1, 2.0, 0.5, 0.1)
power_density = st.sidebar.number_input("Power Density (W/mm²)", value=0.5, step=0.1)
ambient_temp = st.sidebar.number_input("Ambient Temperature (°C)", value=25, step=1)
material = st.sidebar.selectbox("TIM Material", ["Copper", "AlN", "Graphite"])

material_k = {
    "Copper": 400,
    "AlN": 140,
    "Graphite": 150
}

tim_thickness_m = tim_thickness / 1000
k = material_k[material]

area = 1e-6
r_th = tim_thickness_m / (k * area)
junction_temp = ambient_temp + power_density * 1e6 * r_th

st.header("🧪 Simulation Output")
st.write(f"**Selected TIM Material:** {material}")
st.write(f"**Thermal Conductivity:** {k} W/m·K")
st.write(f"**Thermal Resistance:** {r_th:.4f} °C/W")
st.success(f"**Estimated Junction Temperature: {junction_temp:.2f} °C**")

temp_map = np.random.normal(loc=junction_temp, scale=1.5, size=(10, 10))
fig, ax = plt.subplots()
heatmap = ax.imshow(temp_map, cmap='hot', interpolation='nearest')
plt.colorbar(heatmap, ax=ax)
plt.title("📊 Simulated Thermal Map (Sample)")

st.pyplot(fig)
