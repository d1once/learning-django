from django.shortcuts import get_object_or_404, render
from .models import Bounty

# Create your views here.


def index(request):
    bounties = Bounty.objects.all()
    return render(request, "bounty_outlet/index.html", {
        "all_bounties": bounties,
    })


def bounty_details(request, slug):
    bounty = get_object_or_404(Bounty, slug=slug)
    return render(request, "bounty_outlet/bounty_detail.html", {
        "name": bounty.name,
        "benefactor": bounty.benefactor,
        "reward": bounty.reward,
        "deadoralive": bounty.deadoralive
    })
