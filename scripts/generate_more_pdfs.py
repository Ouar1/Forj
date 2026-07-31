#!/usr/bin/env python3
"""Genera los PDFs de los 20 productos nuevos de Forj."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_product_pdfs import document, save  # noqa: E402

# ============ GUÍAS ============

document("Guía: Ciberseguridad para pymes", [
    ("h1", "Guía: Ciberseguridad para pymes"),
    ("p", "Plan práctico de ciberseguridad para empresas de 5 a 50 empleados. Qué hacer primero, en qué invertir y cómo evitar el 90% de los ataques más comunes."),
    ("h2", "1. El riesgo real (y qué pagan las pymes)"),
    ("li", [
        "El 43% de los ciberataques van dirigidos a pymes; la mayoría sobreviven menos de un año tras perder sus datos.",
        "El vector nº1 es el phishing por email; el nº2, los accesos con contraseñas débiles o reutilizadas.",
        "Un ransomware medio pide 10.000-50.000€ a una pyme; sin backups, pagar no garantiza nada.",
        "La ciberseguridad no es opcional: el RGPD obliga a proteger los datos de clientes y empleados.",
    ]),
    ("h2", "2. Las 5 medidas que más reducen el riesgo (por orden)"),
    ("li", [
        "1. 2FA en todo: email, banca online, accesos remotos y paneles de administración.",
        "2. Backups 3-2-1: 3 copias, 2 soportes, 1 fuera de línea, con prueba de restauración.",
        "3. Gestor de contraseñas corporativo: fin de las contraseñas reutilizadas.",
        "4. Actualizaciones automáticas en todos los equipos y software (incluido el antivirus).",
        "5. Firewall con filtrado y red WiFi con WPA3 y red de invitados separada.",
    ]),
    ("h2", "3. Phishing: cómo funciona y cómo defenderse"),
    ("li", [
        "Regla de oro: nunca se pincha un enlace ni se descarga un adjunto de un correo inesperado.",
        "Verificar el remitente real: el nombre mostrado puede ser falso, el dominio no.",
        "Urgencia = sospecha: 'tu cuenta se cerrará en 24h' es la firma del phishing.",
        "Formación breve a empleados (20 min) al entrar y refresco anual: reduce el riesgo un 60%.",
        "Sistema de reporte: un botón 'reportar phishing' en el correo corporativo.",
    ]),
    ("h2", "4. Accesos y privilegios"),
    ("li", [
        "Mínimo privilegio: nadie tiene más permisos de los que necesita para su puesto.",
        "Cuentas de administrador solo para administradores, nunca para uso diario.",
        "Baja de empleados: desactivar accesos el mismo día (ver el kit de baja).",
        "Revisar permisos trimestralmente: empleados que cambian de rol arrastran accesos viejos.",
    ]),
    ("h2", "5. Presupuesto orientativo (pymes)"),
    ("table", [
        ["Medida", "Coste típico", "Riesgo que cubre"],
        ["2FA + gestor de contraseñas", "5-15€/usuario/año", "Robo de credenciales"],
        ["Backups 3-2-1 con nube", "30-80€/mes", "Ransomware, borrados"],
        ["Firewall de nueva generación", "300-900€ una vez", "Exposición externa"],
        ["Formación anti-phishing", "5-10€/usuario/año", "Ingeniería social"],
        ["Auditoría anual de seguridad", "300-800€", "Fugas de configuración"],
    ], [(0.4, None), (0.3, None), (0.3, None)]),
    ("h2", "6. Plan de acción 30 días"),
    ("li", [
        "Semana 1: activar 2FA en todas las cuentas críticas y el gestor de contraseñas.",
        "Semana 2: configurar backups 3-2-1 y probar una restauración real.",
        "Semana 3: actualizar todos los equipos, router y firewalls; desactivar accesos obsoletos.",
        "Semana 4: formación anti-phishing a todo el equipo y documentar el plan de incidentes.",
    ]),
])
save("guia-ciberseguridad-pymes.pdf")

document("Guía: Migración a Microsoft 365 o Google Workspace", [
    ("h1", "Guía: Migración a Microsoft 365 / Google Workspace"),
    ("p", "Todo lo necesario para mover tu empresa al correo y la nube corporativa sin perder un solo email, sin downtime y sin pagar de más."),
    ("h2", "1. ¿Microsoft 365 o Google Workspace?"),
    ("table", [
        ["Criterio", "Microsoft 365", "Google Workspace"],
        ["Correo corporativo", "Outlook", "Gmail"],
        ["Aplicaciones", "Word, Excel, PowerPoint, Teams", "Docs, Sheets, Slides, Meet"],
        ["Precio base", "8,8€/usuario/mes (Basic)", "7,2€/usuario/mes (Starter)"],
        ["Pymes que usan Microsoft en su día a día", "Ideal", "Menos natural"],
        ["Colaboración simple y barata", "Buena", "Ideal"],
        ["Dominio propio", "Sí", "Sí"],
    ], [(0.35, None), (0.33, None), (0.32, None)]),
    ("h2", "2. Preparación antes de migrar"),
    ("li", [
        "Auditar el correo actual: nº de cuentas, tamaño de buzones, cuentas compartidas (info@, ventas@).",
        "Elegir el plan: compara precios reales por usuario y las limitaciones de almacenamiento.",
        "Comprar el dominio si aún no lo tienes (mejor en Ionos/Dondominio que en el proveedor).",
        "Verificar que el dominio no está bloqueado por listas negras de spam (check MX).",
        "Decidir qué hacer con el correo antiguo: migrar buzones completos o solo los últimos 12 meses.",
    ]),
    ("h2", "3. La migración paso a paso"),
    ("li", [
        "1. Configurar el dominio en el nuevo proveedor (DNS: MX, SPF, DKIM, DMARC).",
        "2. Crear las cuentas de usuarios con las contraseñas temporales.",
        "3. Migrar buzones con la herramienta oficial (MigrationWiz, IMAP sync o nativa).",
        "4. Migrar contactos y calendarios por usuario.",
        "5. Probar el envío/recepción con el nuevo sistema (puede tardar 24-72h en converger DNS).",
        "6. Redirigir el correo antiguo durante 1-2 semanas para no perder nada.",
        "7. Dar de baja las cuentas antiguas solo al final.",
    ]),
    ("h2", "4. Errores que arruinan la migración"),
    ("li", [
        "No configurar SPF/DKIM antes de migrar → los correos caen en spam.",
        "Olvidar las cuentas compartidas (info@, admin@) o los alias.",
        "Migrar sin probar la restauración de un buzón completo.",
        "No comunicar el cambio a clientes y proveedores con aviso previo.",
        "Mantener el correo antiguo pagando de más durante meses por inercia.",
    ]),
    ("h2", "5. Checklist post-migración"),
    ("li", [
        "☐ Correos de prueba enviados y recibidos desde y hacia clientes.",
        "☐ Firma corporativa configurada en todos los usuarios.",
        "☐ 2FA activado en todas las cuentas.",
        "☐ Antivirus y gestión de dispositivos (MDM) conectados.",
        "☐ Copia de seguridad del buzón (backup de correo aparte del proveedor).",
        "☐ Formación básica de 30 min al equipo.",
    ]),
])
save("guia-migracion-365.pdf")

document("Manual: Teletrabajo seguro", [
    ("h1", "Manual: Teletrabajo seguro"),
    ("p", "Guía práctica para que tus empleados trabajen desde casa sin poner en riesgo los datos de la empresa. Ideal para repartir con el equipo."),
    ("h2", "1. La conexión: empieza por la VPN"),
    ("li", [
        "Todo acceso a los recursos internos (carpetas, ERP, servidores) debe pasar por VPN corporativa.",
        "VPN recomendadas: WireGuard (rápida), Tailscale (simple), OpenVPN (compatible).",
        "Prohibido exponer el NAS o el servidor directamente a Internet para 'acceder desde casa'.",
        "La VPN de casa (del router) no sirve: hace falta la VPN de la empresa.",
    ]),
    ("h2", "2. El equipo: portátiles y datos"),
    ("li", [
        "Cifrado de disco obligatorio: BitLocker (Windows) o FileVault (Mac).",
        "Pantalla bloqueada con contraseña al dejar el portátil (Win+L / Ctrl+Cmd+Q).",
        "No guardar archivos de empresa en el disco local 'de toda la vida': siempre en las carpetas de red.",
        "USB personales: solo con aprobación y escaneados.",
        "Actualizaciones activadas: el equipo de casa también se actualiza solo.",
    ]),
    ("h2", "3. Las videollamadas y el 'hombro indiscreto'"),
    ("li", [
        "Trabajar en un espacio donde no se vea la pantalla desde la ventana ni el pasillo.",
        "Silenciar el micrófono fuera de turno de palabra.",
        "Cuidado con los chats de soporte que piden contraseñas: verificar siempre por otro canal.",
        "Nunca compartir pantalla de la bandeja de entrada ni de la carpeta de RRHH.",
    ]),
    ("h2", "4. Wifi doméstico"),
    ("li", [
        "Cambiar la contraseña del wifi de casa si hay visitas o vecinos con acceso.",
        "Separar la red de invitados del wifi principal en casa (como en la oficina).",
        "Router doméstico actualizado; si es antiguo, considerar uno con WiFi 6.",
        "Si el trabajo es crítico, contratar fibra simétrica (subida ≥ 300 Mbps).",
    ]),
    ("h2", "5. Qué hacer ante un incidente en casa"),
    ("li", [
        "Correo sospechoso: no pinchar, reportar al responsable TI de inmediato.",
        "Portátil perdido o robado: avisar a TI en la hora siguiente (se borrará remotamente).",
        "Ransomware: desconectar el equipo de la red y avisar; NO pagar sin consultar.",
        "Acceso remoto de terceros (soporte): solo desde canales oficiales de la empresa.",
    ]),
])
save("manual-teletrabajo-seguro.pdf")

document("Guía: Elegir proveedor de internet empresarial", [
    ("h1", "Guía: Elegir proveedor de internet empresarial"),
    ("p", "Cómo elegir la conexión de fibra y el proveedor adecuados para tu empresa sin pagar de más ni quedarte corto."),
    ("h2", "1. Qué necesitas medir"),
    ("li", [
        "Subida: tan importante como la bajada si trabajáis con la nube, videollamadas o backups.",
        "Latencia: crítica para VoIP y ERP en la nube; por debajo de 10 ms en fibra.",
        "Simetría: la fibra simétrica (1 Gbps/1 Gbps) es el estándar para empresas.",
        "Cobertura de oficina: ¿la fibra llega a tu dirección? Comprueba en cada operador.",
        "SLAs: tiempo de reparación garantizado (mejor < 4h) y compensaciones por caídas.",
    ]),
    ("h2", "2. ¿Cuánta velocidad necesito? Regla rápida"),
    ("table", [
        ["Tipo de empresa", "Velocidad recomendada"],
        ["1-5 personas, correo y web", "300 Mbps simétricos"],
        ["5-15 personas, nube + videollamadas", "600 Mbps simétricos"],
        ["15-40 personas, ERP + backup continuo", "1 Gbps simétricos"],
        ["40+ personas o cargas intensas", "1 Gbps + línea de backup"],
    ], [(0.5, None), (0.5, None)]),
    ("h2", "3. Comparar ofertas empresariales"),
    ("li", [
        "Pedir precio de empresa (no de casa): las tarifas empresariales incluyen SLA y soporte distinto.",
        "Leer la letra pequeña: instalación, permanencia, router incluido, IP fija (¿la necesitas?).",
        "IP fija: solo para servicios propios (VPN entrante, cámaras); en la nube casi nunca hace falta.",
        "Backup de línea: si la caída os cuesta dinero, una 4G/5G de respaldo es barata.",
        "Recomendado: operadores neutros (empresas de telecom para negocios) suelen tener mejor soporte.",
    ]),
    ("h2", "4. Antes de firmar"),
    ("li", [
        "☐ Comprobado que la fibra llega a la dirección (o fecha de instalación escrita).",
        "☐ Precio de empresa con SLA escrito (tiempo máximo de reparación).",
        "☐ Router con WiFi 6 y modo bridge para usar tu propio firewall.",
        "☐ Instalación y alta sin coste o con coste negociado.",
        "☐ Permanencia aceptable (≤ 12 meses) y penalización por salida razonable.",
    ]),
])
save("guia-proveedor-internet.pdf")

# ============ PLANTILLAS ============

document("Plantilla: Inventario de equipos TI", [
    ("h1", "Plantilla: Inventario de equipos TI"),
    ("p", "Plantilla editable para tener controlado todo el hardware de la empresa: quién lo tiene, desde cuándo y cuándo toca renovarlo."),
    ("h2", "1. Por qué tener un inventario"),
    ("li", [
        "Saber qué hay y dónde está en 5 minutos (imprescindible en auditorías y seguros).",
        "Planificar renovaciones: el coste de un portátil de 6 años no es la compra, es la pérdida de productividad.",
        "Bajas de empleados: sin inventario, los equipos 'desaparecen' en la mudanza.",
        "Control de software y licencias: evitar pagar licencias de equipos que ya no existen.",
    ]),
    ("h2", "2. Campos del inventario (por equipo)"),
    ("table", [
        ["Campo", "Ejemplo"],
        ["ID interno", "PC-001"],
        ["Tipo", "Portátil / Sobremesa / Monitor / Switch / NAS"],
        ["Marca y modelo", "Lenovo ThinkPad T14"],
        ["Nº de serie", "PF3XKZ21"],
        ["Empleado asignado", "María López (finanzas)"],
        ["Ubicación", "Oficina central - Planta 1"],
        ["Fecha de compra", "2024-03-15"],
        ["Garantía hasta", "2026-03-15"],
        ["Estado", "Activo / Reparación / Baja"],
        ["Notas", "Cifrado activo, sin dock"],
    ], [(0.4, None), (0.6, None)]),
    ("h2", "3. Reglas de oro"),
    ("li", [
        "Actualizar el inventario en el momento del alta/baja, no 'cuando se pueda'.",
        "Escribir el nº de serie en una etiqueta física en cada equipo.",
        "Renovación recomendada: portátiles cada 4-5 años, servidores cada 5-6, NAS cada 5.",
        "Guardar facturas y garantías junto al inventario (una carpeta en la nube).",
        "Hacer una revisión física del inventario cada 6 meses.",
    ]),
    ("h2", "4. Sección de software y licencias"),
    ("li", [
        "Registro de software instalado por equipo (Sistema operativo, Office, antivirus...).",
        "Licencias: producto, nº de licencia, usuario, caducidad y coste anual.",
        "Alertas de renovación: 30 días antes de caducar las suscripciones críticas.",
        "Inventario de cuentas SaaS (dominio, admin, quién paga, qué se usa de verdad).",
    ]),
])
save("plantilla-inventario-ti.pdf")

document("Plantilla: Plan de contingencia ante desastres (DRP)", [
    ("h1", "Plantilla: Plan de recuperación ante desastres (DRP)"),
    ("p", "Plantilla editable para que tu empresa sepa exactamente qué hacer cuando algo grave falla: ransomware, incendio, caída de servidores."),
    ("h2", "1. Objetivo del plan"),
    ("p", "Definir los pasos, responsables y tiempos para recuperar la operativa de TI de [empresa] tras un desastre. Objetivos: RPO (pérdida de datos máxima aceptable) y RTO (tiempo máximo de inactividad) definidos y aprobados por dirección."),
    ("h2", "2. Roles y contactos"),
    ("table", [
        ["Rol", "Responsable", "Teléfono / Email"],
        ["Coordinador del plan", "", ""],
        ["Responsable TI", "", ""],
        ["Comunicación (clientes/empleados)", "", ""],
        ["Proveedor de emergencia (Forj)", "", ""],
        ["Seguros / policía (si aplica)", "", ""],
    ], [(0.4, None), (0.3, None), (0.3, None)]),
    ("h2", "3. Escenarios y respuesta"),
    ("h3", "A. Ransomware / cifrado de datos"),
    ("li", [
        "1. Desconectar el equipo o servidor afectado de la red (no apagarlo).",
        "2. Avisar al coordinador y al responsable TI en < 1 hora.",
        "3. NO pagar sin evaluación: contactar con especialistas.",
        "4. Restaurar desde la copia inmutable (3-2-1) tras validar la limpieza.",
        "5. Cambiar contraseñas de todas las cuentas comprometidas.",
        "6. Documentar el incidente y las lecciones aprendidas.",
    ]),
    ("h3", "B. Caída del servidor / oficina"),
    ("li", [
        "1. Valorar el alcance: ¿afecta correo, ERP, ficheros?",
        "2. Activar el plan de contingencia: trabajo remoto con los backups de la nube.",
        "3. Comunicar a empleados y clientes con el mensaje preparado.",
        "4. Restaurar en el orden: ficheros críticos → ERP → resto.",
        "5. Revisar la causa raíz antes de volver a producción.",
    ]),
    ("h2", "4. RPO y RTO recomendados"),
    ("table", [
        ["Sistema", "RPO (pérdida máx.)", "RTO (parada máx.)"],
        ["Correo", "15 min", "4 h"],
        ["Ficheros compartidos", "24 h", "8 h"],
        ["ERP / gestión", "15 min", "8 h"],
        ["Copias de seguridad", "24 h", "12 h"],
    ], [(0.45, None), (0.27, None), (0.28, None)]),
    ("h2", "5. Pruebas"),
    ("li", [
        "Prueba de restauración completa: trimestral.",
        "Simulacro de ransomware: anual, con todo el equipo implicado.",
        "Revisión del plan: cada 6 meses o tras cada cambio relevante.",
        "El plan se aprueba por dirección y se archiva en dos ubicaciones (local + nube).",
    ]),
])
save("plantilla-plan-contingencia.pdf")

document("Plantilla: Contrato de mantenimiento informático", [
    ("h1", "Plantilla: Contrato de mantenimiento informático"),
    ("p", "Plantilla editable de contrato de servicios TI entre proveedor y cliente. Adapta los campos entre corchetes y hazlo revisar por tu asesor legal."),
    ("h2", "1. Partes"),
    ("p", "De una parte, [nombre del proveedor, CIF, dirección], en adelante EL PROVEEDOR. De otra, [nombre del cliente, CIF, dirección], en adelante EL CLIENTE. Ambas se reconocen capacidad legal para formalizar el presente contrato."),
    ("h2", "2. Objeto del contrato"),
    ("p", "El PROVEEDOR prestará al CLIENTE los servicios de mantenimiento informático descritos en el anexo: [soporte remoto y presencial, mantenimiento preventivo mensual, monitorización, backups, seguridad] con un tiempo de respuesta garantizado de [2/4/8] horas laborables."),
    ("h2", "3. Alcance y exclusiones"),
    ("li", [
        "Incluido: [lista de equipos y sistemas cubiertos, con inventario anexo].",
        "Incluido: [nº de incidencias mensuales incluidas y horas de soporte].",
        "Excluido: [cambio de hardware, proyectos de migración, software no estándar] — se presupuestarán aparte.",
        "Las incidencias se reportan por [email/portal/teléfono] en horario de [9:00-18:00].",
    ]),
    ("h2", "4. Precio y facturación"),
    ("li", [
        "Precio: [X]€ + IVA mensuales, pagaderos por [transferencia] dentro de los [30] días desde la factura.",
        "Revisión anual de precio según IPC y alcance real.",
        "Desplazamientos incluidos hasta [km/ciudad]; los superiores se facturan a [0,X]€/km.",
        "Horas fuera del alcance se facturan a [X]€/hora con aprobación previa.",
    ]),
    ("h2", "5. Duración y terminación"),
    ("li", [
        "Duración: [12] meses renovables tácitamente por periodos iguales.",
        "Terminación: preaviso de [60] días por escrito por cualquiera de las partes.",
        "Incumplimiento: resolución con preaviso de [30] días si no se subsana.",
        "Confidencialidad: ambas partes se obligan a no divulgar información del otro durante la vigencia y los [2] años posteriores.",
    ]),
    ("h2", "6. Responsabilidad y garantías"),
    ("li", [
        "El PROVEEDOR responde de los daños causados por dolo o negligencia, con límite al importe anual del contrato.",
        "El CLIENTE es responsable de mantener las licencias de software propias al día.",
        "El PROVEEDOR no garantiza la recuperación de datos que el CLIENTE no tenía copiados según el plan de backups.",
        "Anexos: inventario, niveles de servicio (SLA), plan de backups.",
    ]),
    ("p", "Firmado en [ciudad], a [fecha]. — Firma proveedor: ______ — Firma cliente: ______"),
])
save("plantilla-contrato-mantenimiento.pdf")

document("Política de uso aceptable de Internet", [
    ("h1", "Política de uso aceptable de Internet"),
    ("p", "Plantilla editable que define cómo los empleados pueden usar la conexión, el correo y los dispositivos de la empresa."),
    ("h2", "1. Objeto"),
    ("p", "Esta política regula el uso aceptable de los recursos tecnológicos de [empresa]: conexión a Internet, correo electrónico, equipos y sistemas. Su incumplimiento puede conllevar medidas disciplinarias."),
    ("h2", "2. Uso aceptable"),
    ("li", [
        "Uso de Internet y correo para tareas laborales y uso personal ocasional y razonable.",
        "Instalación de software únicamente desde fuentes oficiales y con aprobación de TI.",
        "Uso del equipamiento corporativo para el trabajo de la empresa.",
        "Acceso a los recursos internos exclusivamente por los canales oficiales (VPN).",
    ]),
    ("h2", "3. Uso prohibido"),
    ("li", [
        "Actividades ilegales, descarga de contenido protegido o piratería.",
        "Envío de datos sensibles de la empresa o de clientes fuera de los canales aprobados.",
        "Acceso no autorizado a cuentas, ficheros o sistemas ajenos al puesto.",
        "Conexión de dispositivos personales a la red corporativa sin autorización (BYOD).",
        "Uso de cuentas de empresa para asuntos personales masivos o newsletters.",
        "Compartir credenciales o permitir que otra persona use tu cuenta.",
    ]),
    ("h2", "4. Privacidad y monitorización"),
    ("p", "Los recursos corporativos son de la empresa. [Empresa] puede revisar los accesos y logs para proteger sus sistemas y datos, conforme al RGPD y el estatuto de los trabajadores. Los empleados serán informados de cualquier medida de monitorización significativa."),
    ("h2", "5. Consecuencias del incumplimiento"),
    ("li", [
        "Incidencias leves: amonestación verbal o escrita.",
        "Incidencias graves: suspensión temporal de accesos y medidas disciplinarias.",
        "Delitos (acceso no autorizado, suplantación): denuncia ante las autoridades.",
        "El daño económico derivado del incumplimiento puede ser reclamado al responsable.",
    ]),
    ("h2", "6. Aceptación"),
    ("p", "Firma del empleado: ______ — Fecha: ______. Este documento se entrega con el contrato de trabajo o en el onboarding."),
])
save("politica-uso-aceptable.pdf")

document("Plan de respuesta ante incidentes de seguridad", [
    ("h1", "Plan de respuesta ante incidentes de seguridad"),
    ("p", "Plantilla editable con el playbook para responder ante incidentes de seguridad en [empresa]: quién, cómo y cuándo."),
    ("h2", "1. Qué es un incidente"),
    ("p", "Cualquier evento que comprometa la confidencialidad, integridad o disponibilidad de los sistemas o datos: phishing ejecutado, ransomware, robo de equipo, filtración, cuenta comprometida o DDoS."),
    ("h2", "2. Clasificación y tiempos"),
    ("table", [
        ["Severidad", "Ejemplo", "Tiempo de respuesta"],
        ["Bajo", "Correo phishing reportado a tiempo", "24 h"],
        ["Medio", "Cuenta comprometida aislada", "4 h"],
        ["Alto", "Ransomware en un equipo", "1 h"],
        ["Crítico", "Cifrado masivo o filtración", "Inmediato"],
    ], [(0.25, None), (0.45, None), (0.3, None)]),
    ("h2", "3. Fases de respuesta"),
    ("h3", "Detección"),
    ("li", [
        "Vías: reporte de empleados, alertas de monitorización, aviso de terceros.",
        "Registrar fecha, hora y evidencia de cada incidente.",
    ]),
    ("h3", "Contención"),
    ("li", [
        "Aislar el equipo afectado de la red (desconectar cable/wifi, no apagar).",
        "Suspender cuentas comprometidas y revocar sesiones activas.",
        "Bloquear C2/dominios maliciosos en el firewall si aplica.",
    ]),
    ("h3", "Erradicación y recuperación"),
    ("li", [
        "Identificar la causa raíz (cómo entró).",
        "Limpiar el sistema o restaurar desde backup verificado.",
        "Cambiar contraseñas y claves afectadas.",
        "Restaurar los servicios en orden de prioridad del DRP.",
    ]),
    ("h3", "Post-incidente"),
    ("li", [
        "Informe de incidente: cronología, causa, impacto, acciones.",
        "Notificación a la AEPD en < 72 h si hay riesgo para los interesados (RGPD).",
        "Lecciones aprendidas y mejora de controles.",
    ]),
    ("h2", "4. Contactos de emergencia"),
    ("table", [
        ["Contacto", "Teléfono / Email"],
        ["Responsable TI", ""],
        ["Proveedor de ciberseguridad (Forj)", ""],
        ["AEPD (notificación de brechas)", "https://www.aepd.es"],
        ["INCIBE (soporte pymes)", "017"],
        ["Seguro cibernético (si existe)", ""],
    ], [(0.5, None), (0.5, None)]),
])
save("plan-respuesta-incidentes.pdf")

# ============ CHECKLISTS Y KITS ============

document("Kit: Baja de empleados (revocación de accesos)", [
    ("h1", "Kit: Baja de empleados"),
    ("p", "Procedimiento completo para dar de baja a un empleado en un día, sin dejar accesos abiertos ni datos perdidos."),
    ("h2", "1. El día de la baja (imprescindible)"),
    ("li", [
        "☐ Desactivar la cuenta de correo corporativa.",
        "☐ Revocar accesos a todas las aplicaciones (ERP, CRM, banca, nube).",
        "☐ Quitar del grupo de distribución, calendarios compartidos y WhatsApps corporativos.",
        "☐ Revocar la VPN y el acceso remoto.",
        "☐ Cambiar las contraseñas de servicios compartidos que conocía (info@, redes sociales).",
        "☐ Desactivar la tarjeta de acceso físico y recoger llaves.",
    ]),
    ("h2", "2. Primera semana"),
    ("li", [
        "☐ Recoger el equipo y verificar en el inventario (nº de serie y estado).",
        "☐ Revisar el buzón: reenviar correos pendientes a su sustituto, conservar lo necesario.",
        "☐ Transferir la propiedad de documentos y carpetas al responsable del departamento.",
        "☐ Desactivar 2FA del empleado en cuentas de empresa.",
        "☐ Revisar si usaba equipos personales (BYOD): desconectar y revocar.",
    ]),
    ("h2", "3. Primer mes"),
    ("li", [
        "☐ Verificar en los logs que no hay accesos posteriores a la fecha de baja.",
        "☐ Comprobar que las licencias se liberaron (no seguir pagando).",
        "☐ Archivar el registro completo en RRHH con el acta de devolución firmada.",
        "☐ Si el equipo se reasigna: formatear con cifrado limpio y reinstalar.",
    ]),
    ("h2", "4. Riesgos si no se hace"),
    ("li", [
        "Accesos activos tras la baja: fugas, robos o daños con la cuenta de la empresa.",
        "Coste de licencias fantasma (se pagan meses por empleados que ya no están).",
        "Perder documentos clave si nadie se queda con las carpetas del ex-empleado.",
        "Litigios laborales por datos personales mal gestionados en la baja.",
    ]),
])
save("kit-baja-empleados.pdf")

document("Checklist: Seguridad mensual TI", [
    ("h1", "Checklist: Seguridad mensual TI"),
    ("p", "Lista de mantenimiento preventivo de seguridad para hacer cada mes. 30 minutos al mes evitan el 90% de los sustos."),
    ("h2", "1. Sistemas"),
    ("li", [
        "☐ Actualizaciones de Windows/macOS instaladas en todos los equipos.",
        "☐ Actualizaciones de firmware de router, APs y switches.",
        "☐ Antivirus/EDR activo en todos los equipos y con firmas al día.",
        "☐ Discos: revisar alertas SMART de NAS y servidores.",
        "☐ Espacio libre en discos y buzones > 20%.",
    ]),
    ("h2", "2. Accesos"),
    ("li", [
        "☐ Revisar usuarios dados de alta el último mes (¿alguien que no debiera estar?).",
        "☐ Comprobar cuentas administrador: solo las necesarias.",
        "☐ 2FA activado en cuentas nuevas (o alerta a las que no lo tienen).",
        "☐ Revisar accesos remotos/VPN del mes.",
    ]),
    ("h2", "3. Backups"),
    ("li", [
        "☐ Verificar que el backup diario de los últimos 7 días se completó.",
        "☐ Probar una restauración puntual de 3 archivos aleatorios.",
        "☐ Comprobar la copia fuera de línea/immutable sigue accesible.",
    ]),
    ("h2", "4. Correo y web"),
    ("li", [
        "☐ Revisar alertas de spam y correos marcados como sospechosos.",
        "☐ Comprobar que SPF/DKIM/DMARC del dominio siguen correctos.",
        "☐ Revisar certificados SSL que caducan en < 90 días.",
        "☐ Cambiar contraseñas de servicios marcados en alertas de brechas (haveibeenpwned).",
    ]),
    ("h2", "5. Registro"),
    ("li", [
        "☐ Anotar fecha y quién hizo la revisión (firmar el checklist).",
        "☐ Archivar el checklist mensual como evidencia (seguros y auditorías).",
        "☐ Enviar al responsable cualquier incidencia detectada con prioridad.",
    ]),
])
save("checklist-seguridad-mensual.pdf")

document("Kit: Auditoría interna TI para pymes", [
    ("h1", "Kit: Auditoría interna TI para pymes"),
    ("p", "Kit para hacer una autoevaluación TI completa de tu empresa: inventario, red, seguridad, backups y procesos."),
    ("h2", "1. Inventario"),
    ("li", [
        "☐ ¿Hay un inventario actualizado de equipos y software?",
        "☐ ¿Cada equipo tiene responsable y ubicación conocidos?",
        "☐ ¿Las garantías y facturas están archivadas?",
        "☐ ¿Hay software sin licencia? (riesgo legal y de seguridad)",
    ]),
    ("h2", "2. Red"),
    ("li", [
        "☐ ¿WiFi con WPA3 (o al menos WPA2)?",
        "☐ ¿Red de invitados separada de la red interna?",
        "☐ ¿El router admin se usa por HTTPS y con contraseña fuerte?",
        "☐ ¿Hay VLAN para VoIP u otras seguridades?",
        "☐ ¿El cableado está etiquetado y certificado?",
        "☐ ¿Hay dispositivos desconocidos conectados a la red? (revisar en el router)",
    ]),
    ("h2", "3. Seguridad"),
    ("li", [
        "☐ ¿2FA en email, banca y accesos remotos?",
        "☐ ¿Gestor de contraseñas corporativo en uso?",
        "☐ ¿Antivirus/EDR en todos los equipos?",
        "☐ ¿Actualizaciones automáticas activadas?",
        "☐ ¿Firewall corporativo (o al menos el del router) con filtrado?",
        "☐ ¿Cuentas admin solo para administradores?",
    ]),
    ("h2", "4. Backups"),
    ("li", [
        "☐ ¿Se cumple la regla 3-2-1?",
        "☐ ¿El backup fuera de línea es inmutable?",
        "☐ ¿Se prueba la restauración al menos trimestralmente?",
        "☐ ¿Existe política de retención documentada?",
    ]),
    ("h2", "5. Procesos"),
    ("li", [
        "☐ ¿Existe plan de respuesta ante incidentes?",
        "☐ ¿Existe plan de contingencia (DRP) aprobado?",
        "☐ ¿El onboarding/baja de empleados sigue un checklist?",
        "☐ ¿Hay contrato de mantenimiento con proveedor o plan interno?",
        "☐ ¿El inventario TI se revisa semestralmente?",
    ]),
    ("h2", "6. Resultado"),
    ("p", "Cuenta las casillas sin marcar: 0-3 → infraestructura sana; 4-8 → conviene un plan de mejora; 9+ → una auditoría profesional (Forj) es recomendable este trimestre."),
])
save("kit-auditoria-interna-ti.pdf")

document("Checklist: Instalación de oficina nueva", [
    ("h1", "Checklist: Instalación de oficina nueva"),
    ("p", "Lista completa para montar la tecnología de una oficina desde cero: internet, red, equipos y puesta en marcha en orden."),
    ("h2", "1. Antes de la obra (D-30)"),
    ("li", [
        "☐ Contratar la fibra empresarial con fecha de instalación confirmada.",
        "☐ Solicitar al operador el punto de entrada (PTR) en la ubicación del armario.",
        "☐ Planificar el cableado: toma por puesto, fibra entre plantas, canaletas.",
        "☐ Diseñar la cobertura WiFi con APs por zona (ver guía de infraestructura).",
        "☐ Presupuestar armario de comunicaciones con reserva (2-3 U).",
    ]),
    ("h2", "2. Obra e instalación (D-7)"),
    ("li", [
        "☐ Cableado certificado (Cat 6/A) con informe y etiquetado.",
        "☐ Instalación de APs y switch con PoE.",
        "☐ Montaje del armario: patch panel, switch, router, SAI.",
        "☐ Configuración básica: WiFi, VLANs, red de invitados, firewall.",
        "☐ Backup de línea 4G/5G si la oficina es crítica.",
    ]),
    ("h2", "3. Equipos (D-1)"),
    ("li", [
        "☐ Puestos de trabajo montados y conectados al patch panel.",
        "☐ Impresoras con IP fija o reserva DHCP e instaladas en los equipos.",
        "☐ Prueba de velocidad por zona (debe cumplir lo contratado).",
        "☐ Prueba de videollamada en las salas de reuniones.",
        "☐ Servidor/NAS en el armario con acceso por VPN.",
    ]),
    ("h2", "4. Día de la mudanza"),
    ("li", [
        "☐ Comprobar la operativa completa: correo, ficheros, impresión, WiFi.",
        "☐ Revisar la cobertura WiFi con empleados moviéndose por la oficina.",
        "☐ Señalizar el armario (solo personal autorizado).",
        "☐ Entregar al equipo las nuevas contraseñas WiFi por canal seguro.",
    ]),
    ("h2", "5. Primer mes"),
    ("li", [
        "☐ Monitorizar incidencias de cobertura y velocidad.",
        "☐ Ajustar canales/potencia de APs según uso real.",
        "☐ Documentar el nuevo plano de red y el inventario de equipos.",
        "☐ Revisar factura del operador: que el alta y el SLA coinciden con lo contratado.",
    ]),
])
save("checklist-oficina-nueva.pdf")

# ============ SERVICIOS ============

document("Consultoría de ciberseguridad — Briefing", [
    ("h1", "Consultoría de ciberseguridad (1 hora) — Briefing"),
    ("p", "Sesión de 1 hora para evaluar la seguridad de tu empresa y priorizar mejoras. Completa este briefing antes de la sesión."),
    ("h2", "1. Datos"),
    ("table", [
        ["Dato", "Respuesta"],
        ["Nombre de la empresa", ""],
        ["Nº de empleados y equipos", ""],
        ["Sector", ""],
        ["¿Usáis correo corporativo (cuál)?", ""],
        ["¿Tenéis 2FA activado en el correo?", ""],
    ], [(0.5, None), (0.5, None)]),
    ("h2", "2. Tu situación"),
    ("li", [
        "¿Habéis sufrido phishing, ransomware o accesos raros? (cuéntalo brevemente)",
        "¿Los backups están en 3-2-1? ¿Se prueban?",
        "¿Cuántas personas tienen accesos de administrador?",
        "¿El wifi usa WPA3 y hay red de invitados?",
        "¿Tenéis política de contraseñas y gestor?",
    ]),
    ("h2", "3. Qué recibirás"),
    ("li", [
        "Evaluación de tu postura de seguridad actual (0-100).",
        "Las 5 mejoras de mayor impacto con presupuesto orientativo.",
        "Plan de acción a 30/60/90 días.",
        "Resumen por escrito al terminar la sesión.",
    ]),
    ("h2", "4. Agenda"),
    ("li", [
        "0-5 min: repaso del briefing.",
        "5-40 min: análisis de tu seguridad actual.",
        "40-55 min: recomendaciones y priorización.",
        "55-60 min: plan de acción y próximos pasos.",
    ]),
])
save("consultoria-ciberseguridad-1h.pdf")

document("Informe de recomendaciones TI — Documento de preparación", [
    ("h1", "Informe de recomendaciones TI"),
    ("p", "Servicio sin visita: analizamos la información que nos envías y recibes un informe de recomendaciones por escrito."),
    ("h2", "1. Qué incluye"),
    ("li", [
        "Análisis de la documentación y datos que nos envíes (inventario, planos, capturas).",
        "Informe por escrito con hallazgos y recomendaciones priorizadas.",
        "Presupuestos orientativos por mejora (con y sin inversión).",
        "Plan de acción a 30/60/90 días.",
        "Revisión de las conclusiones por videollamada de 20 min (opcional).",
    ]),
    ("h2", "2. Qué necesitamos de ti"),
    ("li", [
        "Inventario de equipos (plantilla disponible en forj.es).",
        "Plano o croquis de la oficina (opcional pero muy útil).",
        "Modelo de router/APs si lo conoces (foto de la etiqueta vale).",
        "Descripción de los problemas que notáis (velocidad, caídas, impresoras...).",
        "Presupuesto anual de TI aproximado (ayuda a priorizar).",
    ]),
    ("h2", "3. Plazos"),
    ("li", [
        "Entrega del informe: 3-5 días laborables desde que recibimos la documentación.",
        "Si falta documentación, te avisamos en 24 h para pedirla.",
        "Validez de las recomendaciones: 60 días (los precios de mercado cambian).",
    ]),
])
save("informe-recomendaciones-ti.pdf")

document("Soporte remoto 5 horas — Guía de uso", [
    ("h1", "Soporte remoto (5 horas) — Guía de uso"),
    ("p", "Bloque de 5 horas de soporte técnico remoto para tu empresa. Así se consume y así funciona."),
    ("h2", "1. Qué incluye"),
    ("li", [
        "5 horas de soporte remoto con técnicos de Forj, válidas durante 3 meses.",
        "Incidencias: correo, WiFi, impresoras, Windows/macOS, VPN, backups.",
        "Horario de atención: lunes a viernes 9:00-18:00.",
        "Reporte al final de cada sesión con lo realizado.",
    ]),
    ("h2", "2. Cómo se consume"),
    ("li", [
        "Cada sesión se factura en bloques de 15 minutos (mínimo 30).",
        "El tiempo de diagnóstico y resolución cuenta en la hora.",
        "El tiempo de espera/coordinación no cuenta.",
        "Puedes consultar el saldo restante en cualquier momento (info@forj.es).",
    ]),
    ("h2", "3. Qué NO incluye"),
    ("li", [
        "Proyectos (migraciones, instalaciones completas): se presupuestan aparte.",
        "Hardware: repuestos o compras van aparte.",
        "Software de terceros en profundidad (contabilidad, diseño): se valora caso a caso.",
        "Soporte fuera de horario: tarifa especial.",
    ]),
    ("h2", "4. Para agilizar cada incidencia"),
    ("li", [
        "Describe el problema: qué pasa, cuándo, desde qué equipo, a quién afecta.",
        "Adjunta capturas de pantalla del error.",
        "Si es posible, ten el equipo afectado encendido y conectado.",
        "Un contacto único por incidencia evita idas y venidas.",
    ]),
])
save("soporte-remoto-5h.pdf")

document("Diagnóstico de red — Documento de preparación", [
    ("h1", "Diagnóstico de red y rendimiento"),
    ("p", "Diagnóstico remoto o presencial de tu red: velocidad real, latencia, interferencias y configuración. Sin obra, con respuestas."),
    ("h2", "1. Qué incluye"),
    ("li", [
        "Test de velocidad y latencia por zona y a horas distintas.",
        "Análisis de interferencias WiFi (canales, vecinos, ruido).",
        "Revisión de configuración: router, APs, QoS, firewall.",
        "Identificación de cuellos de botella (cableado, PoE, DNS, tráfico).",
        "Informe con recomendaciones aplicables inmediatamente (configuración) y a medio plazo (hardware).",
    ]),
    ("h2", "2. Cómo se realiza"),
    ("li", [
        "Remoto: compartes acceso temporal seguro a tu router/APs (o nos haces capturas).",
        "Presencial: visita de 1-2 horas con medición por zonas (opcional).",
        "Los datos se recogen sin interrumpir la operativa (fuera de horas punta si se puede).",
        "Entrega del informe en 48-72 h.",
    ]),
    ("h2", "3. Qué necesitamos de ti"),
    ("li", [
        "Descripción de los síntomas: dónde y cuándo va lenta la red.",
        "Modelos de router/APs (foto de la etiqueta).",
        "Nº de usuarios y dispositivos conectados.",
        "Plano si es presencial.",
    ]),
    ("h2", "4. Resultados típicos"),
    ("li", [
        "Configuración mejorable (canales, potencia, QoS) → solucionable en el acto.",
        "Hardware insuficiente (router básico, APs antiguos) → recomendación concreta.",
        "Cableado antiguo o mal certificado → presupuesto de mejora.",
        "Saturación del enlace → ampliación o backup de línea.",
    ]),
])
save("diagnostico-red.pdf")

# ============ SUSCRIPCIONES ============

document("Monitorización de red 24/7 — Bienvenida", [
    ("h1", "Monitorización de red 24/7 — Bienvenida"),
    ("p", "Bienvenido al servicio de monitorización de red de Forj. Este documento explica qué monitorizamos y cómo recibirás las alertas."),
    ("h2", "1. Qué monitorizamos"),
    ("li", [
        "Servidores y servicios críticos: correo, ERP, ficheros (ping, puertos, respuestas HTTP).",
        "Enlaces: pérdida de conectividad y latencia (con umbral de alerta).",
        "Discos: espacio, estado SMART y temperatura de NAS/servidores.",
        "Backups: verificación de que el backup diario se completa.",
        "Certificados SSL: aviso 30 días antes de caducar.",
        "Red: caídas de APs, switches y router.",
    ]),
    ("h2", "2. Cómo recibirás las alertas"),
    ("li", [
        "Email: alertas críticas y resumen semanal.",
        "WhatsApp/Telegram (opcional): solo alertas críticas.",
        "Panel: estado del servicio accesible 24/7.",
        "Escalado: si no se confirma la alerta en 30 min, nos ponemos en contacto.",
    ]),
    ("h2", "3. Qué hacemos ante una alerta"),
    ("li", [
        "Alerta crítica: intervención remota inmediata en horario laboral; contención y comunicación.",
        "Alerta media: diagnóstico y solución programada en < 24 h.",
        "Informe mensual: resumen de incidencias, tiempos y recomendaciones.",
    ]),
    ("h2", "4. Configuración inicial (primeros 5 días)"),
    ("li", [
        "Nos envías la lista de servicios y equipos a monitorizar.",
        "Instalamos el agente de monitorización en 1 servidor/NAS (o acceso API).",
        "Definimos los umbrales de alerta contigo.",
        "Activamos los canales de notificación.",
    ]),
    ("p", "¿Preguntas? Respuesta en < 4 h laborables: info@forj.es"),
])
save("monitorizacion-red-24-7.pdf")

document("Soporte TI remoto ilimitado — Guía del servicio", [
    ("h1", "Soporte TI remoto ilimitado — Guía del servicio"),
    ("p", "Bienvenido al soporte TI remoto ilimitado de Forj. Este documento define cómo funciona, qué cubre y cómo pedir ayuda."),
    ("h2", "1. Qué incluye"),
    ("li", [
        "Soporte remoto ilimitado en horario laboral (9:00-18:00, L-V).",
        "Incidencias de todo el parque informático: correo, equipos, WiFi, impresoras, VPN, backups.",
        "Tiempo de primera respuesta: < 2 h laborables.",
        "Gestión de proveedores (operador, licencias) en tu nombre.",
        "Informe mensual de actividad y recomendaciones.",
    ]),
    ("h2", "2. Cómo pedir ayuda"),
    ("li", [
        "Email: soporte@forj.es (canal principal, crea el ticket).",
        "WhatsApp (opcional): para urgencias.",
        "Cada incidencia recibe un ticket; puedes consultar el estado.",
        "Las incidencias críticas (todo el correo caído, ransomware) tienen prioridad automática.",
    ]),
    ("h2", "3. Qué no incluye"),
    ("li", [
        "Proyectos de instalación o migración: se presupuestan aparte con condiciones preferentes.",
        "Hardware y licencias nuevas: facturación aparte.",
        "Soporte presencial: incluido 1 visita/mes básica; más visitas se presupuestan.",
        "Soporte fuera de horario: disponible como opción adicional.",
    ]),
    ("h2", "4. Nuestra promesa"),
    ("li", [
        "Ninguna incidencia se cierra sin resolución o plan claro.",
        "Cada mes recibes un resumen con incidencias, tiempos y mejoras recomendadas.",
        "Puedes cancelar con preaviso de 30 días, sin permanencia escondida.",
    ]),
])
save("soporte-ti-ilimitado.pdf")

document("Informe mensual de seguridad — Guía del servicio", [
    ("h1", "Informe mensual de seguridad — Guía del servicio"),
    ("p", "Servicio de supervisión mensual de seguridad de tu empresa con informe ejecutivo. Así funciona."),
    ("h2", "1. Qué revisamos cada mes"),
    ("li", [
        "Actualizaciones pendientes de equipos y sistemas críticos.",
        "Estado de backups y prueba de restauración puntual.",
        "Cuentas con 2FA desactivado o contraseñas débiles (si tenemos acceso a tu directorio).",
        "Certificados SSL, SPF/DKIM/DMARC y presencia en listas negras.",
        "Accesos de administrador y cuentas inactivas.",
        "Alertas de monitorización del mes (si usas el servicio de monitorización).",
    ]),
    ("h2", "2. Qué recibes"),
    ("li", [
        "Informe ejecutivo de 1-2 páginas: estado, hallazgos y prioridad.",
        "Puntuación de seguridad (0-100) con evolución mensual.",
        "Lista de acciones recomendadas con esfuerzo estimado.",
        "Sesión de 15-20 min al trimestre para repasar tendencias (opcional).",
    ]),
    ("h2", "3. Qué no es"),
    ("li", [
        "No es un pentest ni una auditoría de cumplimiento completa (se contratan aparte).",
        "No realiza cambios en tu infraestructura sin tu aprobación explícita.",
        "No sustituye a la gestión de incidencias (soporte aparte).",
    ]),
    ("h2", "4. Puesta en marcha"),
    ("li", [
        "Semana 1: revisión inicial (lo que haya, sin instalaciones).",
        "Semana 1: definición del alcance y accesos de solo lectura.",
        "A partir del mes 2: informes mensuales completos.",
    ]),
])
save("informe-mensual-seguridad.pdf")

print("PDFs nuevos generados en", os.path.abspath(OUT))
