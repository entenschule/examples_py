# generator expressions

https://peps.python.org/pep-0289/

`spam` and `eggs` both return the sum of squares `i**2` for i <= n.<br>
`spam` takes the sum of a list, while `eggs` uses a generator expression.<br>
`eggs` may save memory, but takes slightly longer.