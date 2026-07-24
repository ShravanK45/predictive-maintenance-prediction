import streamlit as st
import pickle
import pandas as pd
import numpy as np

def load_model():

    with open("predictive_maintenance_artifacts.pkl","rb") as f:
        artifacts = pickle.load(f)

    return artifacts


artifacts = load_model()

model = artifacts["model"]
columns = artifacts["columns"]
type_mapping = artifacts["type_mapping"]

def prepare_input(
    machine_type,
    air_temp,
    process_temp,
    rpm,
    torque,
    tool_wear
):

    input_dict = dict.fromkeys(columns,0)

    input_dict["Type"] = type_mapping[machine_type]

    input_dict["Air temperature K"] = air_temp
    input_dict["Process temperature K"] = process_temp
    input_dict["Rotational speed rpm"] = rpm
    input_dict["Torque Nm"] = torque
    input_dict["Tool wear min"] = tool_wear

    input_df = pd.DataFrame([input_dict])

    return input_df


def predict_failure(
    machine_type,
    air_temp,
    process_temp,
    rpm,
    torque,
    tool_wear
):

    input_df = prepare_input(
        machine_type,
        air_temp,
        process_temp,
        rpm,
        torque,
        tool_wear
    )

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability


def show_predict_page():

    st.title("Predictive Maintenance System")

    st.info(
        "Predict whether an industrial machine is likely to fail based on sensor readings."
    )

    with st.form("Prediction Form"):

        machine_type = st.selectbox(
            "Machine Type",["L","M","H"]
        )

        air_temp = st.number_input(
            "Air Temperature (K)"
        )

        process_temp = st.number_input(
            "Process Temperature (K)"
        )

        rpm = st.number_input(
            "Rotational Speed (RPM)"
        )

        torque = st.number_input(
            "Torque (Nm)"
        )

        tool_wear = st.number_input(
            "Tool Wear (minutes)"
        )

        submitted = st.form_submit_button(
            "Predict"
        )

        if submitted:

            prediction, probability = predict_failure(
                machine_type,
                air_temp,
                process_temp,
                rpm,
                torque,
                tool_wear
            )

            if prediction == 1:

                st.error("⚠ Machine Failure Likely")

            else:

                st.success("✅ Machine Healthy")

            st.metric(
                "Failure Probability",
                f"{probability*100:.2f}%"
            )

show_predict_page()

with st.expander("Important Factors"):

    st.write("""
    The model primarily considers:

    • Tool Wear

    • Rotational Speed

    • Torque

    • Air Temperature

    • Process Temperature
    """)