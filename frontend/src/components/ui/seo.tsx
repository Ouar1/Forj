import { Helmet } from "react-helmet-async"
import { useTranslation } from 'react-i18next'

interface SEOProps {
  title?: string
  description?: string
  image?: string
}

const SITE = "https://forj.es"

const jsonLd = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": `${SITE}/#organization`,
      name: "Forj",
      url: SITE,
      logo: `${SITE}/logo.png`,
      description: "Infraestructura TI Profesional",
      email: "contacto@forj.es",
      foundingDate: "2024",
    },
    {
      "@type": "WebSite",
      "@id": `${SITE}/#website`,
      url: SITE,
      name: "Forj · Infraestructura TI Profesional",
      publisher: { "@id": `${SITE}/#organization` },
      inLanguage: "es",
    },
    {
      "@type": "LocalBusiness",
      "@id": `${SITE}/#localbusiness`,
      name: "Forj",
      description: "Infraestructura TI Profesional",
      url: SITE,
      email: "contacto@forj.es",
      areaServed: "ES",
      priceRange: "€€",
    },
  ],
}

export function SEO({ title, description, image }: SEOProps) {
  const { t } = useTranslation()
  const defaultTitle = t('seo.default_title')
  const defaultDescription = t('seo.default_description')
  const fullTitle = title ? `${title} · Forj` : defaultTitle
  const desc = description || defaultDescription

  return (
    <Helmet>
      <title>{fullTitle}</title>
      <meta name="description" content={desc} />
      <meta property="og:title" content={fullTitle} />
      <meta property="og:description" content={desc} />
      <meta property="og:url" content={SITE} />
      <meta property="og:type" content="website" />
      <meta property="og:locale" content="es_ES" />
      <meta property="og:site_name" content="Forj" />
      <meta name="twitter:card" content="summary_large_image" />
      {image && <meta property="og:image" content={image} />}
      {image && <meta name="twitter:image" content={image} />}
      <script type="application/ld+json">{JSON.stringify(jsonLd)}</script>
    </Helmet>
  )
}
