import { useState, useEffect, useMemo, useRef } from 'react'
import { useTranslation } from 'react-i18next'
import { motion, AnimatePresence } from 'framer-motion'
import { getPriceRanges, type PriceRange } from '@/lib/api'
import { useAuth } from '@/lib/auth-context'
import { HoverBorderGradient } from '@/components/ui/hover-border-gradient'
import { BorderBeam } from '@/components/ui/border-beam'
import {
  ArrowUpRight, Calculator, Wifi, Server, HardDrive,
  Shield, Camera, Lock, HeadphonesIcon, Cloud, ChevronDown,
  Check, Building2, Users, Square, Monitor, Clock, Database,
  Zap, FileText, Sparkles, Rocket, Star, Download, Save,
  Trash2, ChevronLeft, Package, Percent, Printer, X, Plus
} from 'lucide-react'
import type { LucideIcon } from 'lucide-react'

interface FormField {
  key: string
  label: string
  icon: LucideIcon
  type: 'number' | 'select'
  placeholder?: string
  options?: { label: string; multiplier: number }[]
  min?: number
  max?: number
  step?: number
}

interface ServiceConfig {
  id: number
  name: string
  icon: LucideIcon
  fields: FormField[]
  baseMin: number
  baseMax: number
  unit: string
}

interface PackageDef {
  id: string
  name: string
  desc: string
  icon: LucideIcon
  color: string
  services: { configId: number; values: Record<string, number | string> }[]
  discount: number
}

interface SavedBudget {
  id: string
  date: string
  name: string
  email: string
  phone: string
  items: { name: string; min: number; max: number }[]
  totalMin: number
  totalMax: number
  discount: number
  packageName: string | null
}

const STEP_PACKAGE = 0
const STEP_CONFIGURE = 1
const STEP_COMPARE = 2
const STEP_REVIEW = 3

