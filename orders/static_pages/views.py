from django.views.generic import TemplateView


class AboutProjectView(TemplateView):
    template_name = 'static_pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О проекте'
        context['main_text'] = ('Данный проект помогает работникам общепита эффективно управлять заказами.')

        return context
