from django.shortcuts import render
from urllib.parse import unquote

# Create your views here.
def home(request):
    video_data = [
        {"name": "Web Tech Presentation", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "WEB-TECH PROJECT PRESENTATION.mp4"},
        {"name": "Interstellar Scene", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Interstellar - Docking Scene.mp4"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
        {"name": "Breakfast in Hell", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1).mp4"},
    ]
    return render(request, 'home1.html', {'video_data': video_data})

def video_display(request, video_name):
    # video_name = unquote(video_name)
    return render(request, 'video_display.html', {'video_name': video_name})
