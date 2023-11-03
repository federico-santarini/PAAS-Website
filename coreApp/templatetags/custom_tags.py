from django import template

register = template.Library()

@register.inclusion_tag('CTA-completa-community.html')
def CTA_completa_community():
    return {}

@register.inclusion_tag('CTA-rapida-articoli.html')
def CTA_rapida_articoli():
    return {}

@register.inclusion_tag('CTA-rapida-contattaci.html')
def CTA_rapida_contattaci():
    return {}

@register.inclusion_tag('CTA-rapida-licenza.html')
def CTA_rapida_licenza():
    return {}