import { Link } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { ArrowUpRight, ExternalLink, Code, Smartphone, Globe, Zap } from 'lucide-react'
import { SEO } from '@/components/ui/seo'
import { HoverBorderGradient } from '@/components/ui/hover-border-gradient'

const projects = [
  {
    title: 'Oficina TechFlow',
    subtitle: 'Red WiFi corporativa + cableado estructurado',
    desc: 'Diseñamos e instalamos red WiFi con 8 AP Ubiquiti, cableado Cat6A para 40 puestos, rack de comunicaciones y VLANs por departamento.',
    tags: ['Ubiquiti', 'Cat6A', 'VLANs', 'Rack 42U', 'QoS'],
    icon: Globe,
    color: 'from-zinc-700 to-zinc-900',
  },
  {
    title: 'NAS InnovaCorp',
    subtitle: 'Servidor NAS + backups automatizados',
    desc: 'Instalamos NAS Synology en RAID 6 con 48 TB, backups automáticos 3-2-1 y recuperación ante desastres con replicación offsite.',
    tags: ['Synology', 'RAID 6', '3-2-1 Backup', 'Hyper Backup', 'Offsite'],
    icon: Smartphone,
    color: 'from-zinc-800 to-zinc-950',
  },
  {
    title: 'Servidores DataSmart',
    subtitle: 'Virtualización Proxmox + alta disponibilidad',
    desc: 'Implementamos cluster Proxmox con 3 nodos, almacenamiento Ceph, balanceo de carga y monitorización 24/7 con alertas predictivas.',
    tags: ['Proxmox', 'Ceph', 'HA Cluster', 'Zabbix', 'Alerting'],
    icon: Code,
    color: 'from-zinc-700 to-zinc-900',
  },
  {
    title: 'Chatbot IA Forj',
    subtitle: 'Asistente virtual para soporte TI',
    desc: 'Chatbot con IA integrado en web corporativa, capaz de diagnosticar incidencias de red, crear tickets y escalar a técnicos automáticamente.',
    tags: ['OpenAI', 'React', 'Python', 'WebSockets', 'RAG'],
    icon: Zap,
    color: 'from-zinc-800 to-zinc-950',
  },
]

export function PortfolioPage() {
  const { t } = useTranslation()

  return (
    <>
      <SEO title={t('portfolio.page_title', 'Portfolio')} description={t('portfolio.page_description', 'Proyectos de infraestructura TI realizados por Forj')} />
      <div className="min-h-screen pt-28 md:pt-36">
        <div className="mx-auto max-w-6xl px-6 md:px-12 lg:px-20 py-16 md:py-24">
          <Link to="/" className="text-xs text-zinc-600 hover:text-white transition-colors inline-flex items-center gap-1 mb-6 no-underline">
            ← {t('portfolio.back', 'Volver')}
          </Link>
          <span className="inline-block text-[11px] tracking-[0.25em] uppercase text-zinc-600 mb-4 font-mono">
            {t('portfolio.badge', 'Trabajos')}
          </span>
          <h1 className="text-3xl md:text-5xl font-bold text-white leading-[1.05] tracking-tight mb-4">
            {t('portfolio.heading', 'Proyectos realizados')}
          </h1>
          <p className="text-sm text-zinc-500 leading-relaxed max-w-2xl mb-16">
            {t('portfolio.description', 'Cada proyecto es único. Aquí algunos de los trabajos que hemos entregado con resultados medibles.')}
          </p>

          <div className="grid md:grid-cols-2 gap-6">
            {projects.map((p) => (
              <div
                key={p.title}
                className="group p-8 rounded-2xl bg-white/[0.02] border border-white/[0.06] hover:border-white/15 transition-all duration-500 relative overflow-hidden"
              >
                <div className="flex items-start justify-between mb-6">
                  <div className={`size-12 rounded-xl bg-gradient-to-br ${p.color} flex items-center justify-center border border-white/[0.06]`}>
                    <p.icon className="size-5 text-zinc-300" />
                  </div>
                  <ExternalLink className="size-4 text-zinc-700 group-hover:text-zinc-400 transition-colors" />
                </div>
                <h3 className="text-xl font-semibold text-white mb-1">{p.title}</h3>
                <p className="text-xs text-zinc-600 mb-4">{p.subtitle}</p>
                <p className="text-sm text-zinc-500 leading-relaxed mb-6">{p.desc}</p>
                <div className="flex flex-wrap gap-2">
                  {p.tags.map((tag) => (
                    <span key={tag} className="text-[10px] tracking-wide text-zinc-600 bg-white/[0.03] px-2.5 py-1 rounded-md border border-white/[0.04]">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className="mt-20 text-center">
            <p className="text-sm text-zinc-500 mb-6">{t('portfolio.cta_text', '¿Tienes un proyecto en mente?')}</p>
            <HoverBorderGradient as="button" onClick={() => window.dispatchEvent(new CustomEvent('open-contact'))} className="inline-flex items-center gap-2 px-8 py-4 text-base font-medium">
              {t('portfolio.cta', 'Cuéntanos tu idea')} <ArrowUpRight className="size-4" />
            </HoverBorderGradient>
          </div>
        </div>
      </div>
    </>
  )
}
