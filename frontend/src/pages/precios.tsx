import { BentoPricing } from '@/components/ui/bento-pricing'
import { PricesSection } from '@/components/ui/prices-section'

export function PreciosPage() {
  return (
    <>
      <div className="w-full border-b border-white/[0.04]">
        <div className="mx-auto max-w-6xl px-6 md:px-12 lg:px-20 py-28 md:py-36">
          <BentoPricing />
        </div>
      </div>
      <div className="w-full">
        <PricesSection />
      </div>
    </>
  )
}
