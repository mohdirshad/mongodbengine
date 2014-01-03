# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Post
from blog.forms import *



def create_post(request):
	template_name="create_post.html"
	ci=RequestContext(request)
	form=Post_form()
	if request.method=='POST':
		form=Post_form(request.POST)
		if form.is_valid():
				title = form.cleaned_data['title']
				text =form.cleaned_data['text'] 
				tags =form.cleaned_data['tags']
				comment = form.cleaned_data['comment']
				post=Post.objects.create(title=title , text = text ,tags = tags , )

				return HttpResponseRedirect('/blog/')
		else:
			return render_to_response(template_name ,{'form':form} )
	else:
		return render_to_response(template_name,{'form':form} ,ci)

def create_comment(request ,id):
	template_name="create_comment.html"
	ci=RequestContext(request)
	form=Comment_form()
	post=Post.objects.get(id = id)
	if request.method=='POST':
		form=Comment_form(request.POST)
		if form.is_valid():
				comment = form.cleaned_data['comment']
				post.comments.extend([comment])
				post.save()

				return HttpResponseRedirect('/blog/')
		else:
			return render_to_response(template_name ,{'form':form} )
	else:
		return render_to_response(template_name,{'form':form , 'post':post} ,ci)



def post_view(request):
	template_name="post.html"
	post=Post.objects.all().order_by('-id')
	return render_to_response(template_name,{'post':post},)


def detail(request , id ):
	template_name='detail.html'
	post=Post.objects.get(id = id)
	return render_to_response(template_name , {'post':post})
