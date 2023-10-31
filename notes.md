# Notes

## Calculators

I tried out a number of calculators, and many of them didn't really work out.

### Qalculate!

https://qalculate.github.io/

Convenient syntax, allows you to use easily use degrees for trigonometric
computations even though radians is the default. Literal matrix syntax is handy
and arithmetic operators largely work as you expect on vectors and matrices.
However, it's cumbersome to define and use custom functions.

### Ivy

https://github.com/robpike/ivy

It has a nice APL-ish syntax and arbitrary-precision numbers but there's no
literal syntax for defining matrices.

### Calcpy

https://github.com/idanpa/calcpy

It has that familiar Python syntax, but that also means the literal syntax for
matrices is cumbersome, and arithmetic operators don't work nicely.

## Scripts

Find the total number of topics on a Math Academy course page:

```javascript
[...document.querySelectorAll('.unitNumTopics')].reduce((acc, node) => acc + parseInt(node.innerText), 0)
```
