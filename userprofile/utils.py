from django.shortcuts import render, redirect
from django.core.paginator import Paginator


class ListMixin:
    model = None
    template = None

    def get(self, request, id=None):
        name = self.model.__name__.lower()
        if name == 'friends':
            list = self.model.objects.filter(user_id=request.user.id)
        elif name == 'userphoto':
            list = self.model.objects.filter(user_id=id)
            name = "list_photo"
        else:
            list = self.model.objects.all()
        paginator = Paginator(list, 10)
        page = request.GET.get('page')
        list = paginator.get_page(page)
        return render(request, self.template, context={name: list})


class CreateObjectMixin:
    form = None
    template = None
    model = None
    template_alt = None

    def get(self, request):
        return render(request, self.template, context={"form": self.form()})

    def post(self, request):
        owner = self.model(owner=request.user)
        form = self.form(request.POST, request.FILES, instance=owner)
        if form.is_valid:
            form.save()
            return redirect(self.template_alt)
        return render(request, self.template, context={"form": form})


class UpdateObjectMixin:
    form = None
    template = None
    model = None

    def get(self, request, id=None):
        obj = self.model.objects.get(pk=id)
        bound_form = self.form(instance=obj)
        return render(request, self.template, context={
                                            "form": bound_form,
                                            "obj": obj
        })

    def post(self, request, id=None):
        obj = self.model.objects.get(pk=id)
        bound_form = self.form(request.POST, request.FILES, instance=obj)
        if bound_form.is_valid():
            bound_form.save()
            return redirect("redirect_user")
        return render(request, self.template, context={
                                            "form": bound_form,
                                            "obj": obj
        })


class CreateCommentObjectMixin:
    form = None
    template = None
    model = None
    model_alt = None
    template_alt = None

    def get(self, request, id):
        post = self.model.objects.get(pk=id)
        comments = self.model_alt.objects.filter(post_id=post.id)
        return render(request, self.template, context={
                                                "post": post,
                                                "comments": comments,
                                                "form": self.form()
            })

    def post(self, request, id):
        post = self.model.objects.get(pk=id)
        owner = self.model_alt(post=post, owner=request.user)
        comments = self.model_alt.objects.filter(post_id=post.id)
        form = self.form(request.POST, instance=owner)
        if form.is_valid:
            form.save()
            return redirect(self.template_alt, id=post.id)
        return render(request, self.template, context={
                                                "post": post,
                                                "comments": comments,
                                                "form": form
        })
