import streamlit as st

st.set_page_config(
    page_title="Late Delivery Predictor",
    page_icon="📦"
)

st.title("📦 Late Delivery Predictor")

st.write(
    "Use the AI-powered order investigation agent "
    "to analyze delivery risk."
)

form_url = "https://n8n-agent-app.reddune-eb2aebd8.westus2.azurecontainerapps.io/form/new-order-risk"

st.link_button(
    "🚀 Open Order Investigation Form",
    form_url,
    use_container_width=True
)

st.info(
    "The form is powered by your Azure-hosted n8n agent."
)
