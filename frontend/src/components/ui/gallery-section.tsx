import { useState, useEffect } from 'react'
import { useTranslation } from 'react-i18next'
import { motion, AnimatePresence } from 'framer-motion'
import { getGallery, type GalleryItem } from '@/lib/api'

export function GallerySection() {
  const { t } = useTranslation()
  const [items, setItems] = useState<GalleryItem[]>([])
  const [filter, setFilter] = useState('all')
  const [selected, setSelected] = useState<GalleryItem | null>(null)

  useEffect(() => {
    getGallery().then(setItems).catch(() => {})
  }, [])

  const categories = ['all', 'redes', 'cableado', 'servidores']
  const filtered = filter === 'all' ? items : items.filter(i => i.category === filter)

  return (
    <section className="py-16 md:py-32">
      <div className="mx-auto max-w-6xl px-6">
        <span className="inline-block text-[11px] tracking-[0.25em] uppercase text-zinc-600 mb-4 font-mono">
          {t('gallery.badge')}
        </span>
        <h2 className="text-3xl md:text-5xl font-bold text-white mb-4">{t('gallery.heading')}</h2>
        <p className="text-sm text-zinc-500 max-w-2xl mb-8">{t('gallery.subtitle')}</p>

        {/* Filters */}
        <div className="flex flex-wrap gap-2 mb-12">
          {categories.map(cat => (
            <button key={cat} onClick={() => setFilter(cat)}
              className={`text-xs px-4 py-2 rounded-full border transition-all ${
                filter === cat ? 'border-[#d4a845] bg-[#d4a845]/10 text-[#d4a845]' : 'border-white/[0.08] text-zinc-500 hover:text-white'
              }`}
            >
              {cat === 'all' ? t('gallery.all') : t(`gallery.categories.${cat}`)}
            </button>
          ))}
        </div>

        {filtered.length === 0 ? (
          <p className="text-zinc-600 text-center py-20">{t('gallery.no_images')}</p>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {filtered.map((item) => (
              <motion.div
                key={item.id}
                layout
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                onClick={() => setSelected(item)}
                className="relative aspect-video rounded-xl overflow-hidden border border-white/[0.06] cursor-pointer group"
              >
                <img src={item.image_data} alt={item.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity">
                  <div className="absolute bottom-0 left-0 right-0 p-4">
                    <h3 className="text-white font-medium text-sm">{item.title}</h3>
                    {item.client_name && <p className="text-[10px] text-zinc-500">{item.client_name}</p>}
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        )}

        {/* Modal */}
        <AnimatePresence>
          {selected && (
            <motion.div
              initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
              onClick={() => setSelected(null)}
              className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4"
            >
              <motion.div
                initial={{ scale: 0.9 }} animate={{ scale: 1 }} exit={{ scale: 0.9 }}
                onClick={e => e.stopPropagation()}
                className="max-w-3xl w-full bg-zinc-900 rounded-2xl overflow-hidden border border-white/[0.06]"
              >
                <img src={selected.image_data} alt={selected.title} className="w-full aspect-video object-cover" />
                <div className="p-6">
                  <h3 className="text-lg font-semibold text-white">{selected.title}</h3>
                  {selected.description && <p className="text-sm text-zinc-500 mt-2">{selected.description}</p>}
                  {selected.client_name && <p className="text-xs text-zinc-600 mt-2">Cliente: {selected.client_name}</p>}
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  )
}
