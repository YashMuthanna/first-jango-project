from django.shortcuts import render


stories = [
    "Embark on a captivating exploration of artificial intelligence, delving into its profound impact on everyday life. Uncover the marvels of cutting-edge technology shaping our future with insights that bridge the gap between innovation and understanding.",
    "Embark on a thrilling journey through awe-inspiring landscapes, a virtual tour to the most exotic destinations worldwide. Experience the essence of diverse cultures and nature's wonders, immersing yourself in the beauty of each captivating locale.",
    "Enhance your productivity with a deep dive into effective workday strategies. Unlock the secrets of successful time management and task organization, discovering tips and tricks that will elevate your efficiency and transform your professional life.",
    "Indulge your taste buds with a collection of delicious and healthy recipes. From culinary masterpieces to quick and easy meals, explore a diverse range of dishes that cater to every food enthusiast's palate, fostering a love for good food and nutrition.",
    "Step into the realm of fashion-forward trends with our style guides. Uncover the latest in fashion, from runway trends to street style. Elevate your wardrobe with tips on curating a chic and sophisticated look that mirrors your unique personality.",
    "Dive into the art of photography, from capturing fleeting moments to mastering post-processing techniques. Explore the intricacies of visual storytelling, learning how to express yourself through the lens and create compelling narratives with your photographs.",
    "Cultivate a calmer and more centered way of living through mindfulness and meditation. Embrace practices that promote mental well-being, explore meditation techniques, and foster a deeper connection with the present moment, guiding you toward a more serene lifestyle.",
    "Immerse yourself in the world of tech innovations reshaping the future. Stay abreast of cutting-edge technologies, from artificial intelligence to the Internet of Things, as we delve into the groundbreaking advancements revolutionizing our technological landscape.",
    "Embark on a literary journey with insightful book reviews, literary discussions, and compelling recommendations. Discover the beauty of literature, exploring the profound impact of words and narratives that shape our understanding of the world and human experiences.",
]
# Create your views her:
def start_page(request):
    return render(request, "blog/start.html", {
        "stories1": stories[0:3]
    })

def posts_page(request):
    return render(request, "blog/posts.html", {
        "stories": stories
    })

def post_details(request):
    pass