function buildConfigs(prices: PriceRange[], t: (key: string) => string): ServiceConfig[] {
  const p = (id: number) => prices.find(x => x.id === id)

  return [
    {
      id: 1, name: p(1)?.service || 'Red WiFi Corporativa',
      icon: Wifi, baseMin: p(1)?.min_price ?? 500, baseMax: p(1)?.max_price ?? 1500, unit: '€',
      fields: [
        { key: 'area', label: t('calc.area'), icon: Square, type: 'number', placeholder: 'm²', min: 20, max: 10000 },
        { key: 'users', label: t('calc.users'), icon: Users, type: 'number', placeholder: t('calc.users_placeholder'), min: 1, max: 500 },
        { key: 'aps', label: t('calc.aps'), icon: Monitor, type: 'number', placeholder: t('calc.aps_placeholder'), min: 1, max: 50 },
      ]
    },
    {
      id: 2, name: p(2)?.service || 'Red WiFi (100-500m²)',
      icon: Wifi, baseMin: p(2)?.min_price ?? 1500, baseMax: p(2)?.max_price ?? 4000, unit: '€',
      fields: [
        { key: 'area', label: t('calc.area'), icon: Square, type: 'number', placeholder: 'm²', min: 100, max: 5000 },
        { key: 'users', label: t('calc.users'), icon: Users, type: 'number', placeholder: t('calc.users_placeholder'), min: 10, max: 1000 },
        { key: 'aps', label: t('calc.aps'), icon: Monitor, type: 'number', placeholder: t('calc.aps_placeholder'), min: 2, max: 50 },
      ]
    },
    {
      id: 3, name: p(3)?.service || 'Cableado Estructurado',
      icon: Server, baseMin: p(3)?.min_price ?? 80, baseMax: p(3)?.max_price ?? 150, unit: '€/puesto',
      fields: [
        { key: 'workstations', label: t('calc.workstations'), icon: Monitor, type: 'number', placeholder: t('calc.workstations_placeholder'), min: 1, max: 500 },
        { key: 'cable_category', label: t('calc.cable_category'), icon: Zap, type: 'select', options: [
          { label: 'Cat6 — 1 Gbps', multiplier: 1 },
          { label: 'Cat6A — 10 Gbps', multiplier: 1.4 },
          { label: 'Fibra óptica', multiplier: 2.5 },
        ]},
      ]
    },
    {
      id: 4, name: p(4)?.service || 'Servidor NAS',
      icon: HardDrive, baseMin: p(4)?.min_price ?? 800, baseMax: p(4)?.max_price ?? 2500, unit: '€',
      fields: [
        { key: 'nas_bays', label: t('calc.nas_bays'), icon: Database, type: 'select', options: [
          { label: '2 bahías', multiplier: 0.7 },
          { label: '4 bahías', multiplier: 1 },
          { label: '6 bahías', multiplier: 1.3 },
          { label: '8 bahías', multiplier: 1.6 },
        ]},
        { key: 'storage', label: t('calc.storage_tb'), icon: HardDrive, type: 'number', placeholder: 'TB', min: 1, max: 200 },
      ]
    },
    {
      id: 5, name: p(5)?.service || 'Servidor en Rack',
      icon: Server, baseMin: p(5)?.min_price ?? 2500, baseMax: p(5)?.max_price ?? 8000, unit: '€',
      fields: [
        { key: 'form_factor', label: t('calc.form_factor'), icon: Server, type: 'select', options: [
          { label: 'Torre', multiplier: 0.8 },
          { label: '1U', multiplier: 1 },
          { label: '2U', multiplier: 1.2 },
          { label: '4U', multiplier: 1.5 },
        ]},
        { key: 'ram', label: t('calc.ram'), icon: Zap, type: 'select', options: [
          { label: '32 GB', multiplier: 0.8 },
          { label: '64 GB', multiplier: 1 },
          { label: '128 GB', multiplier: 1.3 },
          { label: '256 GB+', multiplier: 1.7 },
        ]},
        { key: 'storage_tb', label: t('calc.storage_tb'), icon: HardDrive, type: 'number', placeholder: 'TB', min: 1, max: 500 },
      ]
    },
    {
      id: 6, name: p(6)?.service || 'Backup 3-2-1',
      icon: Database, baseMin: p(6)?.min_price ?? 400, baseMax: p(6)?.max_price ?? 1800, unit: '€',
      fields: [
        { key: 'data_tb', label: t('calc.data_tb'), icon: HardDrive, type: 'number', placeholder: 'TB', min: 0.1, max: 100, step: 0.1 },
        { key: 'retention', label: t('calc.retention'), icon: Clock, type: 'select', options: [
          { label: '30 días', multiplier: 1 },
          { label: '90 días', multiplier: 1.5 },
          { label: '180 días', multiplier: 2 },
          { label: '365 días', multiplier: 3 },
        ]},
      ]
    },
    {
      id: 7, name: p(7)?.service || 'Auditoría TI',
      icon: FileText, baseMin: 0, baseMax: 0, unit: '€',
      fields: [
        { key: 'employees', label: t('calc.employees'), icon: Users, type: 'number', placeholder: t('calc.employees_placeholder'), min: 1, max: 5000 },
        { key: 'scope', label: t('calc.scope'), icon: Building2, type: 'select', options: [
          { label: t('calc.scope_network'), multiplier: 1 },
          { label: t('calc.scope_full'), multiplier: 2 },
          { label: t('calc.scope_security'), multiplier: 1.5 },
        ]},
      ]
    },
    {
      id: 8, name: p(8)?.service || 'Mantenimiento Mensual',
      icon: Clock, baseMin: p(8)?.min_price ?? 100, baseMax: p(8)?.max_price ?? 350, unit: '€/mes',
      fields: [
        { key: 'devices', label: t('calc.devices'), icon: Monitor, type: 'number', placeholder: t('calc.devices_placeholder'), min: 1, max: 500 },
        { key: 'sla', label: t('calc.sla'), icon: Clock, type: 'select', options: [
          { label: '8×5 — Next business day', multiplier: 0.7 },
          { label: '8×5 — 4h response', multiplier: 1 },
          { label: '24×7 — 4h response', multiplier: 1.5 },
          { label: '24×7 — 1h response', multiplier: 2.5 },
        ]},
      ]
    },
    {
      id: 9, name: p(9)?.service || 'Soporte Técnico Premium',
      icon: HeadphonesIcon, baseMin: p(9)?.min_price ?? 200, baseMax: p(9)?.max_price ?? 800, unit: '€/mes',
      fields: [
        { key: 'users_supported', label: t('calc.users_supported'), icon: Users, type: 'number', placeholder: t('calc.users_supported_placeholder'), min: 1, max: 1000 },
        { key: 'sla', label: t('calc.sla'), icon: Clock, type: 'select', options: [
          { label: '8×5 — 4h response', multiplier: 0.8 },
          { label: '24×7 — 4h response', multiplier: 1 },
          { label: '24×7 — 2h response', multiplier: 1.4 },
          { label: '24×7 — 1h onsite', multiplier: 2 },
        ]},
      ]
    },
    {
      id: 10, name: p(10)?.service || 'Consultoría TI & Cloud',
      icon: Cloud, baseMin: p(10)?.min_price ?? 400, baseMax: p(10)?.max_price ?? 2000, unit: '€',
      fields: [
        { key: 'users_cloud', label: t('calc.users_cloud'), icon: Users, type: 'number', placeholder: t('calc.users_cloud_placeholder'), min: 1, max: 5000 },
        { key: 'migration_type', label: t('calc.migration'), icon: Cloud, type: 'select', options: [
          { label: t('calc.migration_audit'), multiplier: 0.5 },
          { label: t('calc.migration_hybrid'), multiplier: 1 },
          { label: t('calc.migration_full'), multiplier: 1.8 },
        ]},
      ]
    },
    {
      id: 11, name: p(11)?.service || 'Firewall & Seguridad',
      icon: Shield, baseMin: p(11)?.min_price ?? 600, baseMax: p(11)?.max_price ?? 2500, unit: '€',
      fields: [
        { key: 'users_fw', label: t('calc.users_fw'), icon: Users, type: 'number', placeholder: t('calc.users_fw_placeholder'), min: 1, max: 5000 },
        { key: 'features', label: t('calc.features'), icon: Shield, type: 'select', options: [
          { label: 'Firewall + VPN', multiplier: 0.8 },
          { label: 'Firewall + VPN + IDS/IPS', multiplier: 1 },
          { label: 'NGFW completo (UTM)', multiplier: 1.5 },
          { label: 'HA + NGFW (alta disponibilidad)', multiplier: 2.2 },
        ]},
      ]
    },
    {
      id: 12, name: p(12)?.service || 'CCTV IP',
      icon: Camera, baseMin: p(12)?.min_price ?? 180, baseMax: p(12)?.max_price ?? 400, unit: '€/cámara',
      fields: [
        { key: 'cameras', label: t('calc.cameras'), icon: Camera, type: 'number', placeholder: t('calc.cameras_placeholder'), min: 1, max: 200 },
        { key: 'resolution', label: t('calc.resolution'), icon: Camera, type: 'select', options: [
          { label: '2 MP (1080p)', multiplier: 0.7 },
          { label: '4 MP (1440p)', multiplier: 1 },
          { label: '8 MP (4K)', multiplier: 1.5 },
          { label: '12 MP (4K+)', multiplier: 2 },
        ]},
        { key: 'storage_days', label: t('calc.storage_days'), icon: Database, type: 'select', options: [
          { label: '7 días', multiplier: 0.8 },
          { label: '15 días', multiplier: 1 },
          { label: '30 días', multiplier: 1.3 },
          { label: '60 días', multiplier: 1.7 },
        ]},
      ]
    },
    {
      id: 13, name: p(13)?.service || 'Control de Acceso',
      icon: Lock, baseMin: p(13)?.min_price ?? 300, baseMax: p(13)?.max_price ?? 800, unit: '€/puerta',
      fields: [
        { key: 'doors', label: t('calc.doors'), icon: Lock, type: 'number', placeholder: t('calc.doors_placeholder'), min: 1, max: 100 },
        { key: 'auth_type', label: t('calc.auth_type'), icon: Lock, type: 'select', options: [
          { label: 'Tarjeta RFID', multiplier: 0.8 },
          { label: 'Huella dactilar', multiplier: 1 },
          { label: 'Tarjeta + Huella', multiplier: 1.3 },
          { label: 'Reconocimiento facial', multiplier: 1.8 },
        ]},
      ]
    },
  ]
}

