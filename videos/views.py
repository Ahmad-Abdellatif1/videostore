from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def home(request):
    # send users to the list page
    return redirect("movie_list")

def movie_list(request):
    q = request.GET.get("q", "").strip()
    movies = Movie.objects.all().order_by("MovieTitle")
    if q:
        movies = movies.filter(MovieTitle__icontains=q)
    return render(request, "videos/movie_list.html", {"movies": movies, "q": q})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "videos/movie_detail.html", {"movie": movie})

def movie_create(request):
    form = MovieForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("movie_list")
    return render(request, "videos/movie_form.html", {"form": form, "mode": "Create"})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("movie_detail", pk=movie.pk)
    return render(request, "videos/movie_form.html", {"form": form, "mode": "Update"})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movie_list")
    return render(request, "videos/movie_confirm_delete.html", {"movie": movie})