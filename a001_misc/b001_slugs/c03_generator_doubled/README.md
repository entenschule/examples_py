# fun3

This is my improvement of the [last version](../c02_generator).<br>
(And the [next version](../c04_combine) is my attempt to improve this one.)

The crucial feature in the last version was the return of a generator by `find_duplicates`.

But it is not efficient, to check all slugs for duplicates.<br>
Instead, the function should refine the duplicates from the last step.

That requires using the generator twice:
* as `dup_gen_to_append` to append the slugs in the for-loop
* as `dup_gen_to_refine` in the next call of `find_duplicates`

As generators can only be used once, it is doubled with `itertools.tee`.