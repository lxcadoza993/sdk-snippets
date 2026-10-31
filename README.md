<div align="center">

# sdk-snippets

**Runnable API call snippets in curl, Python stdlib, and Node fetch — no dependencies.**

[![deps](https://img.shields.io/badge/dependencies-none-lightgrey?style=flat-square)](#quick-start)
[![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

</div>

## About

Same request, three runtimes, zero dependencies — so the example shows the
HTTP request rather than an SDK wrapper around it. Every file is a complete
script that runs as-is.

## Quick start

```bash
git clone https://github.com/lxcadoza993/sdk-snippets
cd sdk-snippets
sh curl/create.sh
```

## Configuration

| Key | Description |
| --- | --- |
| `curl/` | minimal shell examples |
| `python/` | `urllib` only |
| `js/` | Node 18+ `fetch` |
## Roadmap

- [ ] Error-path examples
- [ ] Pagination example
- [ ] Output parity assertion

## Contributing

Issues and pull requests are welcome. Please keep changes small and focused,
and add a test for any behaviour change — every repository here ships with a
runnable test suite and no third-party dependencies, so CI is just
`python3 -m unittest` / `bash test_*.sh`.

## License

[MIT](LICENSE)
