from model.items.item import Item
from model.objects.armors import find_any_armor_by_name
from model.objects.objects import find_any_item_by_name


def find_any_item(name: str) -> Item:
    obj = find_any_item_by_name(name)
    
    if obj is not None:
        return obj
    
    return find_any_armor_by_name(name)
