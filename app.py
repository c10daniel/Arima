
import streamlit as st
import nbformat
from nbconvert import HTMLExporter
from weasyprint import HTML
from pathlib import Path

st.title("ARIMA Forecasting Notebook")
st.write("Generate a PDF of my ARIMA analysis.")

notebooks = list(Path(".").glob("*.ipynb"))

if not notebooks:
    st.error("No notebook found in the repository.")
else:
    notebook_path = notebooks[0]
    st.write(f"Notebook: {notebook_path.name}")

    if st.button("Generate PDF"):
        with st.spinner("Creating PDF..."):
            try:
                nb = nbformat.read(
                    str(notebook_path), as_version=4
                )

                exporter = HTMLExporter()
                html, _ = exporter.from_notebook_node(nb)

                pdf = HTML(
                    string=html,
                    base_url=str(Path(".").resolve())
                ).write_pdf()

                st.download_button(
                    "Download ARIMA PDF",
                    data=pdf,
                    file_name="ARIMA_Analysis.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"PDF generation failed: {e}")
