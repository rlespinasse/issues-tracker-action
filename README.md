# Issues Tracker action

This action track state of related issues to another inside a open milestone.

## How to

If the repository have a labeled issue with multiples sub-issues related in a milestone, this action will automatically keep up-to-date a list of the sub-issues and its states.

### Configuration

This action need to have a [Github token (with `repo` scopes)](https://github.com/settings/tokens) setup as [secret](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets#creating-encrypted-secrets) to read and manage issues.

The label, used on a issue to track the sub-issues, is by default set to `enhancement` (can be override).

The delimiter, used on sub-issues to be tracked, is by default set to `:` (can be override).

### Example

In a milestone `Some Milestone`, imagine a `Some Big Feature` issue, the sub-issues will have the issue title as prefix.

So in a milestone `Some Milestone`, if the following issues are present:

* `Some Big Feature : action 1` (with id `#41`)
* `Some Big Feature : action 2` (with id `#42`)
* `Some Big Feature : action 3` (with id `#43`)

The body of the `Some Big Feature` issue will be:

```markdown
## Related issues

* [ ] #41 action 1
* [ ] #42 action 2
* [ ] #43 action 3
```

But if you close some issue like`Some Big Feature : action 2`, the body of the `Some Big Feature` issue will become:

```markdown
## Related issues

* [ ] #41 action 1
* [x] #42 action 2
* [ ] #43 action 3
```

And so on.

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
