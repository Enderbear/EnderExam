from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm  # 假设你已经创建了一个表单类

# Create your views here.
def exam(request):
    return render(request, 'exam.html')

def data(request):
    return render(request, 'data.html')

def upload(request):
    return render(request, 'upload.html')

def upload_topic(request):
    return render(request, 'upload_topic.html')

def upload_topic_success(request):
    return render(request, 'upload_topic_success.html')

def upload_topic_failed(request):
    return render(request, 'upload_topic_failed.html')

def upload_question(request):
    return render(request, 'upload_question.html')

def upload_topic_func(request):
    if request.method == 'POST':
        print("request.method == 'POST'")
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_topic_success')  # 替换为成功页面的URL
    else:
        print("request.method != 'POST'")
        form = TopicForm()
    return render(request, 'upload_topic_failed', {'form': form})

def view_topic(request):
    topics = Topic.objects.all()
    return render(request, 'view_topic.html', {'topics': topics})