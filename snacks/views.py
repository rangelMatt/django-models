from django.views.generic import ListView
from .models import Snack

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack