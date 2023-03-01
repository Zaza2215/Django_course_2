from .models import *


class DataMixin:
    paginate_by = 1

    def get_user_context(self, **kwargs):
        context = kwargs
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
