from __future__ import annotations

import html
from io import BytesIO

import streamlit as st

# ----------------------------
# Copy to clipboard
# ----------------------------

def copy_to_clipboard(text: str) -> None:
    """
    Renders a client-side copy-to-clipboard button.
    Uses the browser clipboard API (no re-run, no server roundtrip).
    """
    escaped = html.escape(text).replace("\n", "\\n")

    st.markdown(
        f"""
        <button
            onclick="navigator.clipboard.writeText(`{escaped}`)"
            style="
                background:#EEF2FF;
                border:1px solid #CBD5E1;
                padding:6px 12px;
                border-radius:8px;
                cursor:pointer;
                font-size:13px;
                width:100%;
            ">
            📋 Copy to clipboard
        </button>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------
# Word (.docx) export
# ----------------------------

def download_word(text: str, filename: str) -> None:
    """
    Generates a Word document from plain text.
    Each newline becomes a paragraph.
    """
    from docx import Document

    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.download_button(
        label="⬇️ Download Word",
        data=buffer,
        file_name=f"{filename}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        use_container_width=True,
    )


# ----------------------------
# PDF export
# ----------------------------

def download_pdf(text: str, filename: str) -> None:
    """
    Generates a clean, text-first PDF suitable for sharing and governance.
    """
    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4

    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()
    story = []

    for line in text.split("\n"):
        safe_line = html.escape(line)
        story.append(Paragraph(safe_line, styles["Normal"]))

    doc.build(story)
    buffer.seek(0)

    st.download_button(
        label="⬇️ Download PDF",
        data=buffer,
        file_name=f"{filename}.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
