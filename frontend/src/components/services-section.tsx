const services = [
  {
    title: "Redes Profesionales",
    desc: "Instalación de redes WiFi, cableado estructurado, racks, switches, VLANs y VPN para empresas.",
    icon: "01",
  },
  {
    title: "Servidores & NAS",
    desc: "Montaje y configuración de servidores, NAS, backups y recuperación de datos.",
    icon: "02",
  },
  {
    title: "Mantenimiento Informático",
    desc: "Soporte preventivo y correctivo. Monitorización, actualizaciones y resolución de incidencias.",
    icon: "03",
  },
  {
    title: "Soporte Técnico",
    desc: "Asistencia remota y presencial. Resolvemos tus problemas técnicos rápidamente.",
    icon: "04",
  },
  {
    title: "Desarrollo Web",
    desc: "Creamos páginas web corporativas, tiendas online y aplicaciones con tecnologías modernas.",
    icon: "05",
  },
  {
    title: "Integraciones IA",
    desc: "Chatbots, automatizaciones y análisis predictivo con inteligencia artificial para tu negocio.",
    icon: "06",
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
            Todo lo que necesitas
          </h2>
          <p className="mt-4 text-neutral-500 max-w-xl mx-auto text-lg">
            Soluciones completas para llevar tu negocio al siguiente nivel digital.
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {services.map((s) => (
            <div key={s.title} className="group bg-white border border-neutral-200 rounded-lg p-8 transition-all hover:border-neutral-300 hover:shadow-lg">
              <span className="text-3xl font-bold text-neutral-200 group-hover:text-neutral-300 transition-colors">
                {s.icon}
              </span>
              <h3 className="text-xl font-semibold text-neutral-900 mt-4">
                {s.title}
              </h3>
              <p className="text-neutral-500 mt-3 leading-relaxed">
                {s.desc}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
