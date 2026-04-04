from django.views.generic import TemplateView

class ContactsView(TemplateView):

    template_name = 'contacts/contacts.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
