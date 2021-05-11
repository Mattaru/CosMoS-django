from django.db.models import Q


def _capitalize_every_word_in_string(string: str) -> str:
    """Get a string, capitalize every word in this string and return it back."""
    ingredient_name = string.split(' ')
    new_name = []

    for word in ingredient_name:
        new_word = word.strip(' ').capitalize()
        new_name.append(new_word)

    new_name = ' '.join(new_name)

    return new_name


def get_ingredients_names_list_from_string(ingredients: str) -> list[str]:
    """Get a string, split it by ',' and make from it list of the strings,
     where every word starting at the capital letter."""
    names_list = ingredients.split(',')
    ingredients_names = []

    for name in names_list:
        new_name = _capitalize_every_word_in_string(string=name)
        ingredients_names.append(new_name)

    return ingredients_names


def make_list_from_searching_string(string: str) -> list[str]:
    """Get a string from a search form, split it by the ',' and make from it list
    of the words, then adding full string in the list like a first element."""
    data_list = string.split(' ')
    data_list.insert(0, string)

    return data_list


def get_queryset_with_filtered_data_for_search(queryset, search_list: list[str]):
    """Get a queryset of products and has filtering him by the data from the search list."""
    for data in search_list:
        qs = queryset.filter(
            Q(name__icontains=data)
            | Q(line__icontains=data)
            | Q(brand__icontains=data)
        ).order_by('name')

        return qs


def get_search_data(request) -> str:
    """Get search data from the view's request."""
    params = request.GET.dict()
    search_data = params.get('search')

    return search_data
