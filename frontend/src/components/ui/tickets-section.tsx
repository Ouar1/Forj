import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { createTicket } from '@/lib/api'
import { HoverBorderGradient } from '@/components/ui/hover-border-gradient'
import { BorderBeam } from '@/components/ui/border-beam'
import { Ticket, Send, CheckCircle } from 'lucide-react'

export function TicketSection() {
  const { t } = useTranslation()
  const [form, setForm] = useState({ name: '', email: '', subject: '', description: '', priority: 'normal' })
  const [sending, setSending] = useState(false)
  const [done, setDone] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!form.name || !form.email || !form.subject) return
    setSending(true)
    try {
      await createTicket({
        client_name: form.name, client_email: form.email,
        subject: form.subject, description: form.description, priority: form.priority,
      })
      setDone(true)
    } catch { alert('Error al crear ticket') }
    finally { setSending(false) }
  }

  return (
    <section className="py-16 md:py-32">
      <div className="mx-auto max-w-3xl px-6">
        <span className="inline-block text-[11px] tracking-[0.25em] uppercase text-zinc-600 mb-4 font-mono">
          {t('tickets.badge')}
        </span>
        <h2 className="text-3xl md:text-5xl font-bold text-white mb-4">{t('tickets.heading')}</h2>
        <p className="text-sm text-zinc-500 max-w-2xl mb-12">{t('tickets.subtitle')}</p>

        {done ? (
          <div className="relative p-8 rounded-2xl border border-green-500/30 bg-green-500/[0.03] text-center">
            <CheckCircle className="size-12 text-green-500 mx-auto mb-4" />
            <p className="text-white font-medium">{t('tickets.form.success')}</p>
          </div>
        ) : (
          <form onSubmit={submit} className="relative p-8 rounded-2xl border border-white/[0.06] bg-white/[0.02] space-y-5">
            <BorderBeam duration={8} lightColor="#d4a845" borderWidth={1} />
            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <label className="text-xs text-zinc-600 mb-1 block">{t('tickets.form.name')} *</label>
                <input type="text" value={form.name} onChange={e => setForm(p => ({ ...p, name: e.target.value }))} required
                  className="w-full bg-black/50 border border-white/[0.08] rounded-lg px-4 py-2.5 text-sm text-white focus:border-[#d4a845]/50 focus:outline-none transition-colors" />
              </div>
              <div>
                <label className="text-xs text-zinc-600 mb-1 block">{t('tickets.form.email')} *</label>
                <input type="email" value={form.email} onChange={e => setForm(p => ({ ...p, email: e.target.value }))} required
                  className="w-full bg-black/50 border border-white/[0.08] rounded-lg px-4 py-2.5 text-sm text-white focus:border-[#d4a845]/50 focus:outline-none transition-colors" />
              </div>
            </div>
            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <label className="text-xs text-zinc-600 mb-1 block">{t('tickets.form.subject')} *</label>
                <input type="text" value={form.subject} onChange={e => setForm(p => ({ ...p, subject: e.target.value }))} required
                  className="w-full bg-black/50 border border-white/[0.08] rounded-lg px-4 py-2.5 text-sm text-white focus:border-[#d4a845]/50 focus:outline-none transition-colors" />
              </div>
              <div>
                <label className="text-xs text-zinc-600 mb-1 block">{t('tickets.form.priority')}</label>
                <select value={form.priority} onChange={e => setForm(p => ({ ...p, priority: e.target.value }))}
                  className="w-full bg-black/50 border border-white/[0.08] rounded-lg px-4 py-2.5 text-sm text-white focus:border-[#d4a845]/50 focus:outline-none transition-colors">
                  <option value="baja">{t('tickets.form.priority_low')}</option>
                  <option value="normal">{t('tickets.form.priority_normal')}</option>
                  <option value="alta">{t('tickets.form.priority_high')}</option>
                  <option value="urgente">{t('tickets.form.priority_urgent')}</option>
                </select>
              </div>
            </div>
            <div>
              <label className="text-xs text-zinc-600 mb-1 block">{t('tickets.form.description')}</label>
              <textarea rows={4} value={form.description} onChange={e => setForm(p => ({ ...p, description: e.target.value }))}
                className="w-full bg-black/50 border border-white/[0.08] rounded-lg px-4 py-2.5 text-sm text-white focus:border-[#d4a845]/50 focus:outline-none transition-colors resize-none" />
            </div>
            <HoverBorderGradient as="button" type="submit" disabled={sending} className="inline-flex items-center gap-2 px-8 py-3 text-sm font-medium w-full justify-center">
              {sending ? t('common.saving') : <><Send className="size-4" /> {t('tickets.form.submit')}</>}
            </HoverBorderGradient>
          </form>
        )}
      </div>
    </section>
  )
}
