const services = [
  {
    title: "Helpdesk & Soporte",
    desc: "Asistencia remota y presencial: PC lento, impresoras, contraseñas, correo, Windows que no arranca.",
    icon: "01",
  },
  {
    title: "Microsoft 365 / Google Workspace",
    desc: "Usuarios, licencias, buzones, MFA, anti-spam y configuración de correo, Teams y SharePoint.",
    icon: "02",
  },
  {
    title: "Antivirus / EDR",
    desc: "Protección gestionada, renovaciones, cuarentenas resueltas y reporte mensual de seguridad.",
    icon: "03",
  },
  {
    title: "Backup & Recuperación",
    desc: "Copias automáticas de tus datos, archivos borrados recuperados y política de retención.",
    icon: "04",
  },
  {
    title: "Dominios, Web & SSL",
    desc: "Renovaciones, cambios de DNS, correo corporativo, hosting y certificados sin caducar.",
    icon: "05",
  },
  {
    title: "VPN & Acceso Remoto",
    desc: "Teletrabajo seguro y rápido, altas y bajas de accesos, MFA y troubleshooting de conexión.",
    icon: "06",
  },
  {
    title: "Actualizaciones y Parcheo",
    desc: "Windows y software al día, reinicios programados y sin equipos rotos por updates.",
    icon: "07",
  },
  {
    title: "Impresoras y Periféricos",
    desc: "Impresiones que no funcionan, drivers, escaneo a email y mantenimiento de equipos.",
    icon: "08",
  },
  {
    title: "Móviles Corporativos",
    desc: "Perfiles, aplicaciones gestionadas, borrado remoto en perdidas y política de seguridad.",
    icon: "09",
  },
  {
    title: "Limpieza y Optimización",
    desc: "PC lento, disco lleno, malware. Optimizamos y hacemos que vuelva a volar.",
    icon: "10",
  },
  {
    title: "Licencias de Software",
    desc: "Gestionamos tus licencias (Adobe, ERP, etc.), renovaciones en tiempo y sin cortes.",
    icon: "11",
  },
  {
    title: "WiFi para Oficinas",
    desc: "Cobertura total, red de invitados, sin cortes y con acceso controlado.",
    icon: "12",
  },
  {
    title: "Automatización",
    desc: "Workflows, scripts, CI/CD, monitorización e IA: lo repetitivo, que se haga solo.",
    icon: "13",
  },
]

export function ServicesSection() {
  return (
    <section className="py-32 px-6 bg-[#f2f2f2]">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-20">
          <p className="text-sm uppercase tracking-[0.2em] text-neutral-400 mb-4">
            Servicios
          </p>
          <h2 className="text-4xl md:text-5xl font-bold text-neutral-900">
            TI que se gestiona sola
          </h2>
          <p className="mt-4 text-neutral-500 max-w-xl mx-auto text-lg">
            Cuidamos tu día a día, y lo que se repite, lo automatizamos.
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {services.map((s) => (
            <div key={s.title} className="group bg-white border border-neutral-200 rounded-lg p-6 transition-all hover:border-neutral-300 hover:shadow-lg">
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold text-neutral-300 group-hover:text-neutral-400 transition-colors">
                  {s.icon}
                </span>
                {s.title === 'Automatización' && (
                  <span className="text-[10px] tracking-wide uppercase text-neutral-400 bg-neutral-100 px-2 py-1 rounded">Especialidad</span>
                )}
              </div>
              <h3 className="text-lg font-semibold text-neutral-900 mb-2">
                {s.title}
              </h3>
              <p className="text-sm text-neutral-500 leading-relaxed">
                {s.desc}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}