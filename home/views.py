from django.shortcuts import render, redirect
from django.views import View
from .models import ContactMessage
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import BlogPostCommentForm
from .models import About, Hobby, Comment, Education, Experience, Skill, Work, Category, BlogPost, BlogPostComment


class AboutView(View):
    def get(self, request):
        about = About.objects.first()
        hobbies = Hobby.objects.all()
        comments = Comment.objects.all()
        return render(request, 'home/about.html', {'about': about, 'hobbies': hobbies, 'comments': comments})


class ResumeView(View):
    def get(self, request):
        about = About.objects.first()
        educations = Education.objects.all()
        experiences = Experience.objects.all()
        skills = Skill.objects.all()
        return render(request, 'home/resume.html',
                      {'about': about, 'educations': educations, 'experiences': experiences, 'skills': skills, })


class WorksView(View):
    def get(self, request):
        about = About.objects.first()
        works = Work.objects.all()
        categories = Category.objects.all()
        return render(request, 'home/works.html', {'about': about, 'works': works, 'categories': categories, })


class BlogView(View):
    def get(self, request):
        about = About.objects.first()
        posts = BlogPost.objects.all()
        return render(request, 'home/blog.html', {'about': about, 'posts': posts})


class ContactView(View):
    def get(self, request):
        about = About.objects.first()
        return render(request, 'home/contact.html', {'about': about})


class SinglePostView(DetailView):
    model = BlogPost
    template_name = 'home/single-post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.filter(parent__isnull=True).order_by('-created')
        form = BlogPostCommentForm()
        context['comments'] = comments
        context['form'] = form
        context['about'] = About.objects.first()

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        self.object = self.get_object()
        form = BlogPostCommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blogpost = self.object

            parent_id = request.POST.get('parent')
            if parent_id:
                try:
                    parent_comment = BlogPostComment.objects.get(id=parent_id)
                    comment.parent = parent_comment
                except BlogPostComment.DoesNotExist:
                    comment.parent = None

            comment.save()
            return redirect(reverse('home:single-post', kwargs={'pk': self.object.pk}))
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


@login_required
@require_POST
def comment_like(request, comment_id):
    comment = get_object_or_404(BlogPostComment, pk=comment_id)
    user = request.user

    if user in comment.likes.all():
        comment.likes.remove(user)
        liked = False
    else:
        comment.likes.add(user)
        liked = True

    return JsonResponse({'liked': liked, 'total_likes': comment.total_likes})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPostComment
    template_name = 'inc/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('home:single-post', kwargs={'pk': self.object.blogpost.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        print("Comment to delete:", obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context
