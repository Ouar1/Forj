import { useTranslation } from 'react-i18next'
import { Check, Zap, Wrench } from 'lucide-react'
import { BorderBeam } from '@/components/ui/border-beam'
import { HoverBorderGradient } from '@/components/ui/hover-border-gradient'

type Plan = {
  name: string
  price: string
  price_period: string
  seats: string
  features: string[]
  popular?: boolean
}

export function PricingPlans() {
  const { t } = useTranslation()
  const plans = t('pricing.plans', { returnObjects: true }) as Plan[]
  const automation = t('pricing.automation', { returnObjects: true }) as { title: string; desc: string; price: string; price_period: string }

  return (
    <div className="w-full border-b border-white/[0.04]">
      <div className="mx-auto max-w-6xl px-6 md:px-12 lg:px-20 py-28 md:py-36">
        <div className="mb-16 text-center">
          <span className="text-[11px] tracking-[0.25em] uppercase text-zinc-600 font-mono">{t('pricing.label')}</span>
          <h2 className="text-3xl md:text-5xl font-bold text-white leading-[1.05] tracking-tight mt-5">
            {t('pricing.heading')}
          </h2>
          <p className="mt-4 text-zinc-500 max-w-xl mx-auto leading-relaxed">
            {t('pricing.description')}
          </p>
        </div>

        {/* Plans */}
        <div className="grid md:grid-cols-3 gap-6">
          {plans.map((plan) => (
            <div
              key={plan.name}
              className={`relative rounded-2xl bg-white/[0.02] border border-white/[0.06] p-8 flex flex-col overflow-hidden ${
                plan.popular ? 'border-white/15' : ''
              }`}
            >
              {plan.popular && <BorderBeam duration={10} lightColor="#FAFAFA" borderWidth={1} />}
              {plan.popular && (
                <span className="absolute top-4 right-4 text-[10px] tracking-[0.2em] uppercase text-amber-500/90 bg-amber-500/10 border border-amber-500/20 px-2.5 py-1 rounded-md">
                  {t('pricing.popular')}
                </span>
              )}
              <h3 className="text-lg font-semibold text-white">{plan.name}</h3>
              <p className="text-xs text-zinc-600 mt-1">{plan.seats}</p>
              <div className="mt-6 mb-8">
                <span className="text-4xl md:text-5xl font-bold text-white tracking-tight">{plan.price}</span>
                <span className="text-sm text-zinc-500 ml-1">{plan.price_period}</span>
              </div>
              <ul className="space-y-3 mb-10 flex-1">
                {plan.features.map((f) => (
                  <li key={f} className="flex items-start gap-3 text-sm text-zinc-400">
                    <Check className="size-4 text-zinc-500 shrink-0 mt-0.5" />
                    <span className="leading-relaxed">{f}</span>
                  </li>
                ))}
              </ul>
              <HoverBorderGradient
                as="button"
                onClick={() => window.dispatchEvent(new CustomEvent('open-contact'))}
                className="w-full flex items-center justify-center gap-2 py-3.5 text-sm font-medium"
              >
                {t('pricing.cta')}
              </HoverBorderGradient>
            </div>
          ))}
        </div>

        {/* Automation block */}
        <div className="mt-6 rounded-2xl bg-white/[0.02] border border-white/[0.06] p-8 relative overflow-hidden">
          <BorderBeam duration={10} lightColor="#FAFAFA" borderWidth={1} />
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
            <div className="flex items-start gap-4">
              <div className="size-10 rounded-lg bg-white/5 flex items-center justify-center shrink-0">
                <Zap className="size-4 text-zinc-400" />
              </div>
              <div>
                <h3 className="text-lg font-semibold text-white">{automation.title}</h3>
                <p className="text-sm text-zinc-500 leading-relaxed max-w-xl mt-1">{automation.desc}</p>
              </div>
            </div>
            <div className="text-right shrink-0">
              <span className="text-2xl font-bold text-white tracking-tight block">{automation.price}</span>
              <span className="text-xs text-zinc-500">{automation.price_period}</span>
            </div>
          </div>
        </div>

        {/* Hourly note */}
        <div className="mt-6 flex items-center justify-center gap-2 text-xs text-zinc-600">
          <Wrench className="size-3.5" />
          {t('pricing.hourly')}
        </div>
      </div>
    </div>
  )
}