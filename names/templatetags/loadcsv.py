import csv
from django import template
from names.models import card
register = template.Library()

@register.filter
def loadcsv(arg):
    csvfile = arg
    with open(csvfile, 'rb') as csv1:
        cardreader = csv.reader(csv1, delimiter=',')
        card.objects.bulk_create([card(first_name=row[0], last_name=row[1]) for row in cardreader])