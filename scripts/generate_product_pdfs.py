#!/usr/bin/env python3
"""Genera los PDFs entregables de los productos de Forj."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, KeepTogether)

BLACK = HexColor("#0a0a0a")
WHITE = HexColor("#ffffff")
GRAY = HexColor("#6b7280")
LIGHT = HexColor("#f5f5f5")
ACCENT = HexColor("#1a73e8")

OUT = os.path.join(os.path.dirname(__file__), "..", "media", "products")
os.makedirs(OUT, exist_ok=True)

H = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=22, leading=28,
                   textColor=BLACK, spaceBefore=6, spaceAfter=10)
H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=14, leading=18,
                    textColor=BLACK, spaceBefore=16, spaceAfter=6)
H3 = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11, leading=15,
                    textColor=ACCENT, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("b", fontName="Helvetica", fontSize=9.5, leading=14.5,
                      textColor=HexColor("#222"), alignment=TA_LEFT, spaceAfter=6)
BULLET = ParagraphStyle("bu", parent=BODY, leftIndent=14, bulletIndent=4, spaceAfter=3)
NOTE = ParagraphStyle("note", parent=BODY, fontSize=8.5, textColor=GRAY, leading=12.5)


def cover(doc, title, subtitle, items):
    frame = Frame(0, 0, A4[0], A4[1], id="cover", leftPadding=2.2*cm,
                  rightPadding=2.2*cm, topPadding=2.5*cm, bottomPadding=2*cm)
    frame.addToPage(doc)
    el = [
        Spacer(1, 3.5*cm),
        Paragraph("FORJ", ParagraphStyle("brand", fontName="Helvetica-Bold", fontSize=13,
                                         tracking=4, textColor=GRAY, spaceAfter=8)),
        Paragraph(title, ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=28,
                                        leading=34, textColor=BLACK, spaceAfter=10)),
        Paragraph(subtitle, ParagraphStyle("sub", fontName="Helvetica", fontSize=12,
                                           leading=17, textColor=GRAY, spaceAfter=26)),
    ]
    for label, txt in items:
        el.append(Paragraph(f"<b>{label}</b> — {txt}", ParagraphStyle(
            "it", fontName="Helvetica", fontSize=10, leading=15, textColor=HexColor("#333"),
            spaceAfter=6, leftIndent=10)))
    el.append(Spacer(1, 2*cm))
    el.append(Paragraph("© Forj — Infraestructura TI Profesional · forj.es",
                        NOTE))
    doc.build(el)


def page_template(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BLACK)
    canvas.rect(0, A4[1] - 0.9*cm, A4[0], 0.9*cm, stroke=0, fill=1)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(2.2*cm, A4[1] - 0.6*cm, "FORJ")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(A4[0] - 2.2*cm, A4[1] - 0.6*cm, doc.title or "")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(A4[0]/2, 1.1*cm, f"Página {doc.page}")
    canvas.restoreState()


def document(title, blocks):
    doc = BaseDocTemplate(os.path.join(OUT, "tmp.pdf"), pagesize=A4,
                          title=title, author="Forj",
                          leftMargin=2.2*cm, rightMargin=2.2*cm,
                          topMargin=2.2*cm, bottomMargin=2*cm)
    doc.title = title
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="pt", frames=[frame], onPage=page_template)])
    story = []
    for kind, *rest in blocks:
        if kind == "h1":
            story.append(Paragraph(rest[0], H))
        elif kind == "h2":
            story.append(KeepTogether([Paragraph(rest[0], H2)]))
        elif kind == "h3":
            story.append(Paragraph(rest[0], H3))
        elif kind == "p":
            story.append(Paragraph(rest[0], BODY))
        elif kind == "b":
            for line in rest[0]:
                story.append(Paragraph(f"<b>{line[0]}</b><br/>{line[1]}", BULLET))
        elif kind == "li":
            for line in rest[0]:
                story.append(Paragraph(f"&bull; {line}", BULLET))
        elif kind == "table":
            data = rest[0]
            fracs = [f[0] if f[1] is None else f[0] for f in rest[1]]
            total = sum(fracs)
            colw = [f * doc.width / total for f in fracs]
            t = Table(data, colWidths=colw)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), BLACK),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT]),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#d1d5db")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(Spacer(1, 4))
            story.append(t)
            story.append(Spacer(1, 10))
        elif kind == "page":
            story.append(PageBreak())
    doc.build(story)


def save(name):
    os.replace(os.path.join(OUT, "tmp.pdf"), os.path.join(OUT, name))
    print("OK", name)


# ============ 1. GUÍA INFRAESTRUCTURA TI ============
document("Guía: Infraestructura TI ideal para tu negocio", [
    ("h1", "Guía: Infraestructura TI ideal para tu negocio"),
    ("p", "Guía práctica para pymes que quieren una infraestructura TI fiable, segura y escalable sin gastar de más. Escrita por Dani Ramirez — Forj."),
    ("h2", "1. Redes WiFi: el cimiento de todo"),
    ("p", "Una red WiFi mal diseñada es la causa nº1 de incidencias en oficinas: conexiones que caen, videollamadas cortadas e impresoras inaccesibles. Antes de comprar un router potente, conviene diseñar la cobertura."),
    ("li", [
        "Estándar mínimo: WiFi 6 (802.11ax) para oficinas de más de 5 personas. WiFi 6E si trabajáis con muchos dispositivos simultáneos.",
        "Un punto de acceso por cada 10-15 usuarios o cada 60-80 m² de oficina abierta.",
        "Canalización: usa canales 1, 6 y 11 en 2.4 GHz (no se solapan); en 5/6 GHz el router se auto-configura.",
        "Seguridad: WPA3 obligatorio, con PSK para oficinas pequeñas y 802.1X (RADIUS) a partir de 25 empleados.",
        "Red de invitados separada (SSID propio, sin acceso a la red interna) — imprescindible.",
        "VLAN de VoIP: los teléfonos IP en una VLAN aparte evitan que el tráfico de voz compita con las descargas.",
    ]),
    ("h2", "2. Cableado estructurado: la inversión que dura 20 años"),
    ("p", "El cableado es la única parte de la infraestructura que no se actualiza cada 3-4 años. Una instalación bien hecha hoy sigue funcionando dentro de dos décadas."),
    ("li", [
        "Categoría mínima recomendada: Cat 6 (1 Gbps garantizado a 100 m). Si pensáis en 10 Gbps a medio plazo, Cat 6A.",
        "Certificación: toda instalación debe entregarse certificada (test de fluke con informe), no solo 'probada'.",
        "Fibra óptica en el backbone: entre plantas o edificios siempre fibra, el cobre se queda para los puestos.",
        "Organización: bandejas, canaletas y etiquetado con la norma ANSI/TIA-606. Un armario sin etiquetar es un cajón de sastre.",
        "Presupuesto extra del 20-30%: carril de reserva en cada cajetín para el futuro (siempre crece).",
        "Armario de comunicaciones: 2-3 U de reserva, ventilación y una toma dedicada para el SAI.",
    ]),
    ("h2", "3. Servidores y NAS: centralizar en vez de dispersar"),
    ("p", "El error más común en pymes: cada empleado guarda los archivos en su portátil. Centralizar los datos en un NAS o servidor da control, copias y seguridad."),
    ("li", [
        "NAS (Synology, QNAP) es suficiente para oficinas de hasta 50 personas: archivos, copias de seguridad y algunos contenedores.",
        "RAID no es copia de seguridad: RAID protege contra fallos de disco, no contra borrados, ransomware ni incendios. Necesitáis ambos.",
        "Acceso remoto seguro: VPN WireGuard o Tailscale; nunca exponer el NAS directamente a Internet.",
        "Activos en red vs. usuarios: un servidor 'de verdad' (virtualizado con Proxmox/ESXi) merece la pena a partir de 30-40 usuarios o con aplicaciones de gestión.",
        "Estructura de carpetas: definir permisos por departamento (finanzas, RRHH, dirección) desde el primer día.",
        "Monitorización básica: alerta de disco lleno, SMART status y temperatura. Un script simple ahorra sustos.",
    ]),
    ("h2", "4. Copias de seguridad: la regla 3-2-1"),
    ("p", "El 60% de las pymes que sufren pérdida total de datos cierra en los 18 meses siguientes. Las copias no son negociables."),
    ("li", [
        "3 copias de tus datos, en 2 soportes distintos, 1 fuera de la oficina (regla 3-2-1).",
        "Copia local (NAS o disco) + copia en la nube (Backblaze, Wasabi, S3) cifrada.",
        "Backups automatizados y verificados: una copia que no se prueba no existe.",
        "Ransomware: la copia fuera de línea debe tener versionado inmutable (immutable backups).",
        "Restauración probada al menos una vez al trimestre, midiendo tiempo real de recuperación.",
        "Política de retención: diaria 7 días, semanal 4 semanas, mensual 12 meses.",
    ]),
    ("h2", "5. Checklist de implementación"),
    ("table", [
        ["Área", "Tarea", "Estado"],
        ["WiFi", "Diseño de cobertura con APs suficientes y canales planificados", "☐"],
        ["WiFi", "WPA3 activado, red de invitados separada, VLAN VoIP", "☐"],
        ["Cableado", "Cat 6/A certificado con informe, etiquetado ANSI/TIA-606", "☐"],
        ["Cableado", "Fibra en backbone y reserva del 20-30% en cajetines", "☐"],
        ["Servidores", "NAS/servidor centralizado con permisos por departamento", "☐"],
        ["Servidores", "VPN de acceso remoto (WireGuard/Tailscale), sin exposición pública", "☐"],
        ["Backups", "Regla 3-2-1: local + nube cifrada + retención definida", "☐"],
        ["Backups", "Restauración probada y documentada (trimestral)", "☐"],
        ["Seguridad", "Firewall actualizado, router admin por HTTPS, contraseñas fuertes", "☐"],
        ["Seguridad", "Política de contraseñas y 2FA en cuentas críticas", "☐"],
        ["Mantenimiento", "Monitorización de discos y alertas (SMART, temperatura)", "☐"],
        ["Mantenimiento", "Calendario de actualizaciones mensuales documentado", "☐"],
    ], [(0.28, None), (0.6, None), (0.12, None)]),
    ("h2", "6. Errores que cuestan dinero"),
    ("li", [
        "Comprar el router más caro del mercado en vez de diseñar cobertura con varios AP.",
        "Cableado sin certificar: 'funciona' hoy y falla el día que más lo necesitas.",
        "Confiar en que el disco de un empleado guarda los datos de la empresa.",
        "Exponer el NAS al exterior para 'acceder desde casa' sin VPN.",
        "No tener contraseña en la BIOS/UEFI ni cifrado de disco (BitLocker/FileVault).",
        "Actualizar servidores en horario laboral sin plan de rollback.",
    ]),
    ("h2", "7. Resumen ejecutivo"),
    ("p", "Una infraestructura TI correcta no es la más cara: es la que está diseñada, documentada y mantenida. WiFi planificado, cableado certificado, datos centralizados y backups que se prueban: con eso se resuelve el 90% de las incidencias que sufren las pymes. Para el resto (auditorías, proyectos o mantenimiento), Forj está a un correo de distancia."),
])

save("guia-infraestructura-ti.pdf")

# ============ 2. PLANTILLA POLÍTICA SEGURIDAD ============
document("Plantilla: Política de seguridad TI", [
    ("h1", "Plantilla: Política de seguridad TI"),
    ("p", "Documento editable para definir la política de seguridad informática de tu empresa. Completa los campos entre corchetes [ ] con los datos de tu organización y hazlo aprobar por dirección."),
    ("h2", "1. Propósito"),
    ("p", "Esta política define las normas de uso y protección de los sistemas de información de [nombre de la empresa]. Su objetivo es proteger la confidencialidad, integridad y disponibilidad de los datos de la organización, sus clientes y empleados."),
    ("h2", "2. Alcance"),
    ("p", "Aplica a todos los empleados, contratistas y terceros con acceso a los sistemas, redes, equipos y datos de [nombre de la empresa], así como a cualquier dispositivo personal usado para fines laborales (BYOD)."),
    ("h2", "3. Contraseñas y autenticación"),
    ("li", [
        "Longitud mínima de 12 caracteres, con gestor de contraseñas corporativo.",
        "Prohibido reutilizar contraseñas entre cuentas personales y corporativas.",
        "2FA (doble factor) obligatorio en correo, acceso remoto y administración.",
        "Cambio de contraseña inmediato ante sospecha de compromiso.",
        "Las cuentas de administración nunca se comparten y se auditan trimestralmente.",
    ]),
    ("h2", "4. Accesos y permisos"),
    ("li", [
        "Principio de mínimo privilegio: cada persona solo accede a lo necesario para su puesto.",
        "Revisión de permisos al cambiar de rol y baja inmediata de accesos al salir de la empresa.",
        "Acceso remoto únicamente mediante VPN corporativa aprobada.",
        "Acceso de terceros (proveedores): temporal, por proyecto, con aprobación de dirección.",
    ]),
    ("h2", "5. Protección de datos (RGPD)"),
    ("li", [
        "Los datos personales solo se tratan para finalidades legítimas y documentadas.",
        "Cifrado de datos personales en reposo y en tránsito.",
        "Derechos ARCO (acceso, rectificación, cancelación, oposición): canal único de solicitudes.",
        "Registro de actividades de tratamiento actualizado.",
        "Notificación de brechas a la AEPD en menos de 72 horas si hay riesgo.",
    ]),
    ("h2", "6. Correo electrónico y phishing"),
    ("li", [
        "Nunca enviar contraseñas, datos bancarios o documentos sensibles por correo sin cifrado.",
        "Ante correos sospechosos: no pinchar enlaces, no descargar adjuntos, reportar al responsable.",
        "Prohibido usar el correo corporativo para cuentas personales o suscripciones ajenas al negocio.",
        "Filtros antispam y anti-phishing activados a nivel de dominio.",
    ]),
    ("h2", "7. Uso aceptable de Internet y dispositivos"),
    ("li", [
        "Uso ocasional y razonable de Internet personal, nunca para actividades ilegales.",
        "Descargas de software solo desde fuentes oficiales y con aprobación.",
        "Los portátiles corporativos se entregan con cifrado de disco activo (BitLocker/FileVault).",
        "Prohibido instalar software no aprobado en equipos corporativos.",
    ]),
    ("h2", "8. Copias de seguridad"),
    ("li", [
        "Copia diaria de datos críticos, verificación semanal y prueba de restauración trimestral.",
        "Copia fuera de línea o inmutable protegida frente a ransomware.",
        "Responsable de backups: [nombre/cargo].",
    ]),
    ("h2", "9. Gestión de incidentes"),
    ("li", [
        "Todo incidente de seguridad se reporta al responsable de TI en < 1 hora.",
        "Clasificación: bajo / medio / alto / crítico, con tiempos de respuesta definidos.",
        "Registro de incidentes con lecciones aprendidas.",
        "Contacto de emergencia: [teléfono / email del responsable].",
    ]),
    ("h2", "10. Aprobación"),
    ("table", [
        ["Cargo", "Nombre", "Firma", "Fecha"],
        ["Dirección", "", "", ""],
        ["Responsable TI", "", "", ""],
        ["RRHH", "", "", ""],
    ], [(0.25, None), (0.3, None), (0.25, None), (0.2, None)]),
    ("p", "Documento modelo de Forj. Personalízalo y adáptalo a tu organización; un profesional puede revisarlo en [1 hora de consultoría]."),
])
save("plantilla-politica-seguridad.pdf")

# ============ 3. AUDITORÍA RED WIFI ============
document("Auditoría de red WiFi — Documento de preparación", [
    ("h1", "Auditoría de red WiFi"),
    ("p", "Este documento describe qué incluye tu auditoría de red WiFi, qué necesitamos preparar antes de la visita y cómo leerás el informe final."),
    ("h2", "1. Qué incluye la auditoría"),
    ("li", [
        "Estudio de cobertura in situ: mapa térmico de señal en todas las zonas de trabajo.",
        "Análisis de interferencias: canales ocupados, redes vecinas y ruido de RF.",
        "Test de rendimiento: velocidad real por zona, latencia y pérdida de paquetes.",
        "Revisión de seguridad: cifrado, contraseñas, red de invitados, vulnerabilidades.",
        "Inventario de hardware: APs, switches, router, cableado y antigüedad.",
        "Informe final con hallazgos priorizados (crítico / medio / bajo) y plan de mejora.",
    ]),
    ("h2", "2. Antes de la visita (cuestionario)"),
    ("li", [
        "Plano en planta de la oficina (PDF o foto).",
        "Nº de empleados y dispositivos conectados simultáneamente.",
        "¿Dónde notáis más problemas? (salas de reuniones, almacén, terraza...).",
        "Modelos de router/APs actuales y su antigüedad.",
        "¿Hay aplicaciones críticas en red? (VoIP, impresión, ERP).",
        "Horario y zonas donde se realiza la medición.",
    ]),
    ("h2", "3. Cómo se realiza"),
    ("p", "Un técnico de Forj acude a vuestras instalaciones con equipo de medición profesional (analizador de espectro y antenas calibradas). Se recorre toda la superficie con el equipamiento de medición, se registran los datos en tiempo real y se realizan los test de rendimiento en los puntos de trabajo habituales. La visita dura entre 1,5 y 3 horas según el tamaño de las instalaciones."),
    ("h2", "4. Qué recibes"),
    ("li", [
        "Informe PDF con mapa térmico de cobertura y análisis de interferencias.",
        "Resultados de los test de rendimiento por zona.",
        "Lista de vulnerabilidades detectadas (seguridad WiFi).",
        "Plan de mejora priorizado con presupuesto estimado por opción.",
        "Recomendaciones de configuración aplicables sin obra (canales, potencia, QoS).",
    ]),
    ("h2", "5. Después de la auditoría"),
    ("p", "Tras la entrega del informe, dispones de una sesión de 30 minutos para resolver dudas. Si decides ejecutar las mejoras, los cambios de configuración se aplican en el mismo informe se priorizan y se puede contratar la implantación por separado con condiciones preferentes."),
])
save("auditoria-red-wifi.pdf")

# ============ 4. CHECKLIST ONBOARDING TI ============
document("Checklist: Onboarding TI de empleados", [
    ("h1", "Checklist: Onboarding TI de empleados"),
    ("p", "Lista completa para incorporar a un nuevo empleado en tiempo récord y sin agujeros de seguridad. Úsala en cada alta: marca cada casilla y archívala como registro."),
    ("h2", "1. Antes del primer día (D-7)" ),
    ("li", [
        "☐ Alta del puesto en el directorio de la empresa (AD/Google Workspace/Microsoft 365).",
        "☐ Creación de cuenta de correo corporativa con contraseña temporal segura.",
        "☐ Asignación de licencias de software necesarias (Office, diseño, ERP...).",
        "☐ Preparación del equipo: imagen limpia, actualizaciones y cifrado de disco.",
        "☐ Alta del equipo en el inventario TI con número de serie y responsable.",
        "☐ Petición de accesos a las aplicaciones internas según su departamento.",
        "☐ Tarjeta de acceso a la oficina / llaves / plazas de parking, si aplica.",
    ]),
    ("h2", "2. Primer día"),
    ("li", [
        "☐ Entrega del equipo: portátil, cargador, dock, pantalla y teclado si aplica.",
        "☐ Primer inicio de sesión: comprobar que el correo y la VPN funcionan.",
        "☐ Cambio de contraseña temporal (y activación de 2FA si es aplicable).",
        "☐ Conexión a la red WiFi corporativa (y a la de invitados explicada como NO usar).",
        "☐ Configuración de firma de correo con plantilla corporativa.",
        "☐ Configuración de impresora y carpetas compartidas de su departamento.",
        "☐ Breve formación de seguridad: phishing, contraseñas, política de uso.",
        "☐ Confirmar que conoce el canal de soporte TI (email/WhatsApp/portal).",
    ]),
    ("h2", "3. Semana 1"),
    ("li", [
        "☐ Revisión de permisos: ¿accede a todo lo que necesita su puesto?",
        "☐ Formación en las herramientas internas (ERP, gestión de clientes...).",
        "☐ Configuración del teléfono móvil corporativo o BYOD (MDM) si aplica.",
        "☐ Alta en los grupos de comunicación del equipo.",
        "☐ Comprobar que las reuniones y calendario compartido funcionan.",
    ]),
    ("h2", "4. Mes 1"),
    ("li", [
        "☐ Revisión final de accesos según las tareas reales del puesto.",
        "☐ Feedback de la experiencia de onboarding con el departamento de TI.",
        "☐ Archivar el registro completo de alta en el sistema de RRHH.",
        "☐ Definir fecha de revisión de permisos trimestral.",
    ]),
    ("h2", "5. Baja de empleados (para el mismo checklist)"),
    ("li", [
        "☐ Desactivar cuenta de correo y accesos el mismo día de la baja.",
        "☐ Recogida del equipo y verificación de inventario.",
        "☐ Revisar y conservar correos y archivos de su buzón según la política.",
        "☐ Transferir propietarios de documentos y carpetas.",
        "☐ Revocar tarjetas de acceso y claves físicas.",
        "☐ Registrar la baja y sus pasos en el inventario TI.",
    ]),
    ("p", "Plantilla de Forj. Añade las tareas específicas de tu empresa y adáptala a tus herramientas (Microsoft 365, Google Workspace, Entra ID...)."),
])
save("checklist-onboarding-ti.pdf")

# ============ 5. CONSULTORÍA TI 1 HORA ============
document("Consultoría TI — Briefing previo a la sesión", [
    ("h1", "Consultoría TI (1 hora) — Briefing"),
    ("p", "Para sacar el máximo partido a tu hora de consultoría, dedica 10 minutos a completar este briefing. Cuanto mejor definamos el problema, más soluciones concretas saldrán de la sesión."),
    ("h2", "1. Datos de la empresa"),
    ("table", [
        ["Dato", "Respuesta"],
        ["Nombre de la empresa", ""],
        ["Nº de empleados", ""],
        ["Sector", ""],
        ["Ciudad", ""],
        ["¿Trabajáis en oficina, remoto o híbrido?", ""],
    ], [(0.45, None), (0.55, None)]),
    ("h2", "2. Objetivo de la sesión (elige el principal)"),
    ("li", [
        "Resolver un problema concreto (red, servidores, correo, ciberseguridad...).",
        "Diseñar la infraestructura desde cero (nueva oficina / mudanza).",
        "Optimizar costes o rendimiento de la infraestructura actual.",
        "Preparar una decisión de compra (NAS, servidor, wifi, contratos).",
        "Ciberseguridad: qué nos falta y por dónde empezar.",
        "Otra: ______________________________",
    ]),
    ("h2", "3. Describe tu situación actual"),
    ("p", "¿Qué tenéis hoy? (router, APs, servidor/NAS, nube...). Incluye marca/modelo si lo sabes y el año aproximado de instalación."),
    ("p", "...................................................................................................................."),
    ("h2", "4. Qué problemas estáis notando"),
    ("li", [
        "Caídas o lentitud en ciertas zonas / a ciertas horas.",
        "Videollamadas que se cortan, impresoras que 'desaparecen'.",
        "Miedo al ransomware / recibimos un ataque de phishing.",
        "Los archivos están repartidos en los portátiles.",
        "Mudanza / ampliación / nueva sede en [fecha].",
        "Otros: ______________________________",
    ]),
    ("h2", "5. Qué esperas llevarte"),
    ("p", "Al final de la sesión tendrás: diagnóstico del problema, plan de acción priorizado con presupuestos orientativos y una lista de compras concreta (modelos y precios aproximados)."),
    ("h2", "6. Cómo se desarrolla la sesión"),
    ("li", [
        "0-5 min: presentación y repaso del briefing.",
        "5-40 min: análisis de tu situación y preguntas específicas.",
        "40-55 min: recomendaciones y plan de acción por prioridades.",
        "55-60 min: resumen, próximos pasos y qué puedes hacer tú mismo.",
    ]),
    ("p", "Tras la sesión recibirás un resumen por email con las conclusiones y las acciones acordadas, para que no dependas de tus apuntes."),
])
save("consultoria-ti-1h.pdf")

print("PDFs generados en", os.path.abspath(OUT))
