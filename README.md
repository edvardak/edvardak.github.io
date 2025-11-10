# Personal website

Currently under maintenance, building a home rolled static site builder.

## Building the site

Run `main.py`.

## Markdown elements supported

The following Markdown elements are supported:

- html style comments

TODO:

- titles from level 1 to 4
- `blockquotes`
- code blocks, see below for how we will render these
- math/equations -> this should be automatic using katex, but might need to do some escaping?
- some automatic section handling?

## Rendered output

Below are how some of the elements get rendered out.

### Code

We intend on rendering these using prismjs:

```html
<pre><code class="language-js">
const greet = (name) => console.log(`Hello, ${name}!`);
greet("World");
</code></pre>
```
