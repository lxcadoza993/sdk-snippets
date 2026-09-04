# sdk-snippets

Short, runnable API call snippets in multiple languages. Each file does the
same thing: create an item on a demo API endpoint. No API key, no dependencies
beyond the language runtime.

## What is in here

```
curl/create.sh     — POSIX shell + curl
python/create.py   — Python 3.9+ stdlib (urllib, no requests)
js/create.js       — Node 18+ built-in fetch (no npm install)
```

## Why

I keep seeing docs with code fences labeled "Python" that are not actually
Python — they are pseudocode that looks like Python. These snippets are real
files. You can clone the repo and run any of them. If one goes stale, that is
a bug.

## How to use

```bash
# curl
./curl/create.sh

# Python
python3 python/create.py

# JavaScript (Node 18+)
node js/create.js
```

All three hit the same endpoint and send the same payload. The base URL can
be overridden with the `API_BASE` environment variable.

## When to use this

- Quickstart tutorials that need a "try it now" step before authentication.
- Workshops where participants may have any of these three runtimes.
- Sanity-checking that an API behaves the same across clients.

## License

MIT. See [LICENSE](LICENSE).
