from django.shortcuts import redirect, render, get_object_or_404
from .models import Habit, Record
from .forms import HabitForm
from .forms import RecordForm

def home(request):
	if request.user.is_authenticated:
		return redirect('list_habits')
	return render(request, "base.html")

def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habits/list_habits.html", {"habits": habits})

def habit_detail(request,pk):
    # form = FavoriteForm()
    habit = Habit.objects.get(pk=pk)
    context = {
        'habit':habit,
        # 'form':form,
    }
    return render(request, 'habits/habit_detail.html', context)    

def new_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habits/new_habit.html", {"form": form})

def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habits/edit_habit.html", {
        "form": form,
        "habit": habit
    })


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')

    return render(request, "habits/delete_habit.html", {"habit": habit})


def records_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    return render(request, "habits/records_habit.html", {"habit": habit})

def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.habit = habit
            new_record.save()
            return redirect(to='records_habit' ,pk=pk)

    return render(request, "habits/add_record.html", {
        "form": form,
        "habit": habit
    })

# def category_habit(request, slug):
#     category = Category.objects.get(slug=slug)
#     habits = Habit.objects.filter(category=category)
#     return render(request, "habits/category.html", {'habits':habits, 'category':category})

# def add_favorite(request, pk):
#     if request.method == 'POST':
#         habit = get_object_or_404(Habit, pk=pk)
#         user = request.user
#         form = FavoriteForm(data=request.POST)
#         if form.is_valid():
#             favorite = form.save(commit=False)
#             favorite.habit = habit
#             favorite.user = user 
#             favorite.save()
#             return redirect(to='habit_detail', pk=pk)

# def favorite_habit(request):
#     favorites = Favorite.objects.filter(user=request.user)
#     return render(request, 'habits/favorite_habit.html', {'favorites': favorites})