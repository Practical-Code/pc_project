from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from webapp.forms import WebAppForm
from webapp.models import Post

class WebAppView(TemplateView):
    template_name = 'webapp/webapp.html'

    def get(self, request):
        form = WebAppForm()
        posts = Post.objects.all()

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = WebAppForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = WebAppForm()

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)