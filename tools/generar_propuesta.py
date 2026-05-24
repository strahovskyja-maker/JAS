"""
Generador de propuestas de negocio en PDF para JAS.
Uso: python3 generar_propuesta.py propuesta.json
"""

import json
import sys
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, Image
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
LOGO_PATH   = os.path.join(PROJECT_DIR, "MEDCORE.png")

# Paleta MEDCORE
MEDCORE_BLUE   = colors.HexColor("#1A3C6E")
MEDCORE_LIGHT  = colors.HexColor("#D6E4F0")
MEDCORE_ACCENT = colors.HexColor("#2D7DD2")
GRAY_TEXT      = colors.HexColor("#4A4A4A")
LIGHT_GRAY     = colors.HexColor("#F4F6F8")
WHITE          = colors.white

PAGE_W = letter[0]
COL_W  = PAGE_W - 2 * inch   # 6.5 in


def styles():
    s = getSampleStyleSheet()

    s.add(ParagraphStyle("MC_Empresa",
        fontName="Helvetica-Bold", fontSize=20,
        textColor=MEDCORE_BLUE, leading=24, spaceAfter=2))

    s.add(ParagraphStyle("MC_Tagline",
        fontName="Helvetica", fontSize=10,
        textColor=MEDCORE_ACCENT, leading=13, spaceAfter=0))

    s.add(ParagraphStyle("MC_BandaTitulo",
        fontName="Helvetica-Bold", fontSize=16,
        textColor=WHITE, leading=22, spaceAfter=0))

    s.add(ParagraphStyle("MC_BandaMeta",
        fontName="Helvetica", fontSize=9,
        textColor=colors.HexColor("#BDD5EA"), leading=13, spaceAfter=0))

    s.add(ParagraphStyle("MC_SeccionTitulo",
        fontName="Helvetica-Bold", fontSize=10,
        textColor=WHITE, leading=14, spaceAfter=0))

    s.add(ParagraphStyle("MC_Cuerpo",
        fontName="Helvetica", fontSize=10,
        textColor=GRAY_TEXT, leading=16,
        alignment=TA_JUSTIFY, spaceAfter=0))

    s.add(ParagraphStyle("MC_Bullet",
        fontName="Helvetica", fontSize=10,
        textColor=GRAY_TEXT, leading=16,
        leftIndent=14, spaceAfter=0))

    s.add(ParagraphStyle("MC_TablaHeader",
        fontName="Helvetica-Bold", fontSize=9,
        textColor=MEDCORE_BLUE, leading=13))

    s.add(ParagraphStyle("MC_TablaBody",
        fontName="Helvetica", fontSize=9,
        textColor=GRAY_TEXT, leading=14))

    s.add(ParagraphStyle("MC_TablaTotal",
        fontName="Helvetica-Bold", fontSize=10,
        textColor=MEDCORE_BLUE, leading=14))

    s.add(ParagraphStyle("MC_FirmaLabel",
        fontName="Helvetica", fontSize=9,
        textColor=GRAY_TEXT, leading=13, spaceAfter=4))

    s.add(ParagraphStyle("MC_FirmaEmpresa",
        fontName="Helvetica", fontSize=9,
        textColor=MEDCORE_ACCENT, leading=13))

    return s


def banda(contenido_rows, bg=MEDCORE_BLUE, pad_top=10, pad_bot=10, pad_lat=14):
    t = Table(contenido_rows, colWidths=[COL_W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), bg),
        ("TOPPADDING",    (0, 0), (-1,  0), pad_top),
        ("BOTTOMPADDING", (0, -1), (-1, -1), pad_bot),
        ("TOPPADDING",    (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), pad_lat),
        ("RIGHTPADDING",  (0, 0), (-1, -1), pad_lat),
    ]))
    return t


