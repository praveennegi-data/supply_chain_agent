import streamlit as st

st.set_page_config(
    page_title="Late Delivery Predictor",
    page_icon="📦"
)

st.title("📦 Late Delivery Predictor")

st.write(
    "AI-powered Supply Chain Delay Investigation Agent"
)

FORM_URL = "https://n8n-agent-app.reddune-eb2aebd8.westus2.azurecontainerapps.io/form/new-order-risk"

st.link_button(
    "🚀 Start Order Investigation",
    FORM_URL,
    use_container_width=True
)
