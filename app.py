import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="LLM Security Research",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 LLM Security Research Platform")

st.markdown("""
Explore real-world LLM jailbreak research datasets
and analyse AI model security.
""")

file = "jailbreak_dataset.csv"

if os.path.exists(file):

    df = pd.read_csv(file)

    st.success("Dataset loaded successfully!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(df))
    col2.metric("Total Columns", len(df.columns))

    size = os.path.getsize(file) / (1024 * 1024)
    col3.metric("Dataset Size", f"{size:.2f} MB")

    st.divider()

    st.subheader("Dataset Explorer")

    search = st.text_input("Search dataset")

    if search:
        mask = df.astype(str).apply(
            lambda col: col.str.contains(
                search, case=False, na=False
            )
        ).any(axis=1)

        filtered = df[mask]
    else:
        filtered = df

    st.dataframe(
        filtered.head(100),
        use_container_width=True
    )

    st.download_button(
        "Download Dataset CSV",
        data=df.to_csv(index=False),
        file_name="jailbreak_dataset.csv",
        mime="text/csv"
    )

else:
    st.error("Dataset not found!")