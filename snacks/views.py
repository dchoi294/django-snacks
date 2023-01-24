from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Bugles_brand_snack_food.jpg/1200px-Bugles_brand_snack_food.jpg",
                "title": "Bugles",
                "description": "a very simple brass instrument looking like chips.",
                "reference_url": "https://en.wikipedia.org/wiki/Bugles_(snack)"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Bamba_snack.jpg/800px-Bamba_snack.jpg",
                "title": "Bamba",
                "description": "a snack made of peanut-butter-flavored puffed maize manufactured by the Osem corporation in Kiryat Gat, Israel.",
                "reference_url": "https://en.wikipedia.org/wiki/Bamba_%28snack%29"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Chex-Mix-Pile.jpg",
                "title": "Snack Mix",
                "description": "a subset of snack foods consisting of multiple snack items.",
                "reference_url": "https://en.wikipedia.org/wiki/Snack_mix"
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'