def header_block(data, st):
    els = []

    if os.path.exists(LOGO_PATH):
        logo = Image(LOGO_PATH, width=1.9*inch, height=0.72*inch)
        logo.hAlign = "LEFT"
        els.append(logo)
    else:
        els.append(Paragraph("MEDCORE", st["MC_Empresa"]))
        els.append(Paragraph("Soluciones en Salud", st["MC_Tagline"]))

    els.append(Spacer(1, 10))

    fecha   = data.get("fecha", datetime.now().strftime("%d de %B de %Y"))
    cliente = data.get("cliente", "—")
    ref     = data.get("referencia", "—")
    titulo  = data.get("titulo", "Propuesta Comercial")

    els.append(banda([
        [Paragraph(titulo, st["MC_BandaTitulo"])],
        [Paragraph(
            f"<b>Para:</b> {cliente}&nbsp;&nbsp;·&nbsp;&nbsp;"
            f"<b>Fecha:</b> {fecha}&nbsp;&nbsp;·&nbsp;&nbsp;"
            f"<b>Ref:</b> {ref}",
            st["MC_BandaMeta"]
        )],
    ], pad_top=14, pad_bot=14))

    els.append(Spacer(1, 16))
    return els


def seccion_header(titulo, st):
    t = Table([[Paragraph(titulo.upper(), st["MC_SeccionTitulo"])]], colWidths=[COL_W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), MEDCORE_BLUE),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
    ]))
    return t


def render_texto(seccion, st):
    els = [seccion_header(seccion.get("titulo", ""), st), Spacer(1, 8)]
    contenido = seccion.get("contenido", "")
    if isinstance(contenido, str):
        lineas = contenido.split("\n")
    else:
        lineas = contenido

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            els.append(Spacer(1, 4))
            continue
        if linea.startswith("- ") or linea.startswith("• "):
            els.append(Paragraph(f"&bull;&nbsp; {linea[2:]}", st["MC_Bullet"]))
            els.append(Spacer(1, 3))
        else:
            els.append(Paragraph(linea, st["MC_Cuerpo"]))
            els.append(Spacer(1, 5))

    els.append(Spacer(1, 10))
    return els


def render_inversion(seccion, st):
    filas = seccion.get("filas", [])
    if not filas:
        return render_texto(seccion, st)

    els = [seccion_header(seccion.get("titulo", "Inversión"), st), Spacer(1, 8)]

    # Encabezado tabla
    data = [[
        Paragraph("Descripción",   st["MC_TablaHeader"]),
        Paragraph("Detalle",       st["MC_TablaHeader"]),
        Paragraph("Valor",         st["MC_TablaHeader"]),
    ]]
    for f in filas:
        data.append([
            Paragraph(f.get("descripcion", ""), st["MC_TablaBody"]),
            Paragraph(f.get("detalle", ""),     st["MC_TablaBody"]),
            Paragraph(f.get("valor", ""),        st["MC_TablaBody"]),
        ])

    total = seccion.get("total")
    if total:
        data.append([
            Paragraph("", st["MC_TablaBody"]),
            Paragraph("TOTAL", st["MC_TablaTotal"]),
            Paragraph(total,   st["MC_TablaTotal"]),
        ])

    col_w = [2.6*inch, 2.7*inch, 1.2*inch]
    t = Table(data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        # Encabezado
        ("BACKGROUND",    (0, 0), (-1, 0), MEDCORE_LIGHT),
        ("LINEBELOW",     (0, 0), (-1, 0), 1.2, MEDCORE_BLUE),
        # Filas alternas
        ("ROWBACKGROUNDS", (0, 1), (-1, -2 if total else -1), [WHITE, LIGHT_GRAY]),
        # Fila total
        ("BACKGROUND",    (0, -1), (-1, -1), MEDCORE_LIGHT) if total else ("SPAN", (0,0),(0,0)),
        ("LINEABOVE",     (0, -1), (-1, -1), 0.8, MEDCORE_ACCENT) if total else ("SPAN", (0,0),(0,0)),
        # General
        ("ALIGN",         (2, 0), (2, -1), "RIGHT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.3, colors.HexColor("#D0D0D0")),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ]))
    els.append(t)
    els.append(Spacer(1, 10))
    return els


CONDICIONES_SERVICIO = [
    ("Modalidad",          "Suscripción mensual."),
    ("Vigencia mínima",    "12 meses desde la fecha de activación del servicio."),
    ("Facturación",        "Mensual, dentro de los primeros 5 días hábiles de cada mes."),
    ("Plazo de pago",      "Mes anticipado dentro de los 5 días hábiles siguientes a la emisión de la factura."),
    ("Implementación",     "Configuración inicial y capacitación a usuarios en 1 semana."),
    ("Término anticipado", "Con aviso de 30 días corridos antes del siguiente período de facturación, transcurrida la vigencia mínima."),
]


def render_condiciones(seccion, st):
    els = [seccion_header(seccion.get("titulo", "Condiciones de Servicio"), st), Spacer(1, 8)]

    data = []
    for i, (cond, detalle) in enumerate(CONDICIONES_SERVICIO):
        bg = WHITE if i % 2 == 0 else LIGHT_GRAY
        data.append((
            Paragraph(f"<b>{cond}</b>", st["MC_TablaBody"]),
            Paragraph(detalle, st["MC_TablaBody"]),
            bg,
        ))

    for cond_p, detalle_p, bg in data:
        fila = Table([[cond_p, detalle_p]], colWidths=[1.9*inch, 4.6*inch])
        fila.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), bg),
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
            ("GRID",          (0, 0), (-1, -1), 0.3, colors.HexColor("#D0D0D0")),
        ]))
        els.append(fila)

    els.append(Spacer(1, 10))
    return els


