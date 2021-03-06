from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
	# get all posts from db. we have load into the tempate, we have to use a query
	# ORM is Querysets.[ used model instead of table ]
	#posts = Post.objects.all() # all posts objects in the db
	#posts = Post.objects.filter(published__date
	#return render(request,'blog\post_list.html',{'posts':posts})
	return render(request, 'blog\post_list.html',{})


def post_details(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog\post_details.html',{'post':post})
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return render(request,'blog\post_details.html',{'post':post})
	else:
		form = PostForm()
		return render(request,'blog\post_edit.html',{'form':form})