from django import template

register = template.Library()


@register.filter
def map_filter(value):
    # print(value)
    maps = []
    for map in value:
        if(map.admin_permission == True):
            maps.append(map)
    return len(maps)


@register.filter
def replace_with_space(value):
    return value.replace("-", " ")