function calcPrice(config: ServiceConfig, values: Record<string, number | string>): { min: number; max: number } | null {
  if (config.id === 7) return null

  const perUnitIds = [3, 12, 13]
  const isPerUnit = perUnitIds.includes(config.id)
  let qty = 1
  let multiplier = 1

  for (const field of config.fields) {
    const val = values[field.key]
    if (val === undefined || val === '' || val === 0) return null

    if (field.type === 'number') {
      const num = Number(val)
      if (isPerUnit && ['workstations', 'cameras', 'doors'].includes(field.key)) {
        qty = Math.max(qty, Math.ceil(num))
        continue
      }
      if (field.key === 'aps') {
        multiplier *= 1 + (Math.min(num, 20) - 1) * 0.12
        continue
      }
      if (field.key === 'devices') {
        multiplier *= 1 + (Math.min(num, 100) - 1) * 0.04
        continue
      }
      if (field.key === 'area') {
        const ratio = Math.min(num / 100, 5)
        multiplier *= 1 + (ratio - 1) * 0.15
        continue
      }
      if (['users', 'users_supported', 'users_fw', 'users_cloud', 'employees'].includes(field.key)) {
        const ratio = Math.min(num / 10, 20)
        multiplier *= 1 + (ratio - 1) * 0.06
        continue
      }
      if (['storage', 'storage_tb', 'data_tb'].includes(field.key)) {
        const ratio = Math.min(num / 4, 10)
        multiplier *= 1 + (ratio - 1) * 0.12
        continue
      }
    }

    if (field.type === 'select') {
      const opt = field.options?.find(o => o.label === val)
      if (opt) multiplier *= opt.multiplier
    }
  }

  multiplier = Math.max(0.5, Math.min(multiplier, 4))

  const min = Math.round(config.baseMin * multiplier * qty)
  const max = Math.round(config.baseMax * multiplier * qty)
  return { min, max }
}

function getVolumeDiscount(total: number): number {
  if (total >= 20000) return 0.15
  if (total >= 10000) return 0.10
  if (total >= 5000) return 0.05
  return 0
}

function loadSaved(): SavedBudget[] {
  try {
    return JSON.parse(localStorage.getItem('forj_budgets') || '[]')
  } catch { return [] }
}

function saveToStorage(budget: SavedBudget) {
  const list = loadSaved()
  list.unshift(budget)
  localStorage.setItem('forj_budgets', JSON.stringify(list.slice(0, 20)))
}

function deleteFromStorage(id: string) {
  const list = loadSaved().filter(b => b.id !== id)
  localStorage.setItem('forj_budgets', JSON.stringify(list))
}

const packages: PackageDef[] = [
  {
    id: 'startup',
    name: 'pkg.startup',
    desc: 'pkg.startup_desc',
    icon: Sparkles,
    color: '#3b82f6',
    discount: 0.10,
    services: [
      { configId: 1, values: { area: 80, users: 15, aps: 3 } },
      { configId: 3, values: { workstations: 10, cable_category: 'Cat6 — 1 Gbps' } },
      { configId: 4, values: { nas_bays: '4 bahías', storage: 8 } },
      { configId: 8, values: { devices: 20, sla: '8×5 — Next business day' } },
    ]
  },
  {
    id: 'professional',
    name: 'pkg.professional',
    desc: 'pkg.professional_desc',
    icon: Rocket,
    color: '#8b5cf6',
    discount: 0.15,
    services: [
      { configId: 2, values: { area: 300, users: 50, aps: 6 } },
      { configId: 3, values: { workstations: 25, cable_category: 'Cat6A — 10 Gbps' } },
      { configId: 4, values: { nas_bays: '6 bahías', storage: 24 } },
      { configId: 6, values: { data_tb: 4, retention: '90 días' } },
      { configId: 11, values: { users_fw: 50, features: 'Firewall + VPN + IDS/IPS' } },
      { configId: 8, values: { devices: 50, sla: '8×5 — 4h response' } },
    ]
  },
  {
    id: 'enterprise',
    name: 'pkg.enterprise',
    desc: 'pkg.enterprise_desc',
    icon: Star,
    color: '#d4a845',
    discount: 0.20,
    services: [
      { configId: 2, values: { area: 800, users: 150, aps: 12 } },
      { configId: 3, values: { workstations: 60, cable_category: 'Fibra óptica' } },
      { configId: 5, values: { form_factor: '2U', ram: '128 GB', storage_tb: 48 } },
      { configId: 6, values: { data_tb: 10, retention: '180 días' } },
      { configId: 11, values: { users_fw: 200, features: 'NGFW completo (UTM)' } },
      { configId: 12, values: { cameras: 12, resolution: '8 MP (4K)', storage_days: '30 días' } },
      { configId: 13, values: { doors: 4, auth_type: 'Tarjeta + Huella' } },
      { configId: 10, values: { users_cloud: 150, migration_type: 'Híbrida (on-premise + cloud)' } },
      { configId: 9, values: { users_supported: 150, sla: '24×7 — 4h response' } },
    ]
  },
]

