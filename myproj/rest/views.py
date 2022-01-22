
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def post_list(request):
    post_list = []
    for post in Post.objects.all():
        post_list.append({
            "id": post.id,
            "title": post.title,
            "content": post.content,
        })
    return JsonResponse(post_list, safe=False)


def renew_post(request, pk):
    post_instance = get_object_or_404(PostForm, pk=pk)

    # POST 요청이면 폼 데이터를 처리한다.
    if request.method == "POST":
        # 폼 인스턴스를 생성하고 요청에 의한 데이타로 채운다 (binding)
        post_renew_form = PostForm(request.POST)

        if post_renew_form.is_valid():
            # form.cleaned_data 데이터를 요청받은데로 처리한다.
            #post_instance.created_at = post_renew_form.cleaned_data["renewal_date"]
            post_instance.save()

            # 새로운 URL로 보낸다.
            return HttpResponseRedirect(reverse("all-borrowed"))

    else:
        #proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        #book_renewal_form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
        pass

    context = {
        'form': PostForm(),
        "book_instance": post_instance
    }

    return render(request, "rest/post.html", context)