def render_firma(st):
    els = [
        Spacer(1, 24),
        HRFlowable(width="100%", thickness=0.6, color=MEDCORE_LIGHT),
        Spacer(1, 12),
        Paragraph("Slds,", st["MC_FirmaLabel"]),
        Spacer(1, 6),
    ]
    if os.path.exists(LOGO_PATH):
        logo = Image(LOGO_PATH, width=1.5*inch, height=0.56*inch)
        logo.hAlign = "LEFT"
        els.append(logo)
        els.append(Spacer(1, 4))
    else:
        els.append(Paragraph("<b>MEDCORE</b>", st["MC_FirmaLabel"]))
    els.append(Paragraph("Equipo Comercial MEDCORE", st["MC_FirmaEmpresa"]))
    return els


def footer(canvas, doc):
    canvas.saveState()
    h = 0.32 * inch
    canvas.setFillColor(MEDCORE_BLUE)
    canvas.rect(0, 0, PAGE_W, h, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(WHITE)
    canvas.drawCentredString(
        PAGE_W / 2, 0.10 * inch,
        f"MEDCORE · GESTIA · Propuesta Confidencial · {datetime.now().year}"
    )
    canvas.drawRightString(
        PAGE_W - 0.5 * inch, 0.10 * inch,
        f"Página {doc.page}"
    )
    canvas.restoreState()


def generar_pdf(data: dict, output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=0.8 * inch,
        bottomMargin=0.7 * inch,
    )

    st   = styles()
    els  = header_block(data, st)

    for sec in data.get("secciones", []):
        tipo = sec.get("tipo", "texto")
        if tipo == "inversion":
            bloque = render_inversion(sec, st)
        elif tipo == "condiciones":
            bloque = render_condiciones(sec, st)
        else:
            bloque = render_texto(sec, st)
        els.append(KeepTogether(bloque))

    if data.get("cierre"):
        cierre_sec = {
            "tipo": "texto",
            "titulo": "Cierre",
            "contenido": data["cierre"],
        }
        els.append(KeepTogether(render_texto(cierre_sec, st)))

    els += render_firma(st)

    doc.build(els, onFirstPage=footer, onLaterPages=footer)
    print(f"✓ PDF generado: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 generar_propuesta.py propuesta.json")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)

    carpeta = os.path.join(PROJECT_DIR, "Propuestas")
    os.makedirs(carpeta, exist_ok=True)

    nombre = data.get("nombre_archivo", "propuesta") + ".pdf"
    output = os.path.join(carpeta, nombre)

    generar_pdf(data, output)