export function PricesSection() {
  const { t } = useTranslation()
  const { user, isAuthenticated } = useAuth()
  const [prices, setPrices] = useState<PriceRange[]>([])
  const [configs, setConfigs] = useState<ServiceConfig[]>([])
  const [step, setStep] = useState(STEP_PACKAGE)
  const [selectedPackage, setSelectedPackage] = useState<string | null>(null)
  const [expanded, setExpanded] = useState<Record<number, boolean>>({})
  const [values, setValues] = useState<Record<number, Record<string, number | string>>>({})
  const [totals, setTotals] = useState<Record<number, { min: number; max: number } | null>>({})
  const [contactName, setContactName] = useState('')
  const [contactEmail, setContactEmail] = useState('')
  const [contactPhone, setContactPhone] = useState('')
  const [contactCompany, setContactCompany] = useState('')
  const [message, setMessage] = useState('')
  const [saved, setSaved] = useState<SavedBudget[]>([])
  const [showSaved, setShowSaved] = useState(false)
  const [savedId, setSavedId] = useState<string | null>(null)
  const [saving, setSaving] = useState(false)
  const printRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    getPriceRanges().then(data => {
      setPrices(data)
      setConfigs(buildConfigs(data, t))
    }).catch(() => {})
    setSaved(loadSaved())
  }, [])

  useEffect(() => {
    if (selectedPackage && configs.length) {
      const pkg = packages.find(p => p.id === selectedPackage)
      if (pkg) {
        const newValues: Record<number, Record<string, number | string>> = {}
        for (const svc of pkg.services) {
          newValues[svc.configId] = { ...svc.values }
        }
        setValues(newValues)
        const exps: Record<number, boolean> = {}
        pkg.services.forEach(s => { exps[s.configId] = true })
        setExpanded(exps)
      }
    }
  }, [selectedPackage, configs])

  useEffect(() => {
    const newTotals: Record<number, { min: number; max: number } | null> = {}
    for (const config of configs) {
      const v = values[config.id] || {}
      newTotals[config.id] = calcPrice(config, v)
    }
    setTotals(newTotals)
  }, [values, configs])

  const toggleExpand = (id: number) => {
    setExpanded(prev => ({ ...prev, [id]: !prev[id] }))
    if (!values[id]) setValues(prev => ({ ...prev, [id]: {} }))
  }

  const updateValue = (configId: number, key: string, val: number | string) => {
    setValues(prev => ({
      ...prev,
      [configId]: { ...(prev[configId] || {}), [key]: val }
    }))
  }

  const activeConfigs = configs.filter(c => {
    const v = values[c.id]
    return v && Object.values(v).some(x => x !== '' && x !== undefined && x !== 0)
  })

  let rawMin = 0; let rawMax = 0
  for (const c of activeConfigs) {
    const t = totals[c.id]
    if (t) { rawMin += t.min; rawMax += t.max }
  }
  const discount = selectedPackage
    ? packages.find(p => p.id === selectedPackage)!.discount
    : getVolumeDiscount(rawMin)
  const discMin = Math.round(rawMin * (1 - discount))
  const discMax = Math.round(rawMax * (1 - discount))
  const grandMin = discMin
  const grandMax = discMax

  const handlePackageSelect = (pkgId: string | null) => {
    setSelectedPackage(pkgId)
    if (pkgId) {
      setStep(STEP_REVIEW)
    } else {
      setValues({})
      setExpanded({})
      setStep(STEP_CONFIGURE)
    }
  }

  const totalItems = () => activeConfigs.map(c => ({
    name: c.name,
    min: totals[c.id]?.min ?? 0,
    max: totals[c.id]?.max ?? 0,
  })).filter(i => i.min > 0 || i.max > 0)

  const handleSave = () => {
    setSaving(true)
    const budget: SavedBudget = {
      id: Date.now().toString(36),
      date: new Date().toISOString(),
      name: contactName || user?.name || '',
      email: contactEmail || user?.email || '',
      phone: contactPhone,
      items: totalItems(),
      totalMin: grandMin,
      totalMax: grandMax,
      discount,
      packageName: selectedPackage ? t(packages.find(p => p.id === selectedPackage)!.name) : null,
    }
    saveToStorage(budget)
    setSaved(loadSaved())
    setSavedId(budget.id)
    setSaving(false)
  }

  const handlePrint = () => {
    window.print()
  }

  const handleDelete = (id: string) => {
    deleteFromStorage(id)
    setSaved(loadSaved())
  }

  const loadBudget = (b: SavedBudget) => {
    setContactName(b.name)
    setContactEmail(b.email)
    setContactPhone(b.phone)
    setSavedId(null)
    setShowSaved(false)
    if (b.packageName) {
      const pkg = packages.find(p => t(p.name) === b.packageName)
      if (pkg) {
        setSelectedPackage(pkg.id)
        const newValues: Record<number, Record<string, number | string>> = {}
        for (const svc of pkg.services) {
          newValues[svc.configId] = { ...svc.values }
        }
        setValues(newValues)
      }
    }
    setStep(STEP_REVIEW)
  }

  const requestQuote = () => {
    const lines = totalItems().map(i => `${i.name}: ${i.min}€${i.max > i.min ? ` — ${i.max}€` : ''}`).join('\n')
    const discountLine = discount > 0 ? `\nDescuento: ${Math.round(discount * 100)}%` : ''
    const pkgLine = selectedPackage ? `\nPack: ${t(packages.find(p => p.id === selectedPackage)!.name)}` : ''
    const msg = encodeURIComponent(
      `📋 Solicitud de presupuesto - Forj\n\n` +
      `Nombre: ${contactName || user?.name || ''}\nEmail: ${contactEmail || user?.email || ''}\nTeléfono: ${contactPhone}\nEmpresa: ${contactCompany}\n\n` +
      `--- Servicios ---\n${lines}\n${pkgLine}${discountLine}\n\n` +
      `Total estimado: ${grandMin}€${grandMax > grandMin ? ` — ${grandMax}€` : ''}\n\n` +
      `${message ? `Notas: ${message}` : ''}`
    )
    window.open(`https://wa.me/34600000000?text=${msg}`, '_blank')
  }

  const printStyles = `
    @media print {
      body { background: white !important; color: black !important; }
      nav, .no-print { display: none !important; }
      .print-only { display: block !important; }
    }
    @media screen {
      .print-only { display: none !important; }
    }
  `

  const progressSteps = [
    { label: t('calc.step_package'), key: STEP_PACKAGE },
    { label: t('calc.step_configure'), key: STEP_CONFIGURE },
    { label: t('calc.step_review'), key: STEP_REVIEW },
  ]

  return (
    <>
      <style>{printStyles}</style>

      <section className="py-16 md:py-32">
        <div className="mx-auto max-w-6xl px-6">
          <div className="text-center mb-12">
            <span className="inline-block text-[11px] tracking-[0.25em] uppercase text-zinc-600 mb-4 font-mono">
              {t('prices.badge')}
            </span>
            <h2 className="text-3xl md:text-5xl font-bold text-white mb-4">{t('prices.heading')}</h2>
            <p className="text-sm text-zinc-500 max-w-2xl mx-auto">{t('prices.subtitle')}</p>
          </div>

          <div className="flex items-center justify-center gap-2 mb-12 no-print">
            {progressSteps.map((ps, i) => {
              const active = step >= ps.key
              return (
                <div key={ps.key} className="flex items-center gap-2">
                  <div className={`flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-medium transition-colors ${
                    active ? 'bg-[#d4a845]/10 text-[#d4a845] border border-[#d4a845]/20' : 'text-zinc-600'
                  }`}>
                    <div className={`size-5 rounded-full flex items-center justify-center text-[10px] font-bold ${
                      active ? 'bg-[#d4a845] text-black' : 'bg-zinc-800 text-zinc-500'
                    }`}>
                      {i + 1}
                    </div>
                    {ps.label}
                  </div>
                  {i < progressSteps.length - 1 && <div className={`w-8 h-px ${active ? 'bg-[#d4a845]/30' : 'bg-zinc-800'}`} />}
                </div>
              )
            })}
          </div>

          <div className="flex justify-end mb-6 no-print">
            <button
              onClick={() => setShowSaved(!showSaved)}
              className="flex items-center gap-2 text-xs text-zinc-500 hover:text-white transition-colors bg-transparent border-none cursor-pointer"
            >
              <Save className="size-3.5" />
              {t('calc.saved_budgets')} ({saved.length})
            </button>
          </div>

          {showSaved && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              className="mb-8 p-6 rounded-2xl border border-white/[0.06] bg-white/[0.02] no-print"
            >
              <h3 className="text-sm font-semibold text-white mb-4">{t('calc.saved_budgets')}</h3>
              {saved.length === 0 ? (
                <p className="text-xs text-zinc-500">{t('calc.no_saved')}</p>
              ) : (
                <div className="space-y-2 max-h-60 overflow-y-auto">
                  {saved.map(b => (
                    <div key={b.id} className="flex items-center justify-between p-3 rounded-lg bg-white/[0.02] border border-white/[0.04]">
                      <button
                        onClick={() => loadBudget(b)}
                        className="text-left bg-transparent border-none cursor-pointer flex-1"
                      >
                        <p className="text-sm text-white">{b.name || 'Sin nombre'}</p>
                        <p className="text-xs text-zinc-500">
                          {new Date(b.date).toLocaleDateString()} — {b.totalMin}€{b.totalMax > b.totalMin ? ` — ${b.totalMax}€` : ''}
                          {b.packageName && ` · ${b.packageName}`}
                        </p>
                      </button>
                      <button
                        onClick={() => handleDelete(b.id)}
                        className="text-zinc-600 hover:text-red-400 transition-colors bg-transparent border-none cursor-pointer p-1"
                      >
                        <Trash2 className="size-3.5" />
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </motion.div>
          )}

          {step === STEP_PACKAGE && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
            >
              <div className="text-center mb-10">
                <Package className="size-8 text-[#d4a845] mx-auto mb-3" />
                <h3 className="text-2xl font-bold text-white mb-2">{t('calc.choose_package')}</h3>
                <p className="text-sm text-zinc-500">{t('calc.choose_package_desc')}</p>
              </div>

              <div className="grid md:grid-cols-4 gap-4 mb-6">
                {packages.map(pkg => (
                  <button
                    key={pkg.id}
                    onClick={() => handlePackageSelect(pkg.id)}
                    className="relative p-6 rounded-2xl border border-white/[0.06] bg-white/[0.02] hover:border-white/15 hover:bg-white/[0.04] transition-all text-left bg-transparent cursor-pointer group"
                  >
                    <div className="flex items-center gap-3 mb-4">
                      <div className="flex size-10 items-center justify-center rounded-xl bg-white/[0.04] text-zinc-400 group-hover:text-white transition-colors">
                        <pkg.icon className="size-5" />
                      </div>
                      <div>
                        <p className="text-base font-semibold text-white">{t(pkg.name)}</p>
                        <span className="text-[10px] font-mono text-green-400">{Math.round(pkg.discount * 100)}% {t('calc.discount')}</span>
                      </div>
                    </div>
                    <p className="text-xs text-zinc-500 leading-relaxed">{t(pkg.desc)}</p>
                  </button>
                ))}
                <button
                  onClick={() => handlePackageSelect(null)}
                  className="relative p-6 rounded-2xl border border-dashed border-white/[0.06] bg-white/[0.01] hover:border-white/15 hover:bg-white/[0.03] transition-all text-left bg-transparent cursor-pointer group"
                >
                  <div className="flex items-center gap-3 mb-4">
                    <div className="flex size-10 items-center justify-center rounded-xl bg-white/[0.04] text-zinc-400 group-hover:text-white transition-colors">
                      <Plus className="size-5" />
                    </div>
                    <p className="text-base font-semibold text-white">{t('calc.custom')}</p>
                  </div>
                  <p className="text-xs text-zinc-500 leading-relaxed">{t('calc.custom_desc')}</p>
                </button>
              </div>

              <div className="mt-12">
                <div className="text-center mb-8">
                  <h3 className="text-xl font-bold text-white mb-2">{t('calc.compare_plans')}</h3>
                  <p className="text-sm text-zinc-500">{t('calc.compare_plans_desc')}</p>
                </div>
                <div className="overflow-x-auto rounded-2xl border border-white/[0.06]">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b border-white/[0.06]">
                        <th className="text-left p-4 text-zinc-400 font-medium">{t('calc.service')}</th>
                        {packages.map(pkg => (
                          <th key={pkg.id} className="p-4 text-center">
                            <div className="flex items-center justify-center gap-2">
                              <pkg.icon className="size-4" style={{ color: pkg.color }} />
                              <span className="text-white font-semibold">{t(pkg.name)}</span>
                            </div>
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {[
                        { id: 1, label: 'Red WiFi (100m²)' },
                        { id: 2, label: 'Red WiFi (500m²)' },
                        { id: 3, label: 'Cableado Estructurado' },
                        { id: 4, label: 'Servidor NAS' },
                        { id: 5, label: 'Servidor Rack' },
                        { id: 6, label: 'Backup 3-2-1' },
                        { id: 11, label: 'Firewall' },
                        { id: 12, label: 'CCTV' },
                        { id: 13, label: 'Control Acceso' },
                        { id: 10, label: 'Consultoría Cloud' },
                        { id: 9, label: 'Soporte Premium' },
                        { id: 8, label: 'Mantenimiento' },
                      ].map((svc, idx) => (
                        <tr key={svc.id} className={idx % 2 === 0 ? 'bg-white/[0.01]' : ''}>
                          <td className="p-4 text-zinc-300">{svc.label}</td>
                          {packages.map(pkg => (
                            <td key={pkg.id} className="p-4 text-center">
                              {pkg.services.some(s => s.configId === svc.id) ? (
                                <Check className="size-4 mx-auto text-green-400" />
                              ) : (
                                <span className="text-zinc-700">—</span>
                              )}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </motion.div>
          )}

          {step === STEP_CONFIGURE && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
            >
              <div className="text-center mb-8">
                <h3 className="text-xl font-bold text-white mb-2">{t('calc.configure_services')}</h3>
                <p className="text-sm text-zinc-500">{t('calc.configure_services_desc')}</p>
              </div>
              <div className="grid md:grid-cols-2 gap-4 mb-8">
                {configs.map((config, idx) => {
                  const isExpanded = expanded[config.id]
                  const total = totals[config.id]
                  const hasValues = Object.values(values[config.id] || {}).some(v => v !== '' && v !== undefined)

                  return (
                    <motion.div
                      key={config.id}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: idx * 0.04 }}
                      className="relative rounded-2xl border border-white/[0.06] bg-white/[0.02] overflow-hidden transition-all duration-300 hover:border-white/15"
                    >
                      <BorderBeam duration={10} lightColor="#d4a845" borderWidth={1} className={isExpanded ? 'opacity-100' : 'opacity-0'} />
                      <button
                        onClick={() => toggleExpand(config.id)}
                        className="w-full flex items-center justify-between p-5 bg-transparent border-none cursor-pointer text-left"
                      >
                        <div className="flex items-center gap-3">
                          <div className={`flex size-10 shrink-0 items-center justify-center rounded-xl transition-colors ${
                            isExpanded ? 'bg-[#d4a845]/10 text-[#d4a845]' : 'bg-white/[0.04] text-zinc-500'
                          }`}>
                            <config.icon className="size-5" />
                          </div>
                          <div>
                            <h3 className="text-base font-semibold text-white">{config.name}</h3>
                            <p className="text-xs text-zinc-500">
                              {config.baseMin > 0 ? `Desde ${config.baseMin}${config.unit}` : 'Gratis'}
                            </p>
                          </div>
                        </div>
                        <div className="flex items-center gap-3">
                          {hasValues && total && (
                            <span className="text-sm font-medium text-[#d4a845] whitespace-nowrap">
                              {total.min}€{total.max > total.min ? ` — ${total.max}€` : ''}
                            </span>
                          )}
                          <ChevronDown className={`size-4 text-zinc-500 transition-transform duration-300 ${isExpanded ? 'rotate-180' : ''}`} />
                        </div>
                      </button>

                      <AnimatePresence>
                        {isExpanded && (
                          <motion.div
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: 'auto', opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.3 }}
                            className="overflow-hidden"
                          >
                            <div className="px-5 pb-5 pt-2 border-t border-white/[0.04] space-y-4">
                              {config.fields.map(field => (
                                <div key={field.key}>
                                  <label className="flex items-center gap-2 text-xs text-zinc-400 mb-2">
                                    <field.icon className="size-3.5" />
                                    {field.label}
                                  </label>
                                  {field.type === 'select' ? (
                                    <select
                                      value={(values[config.id]?.[field.key] as string) || ''}
                                      onChange={e => updateValue(config.id, field.key, e.target.value)}
                                      className="w-full bg-white/[0.04] border border-white/[0.08] rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-[#d4a845]/50 transition-colors appearance-none cursor-pointer"
                                    >
                                      <option value="" className="bg-zinc-900">{t('calc.select')}</option>
                                      {field.options?.map(o => (
                                        <option key={o.label} value={o.label} className="bg-zinc-900">{o.label}</option>
                                      ))}
                                    </select>
                                  ) : (
                                    <div className="relative">
                                      <input
                                        type="number"
                                        min={field.min}
                                        max={field.max}
                                        step={field.step}
                                        placeholder={field.placeholder}
                                        value={(values[config.id]?.[field.key] as string) || ''}
                                        onChange={e => updateValue(config.id, field.key, e.target.value)}
                                        className="w-full bg-white/[0.04] border border-white/[0.08] rounded-lg px-3 py-2 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[#d4a845]/50 transition-colors [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
                                      />
                                      {field.placeholder && (
                                        <span className="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-zinc-600 pointer-events-none">
                                          {field.placeholder}
                                        </span>
                                      )}
                                    </div>
                                  )}
                                </div>
                              ))}
                              {total && (
                                <div className="pt-2 border-t border-white/[0.04] flex justify-between items-center">
                                  <span className="text-xs text-zinc-500">{t('calc.estimated_price')}</span>
                                  <span className="text-base font-bold text-[#d4a845]">
                                    {total.min}€{total.max > total.min ? ` — ${total.max}€` : ''}
                                  </span>
                                </div>
                              )}
                            </div>
                          </motion.div>
                        )}
                      </AnimatePresence>
                    </motion.div>
                  )
                })}
              </div>
            </motion.div>
          )}

          {(step === STEP_CONFIGURE || step === STEP_REVIEW) && activeConfigs.length > 0 && (
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              className="relative rounded-2xl border border-[#d4a845]/30 bg-gradient-to-b from-[#d4a845]/[0.03] to-transparent p-8 mb-12"
            >
              <BorderBeam duration={8} lightColor="#d4a845" borderWidth={1} />

              <div className="text-center mb-6">
                <div className="flex items-center justify-center gap-2 mb-3">
                  <Calculator className="size-5 text-[#d4a845]" />
                  <span className="text-sm font-mono text-[#d4a845]">{t('prices.calculator_heading')}</span>
                </div>
                <p className="text-sm text-zinc-500 mb-4">{t('prices.calculator_desc')}</p>

                <div className="flex flex-wrap gap-2 justify-center mb-6">
                  {activeConfigs.map(c => (
                    <span key={c.id} className="text-xs bg-[#d4a845]/10 text-[#d4a845] px-3 py-1 rounded-full border border-[#d4a845]/20">
                      {c.name}
                    </span>
                  ))}
                </div>

                <div className="text-center mb-6">
                  <p className="text-sm text-zinc-400 mb-2">{t('calc.estimated_total')}</p>
                  <p className="text-4xl md:text-5xl font-bold text-white">
                    {grandMin.toLocaleString()}€{grandMax > grandMin ? ` — ${grandMax.toLocaleString()}€` : ''}
                  </p>
                  {discount > 0 && (
                    <p className="text-xs text-green-400 mt-2">
                      {t('calc.includes_discount')} {Math.round(discount * 100)}%
                    </p>
                  )}
                  <p className="text-[10px] text-zinc-600 mt-1">{t('prices.note')}</p>
                </div>
              </div>

              {step === STEP_CONFIGURE && (
                <div className="flex justify-center no-print">
                  <HoverBorderGradient
                    as="button"
                    onClick={() => setStep(STEP_REVIEW)}
                    className="inline-flex items-center gap-2 px-8 py-4 text-base font-medium"
                  >
                    {t('calc.continue_review')} <ArrowUpRight className="size-4" />
                  </HoverBorderGradient>
                </div>
              )}

              {step === STEP_REVIEW && (
                <div className="no-print">
                  <div className="grid md:grid-cols-4 gap-3 mb-6">
                    <input
                      type="text"
                      placeholder={t('calc.name_placeholder')}
                      value={contactName}
                      onChange={e => setContactName(e.target.value)}
                      className="w-full bg-white/[0.04] border border-white/[0.08] rounded-lg px-4 py-3 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[#d4a845]/50 transition-colors"
                    />
                    <input
                      type="email"
                      placeholder={t('calc.email_placeholder')}
                      value={contactEmail}
                      onChange={e => setContactEmail(e.target.value)}
                      className="w-full bg-white/[0.04] border border-white/[0.08] rounded-lg px-4 py-3 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[#d4a845]/50 transition-colors"
                    />
                    <input
                      type="tel"
                      placeholder={t('calc.phone_placeholder')}
                      value={contactPhone}
                      onChange={e => setContactPhone(e.target.value)}
                      className="w-full bg-white/[0.04] border border-white/[0.08] rounded-lg px-4 py-3 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[#d4a845]/50 transition-colors"
                    />
                    <input
                      type="text"
                      placeholder={t('calc.company_placeholder')}
                      value={contactCompany}
                      onChange={e => setContactCompany(e.target.value)}
                      className="w-full bg-white/[0.04] border border-white/[0.08] rounded-lg px-4 py-3 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[#d4a845]/50 transition-colors"
                    />
                  </div>
                  <textarea
                    placeholder={t('calc.message_placeholder')}
                    value={message}
                    onChange={e => setMessage(e.target.value)}
                    rows={2}
                    className="w-full bg-white/[0.04] border border-white/[0.08] rounded-lg px-4 py-3 text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[#d4a845]/50 transition-colors mb-6 resize-none"
                  />

                  <div className="flex flex-wrap gap-3 justify-center">
                    <HoverBorderGradient
                      as="button"
                      onClick={requestQuote}
                      disabled={!contactEmail && !contactName}
                      className="inline-flex items-center gap-2 px-6 py-3 text-sm font-medium disabled:opacity-40 disabled:cursor-not-allowed"
                    >
                      <FileText className="size-4" /> {t('calc.send_whatsapp')}
                    </HoverBorderGradient>
                    <button
                      onClick={() => window.dispatchEvent(new CustomEvent('open-contact'))}
                      className="inline-flex items-center gap-2 px-6 py-3 text-sm font-medium rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/[0.08] text-white transition-colors cursor-pointer"
                    >
                      {t('calc.contact_form')}
                    </button>
                    <button
                      onClick={handleSave}
                      disabled={saving}
                      className="inline-flex items-center gap-2 px-4 py-3 text-sm rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/[0.08] text-zinc-300 hover:text-white transition-colors cursor-pointer disabled:opacity-40"
                    >
                      <Save className="size-4" /> {saving ? t('common.saving') : t('calc.save_budget')}
                    </button>
                    <button
                      onClick={handlePrint}
                      className="inline-flex items-center gap-2 px-4 py-3 text-sm rounded-lg bg-white/[0.04] hover:bg-white/[0.08] border border-white/[0.08] text-zinc-300 hover:text-white transition-colors cursor-pointer"
                    >
                      <Printer className="size-4" /> {t('calc.print')}
                    </button>
                  </div>

                  {savedId && (
                    <motion.p
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      className="text-xs text-green-400 text-center mt-4"
                    >
                      {t('calc.saved_success')}
                    </motion.p>
                  )}
                </div>
              )}
            </motion.div>
          )}

          {activeConfigs.length === 0 && step > STEP_PACKAGE && (
            <div className="text-center py-16">
              <Calculator className="size-12 text-zinc-700 mx-auto mb-4" />
              <p className="text-zinc-500">{t('calc.no_services')}</p>
              <button
                onClick={() => handlePackageSelect(null)}
                className="mt-4 text-sm text-[#d4a845] hover:text-[#d4a845]/80 transition-colors bg-transparent border-none cursor-pointer underline underline-offset-4"
              >
                {t('calc.start_adding')}
              </button>
            </div>
          )}

          {step > STEP_PACKAGE && activeConfigs.length > 0 && (
            <div className="flex justify-center mt-8 no-print">
              <button
                onClick={() => { setStep(STEP_PACKAGE); setSelectedPackage(null) }}
                className="flex items-center gap-2 text-sm text-zinc-500 hover:text-white transition-colors bg-transparent border-none cursor-pointer"
              >
                <ChevronLeft className="size-4" />
                {t('calc.back_packages')}
              </button>
            </div>
          )}

          {step === STEP_PACKAGE && activeConfigs.length === 0 && (
            <div className="text-center mt-16">
              <p className="text-sm text-zinc-500 mb-4">{t('prices.cta')}</p>
              <HoverBorderGradient as="button" onClick={() => window.dispatchEvent(new CustomEvent('open-contact'))} className="inline-flex items-center gap-2 px-8 py-4 text-base font-medium">
                {t('prices.cta')} <ArrowUpRight className="size-4" />
              </HoverBorderGradient>
            </div>
          )}
        </div>
      </section>

      <div ref={printRef} className="print-only p-8" style={{ background: 'white', color: 'black', fontFamily: 'system-ui, sans-serif' }}>
        <div style={{ textAlign: 'center', marginBottom: 24 }}>
          <h1 style={{ fontSize: 24, fontWeight: 700, letterSpacing: '0.3em', color: '#111' }}>FORJ</h1>
          <p style={{ color: '#666', fontSize: 14 }}>{t('calc.quote_title')}</p>
        </div>
        <div style={{ marginBottom: 16 }}>
          <p style={{ fontSize: 12, color: '#444' }}><strong>{t('calc.contact')}:</strong> {contactName || user?.name || ''} — {contactEmail || user?.email || ''}{contactPhone ? ` — ${contactPhone}` : ''}</p>
          {contactCompany && <p style={{ fontSize: 12, color: '#444' }}><strong>Empresa:</strong> {contactCompany}</p>}
          {selectedPackage && <p style={{ fontSize: 12, color: '#444' }}><strong>Pack:</strong> {t(packages.find(p => p.id === selectedPackage)!.name)}</p>}
        </div>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13, marginBottom: 16 }}>
          <thead>
            <tr style={{ borderBottom: '2px solid #ddd' }}>
              <th style={{ textAlign: 'left', padding: '8px 4px', color: '#333' }}>{t('calc.service')}</th>
              <th style={{ textAlign: 'right', padding: '8px 4px', color: '#333' }}>{t('calc.estimated_price')}</th>
            </tr>
          </thead>
          <tbody>
            {totalItems().map((item, i) => (
              <tr key={i} style={{ borderBottom: '1px solid #eee' }}>
                <td style={{ padding: '8px 4px', color: '#333' }}>{item.name}</td>
                <td style={{ textAlign: 'right', padding: '8px 4px', color: '#111', fontWeight: 500 }}>
                  {item.min}€{item.max > item.min ? ` — ${item.max}€` : ''}
                </td>
              </tr>
            ))}
          </tbody>
          <tfoot>
            {discount > 0 && (
              <tr>
                <td style={{ padding: '8px 4px', color: '#666', fontSize: 12 }}>{t('calc.discount')} ({Math.round(discount * 100)}%)</td>
                <td style={{ textAlign: 'right', padding: '8px 4px', color: '#666', fontSize: 12 }}>
                  -{Math.round(rawMin * discount)}€{rawMax > rawMin ? ` — -${Math.round(rawMax * discount)}€` : ''}
                </td>
              </tr>
            )}
            <tr style={{ borderTop: '2px solid #111' }}>
              <td style={{ padding: '8px 4px', fontWeight: 700, color: '#111' }}>{t('calc.total')}</td>
              <td style={{ textAlign: 'right', padding: '8px 4px', fontWeight: 700, color: '#111', fontSize: 16 }}>
                {grandMin.toLocaleString()}€{grandMax > grandMin ? ` — ${grandMax.toLocaleString()}€` : ''}
              </td>
            </tr>
          </tfoot>
        </table>
        {message && <p style={{ fontSize: 12, color: '#666', marginTop: 16 }}><strong>Notas:</strong> {message}</p>}
        <p style={{ fontSize: 10, color: '#999', marginTop: 24, textAlign: 'center' }}>
          {t('prices.note')} · Generado el {new Date().toLocaleDateString()} · Forj — Redes Profesionales e Infraestructura TI
        </p>
      </div>
    </>
  )
}
