from django.shortcuts import render
from urllib.parse import unquote

# Create your views here.
def home(request):
    video_data = [
        {"name": "Interstellar Docking Scene", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.EIqYEemIFVVwLIvT_5g72gHaEK%26pid%3DApi&f=1&ipt=4dfc8684ebf0f731aa16df5a2318813146e28e446fafe5a5c197f3bb94fe860a&ipo=images", "video_name": "Interstellar_Docking_Scene"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Lunch in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Breakfast in Heaven", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
        {"name": "Breakfast in Hell", "thumbnail_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VSkK-gvkjC7UgcqMsIxMNwHaHa%26pid%3DApi&f=1&ipt=44e107cf1a8b157c9cc209efad686385f7ea4c87ba88a81e389bab7670ac0f30&ipo=images", "video_name": "Shotgun Willy x Yung Craka - Breakfast in Heaven (Official Music Video) (1) (1)"},
    ]
    return render(request, 'home1.html', {'video_data': video_data})

def video_display(request, video_name):
    # video_name = unquote(video_name)
    return render(request, 'video_display.html', {'video_name': video_name})
