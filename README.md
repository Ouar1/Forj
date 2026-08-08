# Forj

Infraestructura TI Profesional — Diseño, instalación y mantenimiento de redes, servidores y automatización para empresas.

## Stack

- **Frontend:** React + Vite + TypeScript
- **Backend:** FastAPI (Python 3.11+)
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)
- **ORM:** SQLAlchemy 2.0
- **Auth:** JWT + refresh tokens
- **Pagos:** Stripe
- **Deploy:** Docker + Railway

## Servicios

- **Soporte usuarios / Helpdesk** — PC lento, impresoras, contraseñas, Windows updates, "se me borró un archivo"
- **Gestión Microsoft 365 / Google Workspace** — Usuarios, licencias, buzones, MFA, SPF/DKIM/DMARC, Teams/SharePoint
- **Antivirus / EDR gestionado** — Alertas, exclusiones, renovaciones, reporting mensual, respuesta a incidencias
- **Backup de puestos de trabajo** — OneDrive/Drive, recuperación archivos, carpetas conocidas, test de restore
- **Dominios, DNS, Web y SSL** — Renovaciones, cambios DNS, certificados, correo corporativo, hosting básico
- **VPN / Acceso remoto + MFA** — WireGuard/Tailscale, onboarding/offboarding, revocación accesos, troubleshooting
- **Parcheo y actualizaciones** — Anillos de despliegue, reinicios programados, drivers, apps críticas, rollback auto
- **Impresoras y periféricos** — Tóner/atascos, drivers, escaneo a carpetas/email, colas de impresión, impresoras de red
- **MDM / Móviles corporativos** — Intune/Jamf, perfiles, apps gestionadas, bloqueo/borrado remoto, BYOD básico
- **Limpieza y optimización de equipos** — Disco lleno, inicio lento, malware/adware, bloatware, salud SSD
- **Gestión de licencias de software** — Adobe CC, ERPs, antivirus, renovaciones, auditorías, true-ups
- **WiFi oficina (básico)** — 2-4 APs UniFi, SSID corporativo + guest, roaming, reinicios remotos, firmware

### Automatización (transversal + proyectos a medida)
- **Workflows internos** (n8n / Power Automate / Make): CRM ↔ ERP, email → ticket, formularios → BD, aprobaciones
- **Scripts y bots operativos** (Python / Bash): Migraciones, sincronización, reportes, limpieza, backups custom
- **Infraestructura como código** (Terraform / Ansible): Provisionar VPS, K8s, networking, DNS, secrets reproducible
- **CI/CD y pipelines** (GitHub Actions / GitLab CI): Build → test → deploy, gates, rollback, entornos efímeros por PR
- **Observabilidad y alertas** (Prometheus + Grafana / Loki / Uptime Kuma): Dashboards, SLO/SLI, auto-remediación básica
- **IA aplicada a operaciones**: Clasificar tickets, extraer datos PDFs/facturas, resúmenes logs, chat interno RAG

## Desarrollo local

```bash
git clone https://github.com/OUAR77/Forj.git
cd Forj
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Licencia

Uso interno.
