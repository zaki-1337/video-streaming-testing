from django.shortcuts import render
from urllib.parse import unquote

# Create your views here.
def home(request):
    video_data = [
        {"name": "Video 1", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_url": "gs://se-proj-8c444.appspot.com/WEB-TECH PROJECT PRESENTATION.mp4"},
        {"name": "Video 1", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_url": "https://www.youtube.com/watch?v=7nQsQ0rvYqQ"},
    ]
    return render(request, 'home1.html', {'video_data': video_data})

def video_display(request, video_url):
    video_url = unquote(video_url)
    return render(request, 'video_display.html', {'video_url': video_url})