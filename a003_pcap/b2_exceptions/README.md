# exceptions


## discard exceptions in `finally`

If the `finally` clause executes a `return`, `break` or `continue` statement, the saved exception is discarded:

* [c01](c01_try_except_finally_return): `finally` (after `except`) with `return`
* [c02](c02_try_finally_continue): `finally` (without `except`) with `continue` (or `break`)
* [c10](c10_try_finally): `return` in `finally` is stronger than `return` in `try`
* [c11](c11_try_except_finally): `finally` without `return` for comparison


## arguments

* [c03](c03_super_arg), [c05](c05_super): calling `__init__()` of parent class sets args of parent and self
* [c04](c04_args): multiple arguments are printed as tuple (but not a single one)
