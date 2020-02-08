from github import Github
import sys
import os


def issues_tracker(token, repo_name, holder_label, delimiter):
    g = Github(token)
    repo = g.get_repo(repo_name)
    holder_labels = [repo.get_label(holder_label)]

    milestones = repo.get_milestones(state="open")
    for milestone in milestones:
        milestone_issues_tracker(repo, milestone, holder_labels, delimiter)


def milestone_issues_tracker(repo, milestone, holder_labels, delimiter):
    holders = repo.get_issues(
        milestone=milestone, state="all", labels=holder_labels)
    issues = repo.get_issues(
        milestone=milestone, state="all", sort="created", direction="asc")

    for holder in holders:
        holder_issues_tracker(milestone, holder, issues, delimiter)


def holder_issues_tracker(milestone, holder, issues, delimiter):

    text = "## Related issues\n"

    for issue in issues:
        if holder != issue and issue.title.startswith(holder.title) and delimiter in issue.title:
            split = issue.title.index(delimiter)
            title = issue.title[split + 1:].strip()
            state = "x" if issue.state == "closed" else " "
            text += "\n* [%s] #%s %s" % (state, issue.number, title)

    holder.edit(body=text)

    action = "On '%s' in '%s', set body to\n----\n%s\n----" % (
        milestone.title, holder.title, text)
    print(action)


def main():
    default_label = "enhancement"
    default_delimiter = ":"

    if len(sys.argv) > 1:

        token = sys.argv[1]
        repo_name = sys.argv[2]
        holder_label = default_label if len(sys.argv) < 4 else sys.argv[3]
        delimiter = default_delimiter if len(sys.argv) < 5 else sys.argv[4]
    else:

        token = os.environ["GITHUB_TOKEN"]
        repo_name = os.environ["GITHUB_REPOSITORY"]
        holder_label = default_label if "HOLDER_LABEL" not in os.environ else os.environ[
            "HOLDER_LABEL"]
        delimiter = default_delimiter if "DELIMITER" not in os.environ else os.environ[
            "DELIMITER"]

    issues_tracker(token, repo_name, holder_label, delimiter)


if __name__ == '__main__':
    main()
