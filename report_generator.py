from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

def make_report(title, students, aim, cell, e0, observation, conclusion):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CenterTitle", parent=styles["Title"], alignment=TA_CENTER, fontSize=19, leading=24))
    styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], textColor=colors.HexColor("#0f766e"), spaceBefore=12, spaceAfter=7))

    story = []
    story.append(Paragraph(title, styles["CenterTitle"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("Virtual Electrochemistry Laboratory Report", styles["Heading3"]))
    story.append(Spacer(1, 10))

    student_rows = [["Student", "Name", "Registration No."]]
    idx = 1
    for name, reg in students:
        if name:
            student_rows.append([f"Student {idx}", name, reg or ""])
            idx += 1
    t = Table(student_rows, colWidths=[75, 220, 150])
    t.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.6,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#dff3f1")),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("PADDING",(0,0),(-1,-1),7),
    ]))
    story.append(t)

    story.append(Paragraph("1. Aim", styles["Section"]))
    story.append(Paragraph(aim, styles["BodyText"]))

    story.append(Paragraph("2. Theory", styles["Section"]))
    story.append(Paragraph(
        "A galvanic cell converts chemical energy into electrical energy through a spontaneous redox reaction. "
        "Oxidation occurs at the anode and reduction occurs at the cathode. The cell potential can be related to "
        "thermodynamic free energy using ΔG = −nFE. Under non-standard conditions, the Nernst equation is used "
        "to determine the cell potential.",
        styles["BodyText"]
    ))

    story.append(Paragraph("3. Experimental Setup / Virtual Cell", styles["Section"]))
    story.append(Paragraph(f"Selected cell notation: <b>{cell}</b>", styles["BodyText"]))
    story.append(Paragraph(f"Standard cell potential entered: <b>{e0:.3f} V</b>", styles["BodyText"]))

    story.append(Paragraph("4. Nernst Equation", styles["Section"]))
    story.append(Paragraph("E = E° − (RT/nF) ln Q", styles["BodyText"]))
    story.append(Paragraph(
        "The Nernst module in the website allows the user to change E°, n, Q and temperature and calculate E.",
        styles["BodyText"]
    ))

    story.append(Paragraph("5. Gibbs Free Energy", styles["Section"]))
    story.append(Paragraph("ΔG = −nFE", styles["BodyText"]))
    story.append(Paragraph(
        "A positive cell potential gives negative ΔG for the reaction written in the spontaneous direction.",
        styles["BodyText"]
    ))

    story.append(Paragraph("6. Observation", styles["Section"]))
    story.append(Paragraph(observation, styles["BodyText"]))

    story.append(Paragraph("7. Result", styles["Section"]))
    story.append(Paragraph(
        "The virtual electrochemistry experiment was completed successfully using the E-CELL modules.",
        styles["BodyText"]
    ))

    story.append(Paragraph("8. Conclusion", styles["Section"]))
    story.append(Paragraph(conclusion, styles["BodyText"]))

    story.append(Spacer(1, 24))
    story.append(Paragraph("Generated using E-CELL Virtual Electrochemistry Lab", styles["CenterTitle"]))
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
