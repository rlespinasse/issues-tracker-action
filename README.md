# Issues Tracker action

This action track state of related issues to another inside a open milestone.

## Configuration

This action need to have a [Github token (with `repo` scopes)](https://github.com/settings/tokens) setup as [secret](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets#creating-encrypted-secrets) to read and manage issues.

## Example usages

```yaml
on: issues

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: rlespinasse/issues-tracker-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GH_TOKEN }}
```

or with a specific label (like `documentation`) and a specific delimiter (like `-`):

```yaml
on: issues

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: rlespinasse/issues-tracker-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GH_TOKEN }}
          HOLDER_LABEL: "documentation"
          DELIMITER: "-"
```
