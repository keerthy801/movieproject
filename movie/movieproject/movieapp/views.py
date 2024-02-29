from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# def index(request):
#     movie = Movie.objects.all()
#     context = {
#         'movie_list': movie
#     }
#     return render(request, "index.html", context)

class MovieList(ListView):
    model=Movie
    template_name="index.html"
    context_object_name="movie_list"


# def detail(request, movie_id):
#     movie=Movie.objects.get(id=movie_id)
#     return render(request,"detail.html",{'movie':movie})

class MovieDetail(DetailView):                   #it displays a particular object retrieving from a model
    model=Movie
    template_name="detail.html"
    context_object_name="movie"


# def add_movie(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         desc=request.POST.get('desc')
#         year=request.POST.get('year')
#         img = request.FILES['img']
#         movie=Movie(name=name,desc=desc,year=year,img=img)
#         movie.save()
#         return redirect("/")
#
#     return render(request,'add.html')

class MovieAdd(CreateView):              #displays a form for adding new object and handle form submission
    model=Movie
    template_name="add.html"
    fields='__all__'
    success_url=reverse_lazy('movieapp:index')

 
# def update(request,id):
#     movie=Movie.objects.get(id=id)
#     form=MovieForm(instance=movie)
#     if(request.method=="POST"):
#         form = MovieForm(request.POST,request.FILES,instance=movie)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     return render(request,'edit.html',{'form':form})

class MovieUpdate(UpdateView):              #displays a form for adding new object and handle form submission
    model=Movie
    template_name="add.html"
    fields='__all__'
    success_url=reverse_lazy('movieapp:index')



# def delete(request,id):
#     if request.method=='POST':
#         movie=Movie.objects.get(id=id)
#         movie.delete()
#         return redirect('/')
#     return render(request,'delete.html')

class MovieDelete(DeleteView):
    model=Movie
    success_url=reverse_lazy('movieapp:index')
    template_name="delete.html"



