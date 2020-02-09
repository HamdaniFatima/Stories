import django_filters
from stories.models import Cases

class CasesFilter (django_filters.FilterSet):
    class Meta:
        model = Cases
        fields = ['title_case', 'mois', 'subject', 'processus' ]