animal_names = ['Mickey Mouse', 'Donald Duck', 'Gladstone Gander', 'Scrooge McDuck']

duck_names = [animal_names[i] for i in [1, 3]]

filtered_names = filter(
    lambda x: 'Duck' in x,
    animal_names
)


duck_names_again = []
# filters allow the use of `enumerate` (unlike generators)
for i, name in enumerate(filtered_names):
    assert name == duck_names[i]
    duck_names_again.append(name)
assert duck_names_again == duck_names


# filters can not be used for a second time (like generators)
assert list(filtered_names) == []
