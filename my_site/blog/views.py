from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "the-brittle-brothers",
        "image": "Freresbrittles.jpg",
        "author": "Django",
        "date": date(2021, 7, 21),
        "title": "Brittle Brothers",
        "excerpt": "Get rekt you bitches!!! That's what you deserve from messing with Django <- the D is silent! 😶",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam sapiente ipsum delectus minima esse blanditiis molestias magnam voluptatem numquam odio.
                      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam sapiente ipsum delectus minima esse blanditiis molestias magnam voluptatem numquam odio.
                      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam sapiente ipsum delectus minima esse blanditiis molestias magnam voluptatem numquam odio.
        """
    },
    {
        "slug": "spencer-gordon-bennet",
        "image": "SpencerGordonBennet.jpg",
        "author": "Django",
        "date": date(2022, 3, 10),
        "title": "Spencer Gordon Bennet",
        "excerpt": "Chest Shot mudafucka! ☠",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "three-unnamed-klansman",
        "image": "three-unnamed-klansman.jpg",
        "author": "Dr. King Schultz",
        "date": date(2022, 3, 10),
        "title": "Gotta Love Explosives",
        "excerpt": "Hahaha wagon goes KABOOM! 💥",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    found_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": found_post
    })
