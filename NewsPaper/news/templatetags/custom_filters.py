from django import template


register = template.Library()

TABOO_WORDS = {
   'редиска': '*******',
   'Шок': '***'
}

@register.filter()
def currency(value, word = 'Шок'):
   """
   value: значение, к которому нужно применить фильтр
   word: запретные слова
   """
   postfix = TABOO_WORDS[word]
   return f'{value} {postfix}'