def slug_gen():
    slug = 'John'
    yield slug

    slug += 'Doe'
    yield slug

    slug += '89'
    yield slug


for slug in slug_gen():
    print(slug)


"""
John
JohnDoe
JohnDoe89
"""
