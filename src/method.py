import requests


def get_repo_metadata(repo_owner=None, repo_name=None, repo_url=None):
    # 如果repo_owner和repo_name均不为空，则构建repo_url
    if repo_owner and repo_name:
        repo_url = "https://github.com/" + f"{repo_owner}/{repo_name}"
    else:
        repo_url = repo_url
    return repo_url


def get_colour(colour_name: str) -> str:
    palette = {
        "Python": "#3572A5",
        "HTML": "#E34C26",
        "C#": "#178600",
        "Java": "#B07219",
        "JavaScript": "#F1E05A",
        "Go": "#00ADD8",
        "TypeScript": "#3178C6",
        "Rust": "#DEA584",
    }
    return palette[colour_name]
