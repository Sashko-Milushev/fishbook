from fishbook.fish.models import Fish


def get_fish_by_id(pk):
    fish = Fish.objects.filter(pk=pk).get()
    return fish
