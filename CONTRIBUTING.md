# Contributing Guidelines

> Thank you for considering contributing! This guide applies to this repository.

---

## Before you start

- Check existing issues to avoid duplicate work.
- For major changes, open an issue first to discuss what you would like to change.

## How to contribute

1. Fork the repository.
2. Create a feature branch from `main`.
3. Set up your local environment according to the subproject own README.
4. Make your changes, following the code style for that project language.
5. Write or update tests for your changes.
6. Ensure all checks pass locally.
7. Write clear, descriptive commit messages (Conventional Commits).
8. Push your branch and open a Pull Request targeting `main`.

## Code style (per language)

| Language | Format | Lint | Test |
|---|---|---|---|
| Python | black --check . | flake8 . | pytest -v |
| Go | gofmt -l . | go vet ./... | go test ./... |
| Rust | cargo fmt --check | cargo clippy | cargo test |
| JavaScript / TypeScript | npx prettier --check . | npx eslint . | npm test |

## Commit messages

Follow Conventional Commits: feat, fix, docs, chore, refactor, test.

## Pull Request checklist

- [ ] Code passes formatter/linter for its language
- [ ] Tests pass locally
- [ ] New/changed behavior has test coverage
- [ ] Documentation updated
- [ ] Commit messages follow Conventional Commits
- [ ] PR scoped and focused

## Reporting bugs / security issues

- Regular bugs: open a GitHub issue.
- Security vulnerabilities: do NOT open a public issue. See SECURITY.md.

We appreciate your effort.