from typing import List, Optional
import requests
import re

def get_repo_stars(repo_owner=None, repo_name=None, repo_url=None)->Optional[List[int]]:
    repo_url = get_repo_url(repo_owner, repo_name, repo_url)
    response = requests.get(repo_url)

    if response.status_code == 200:
        html_content = response.text
        pattern = r'<[^>]+id="repo-stars-counter-star"[^>]*>(.*?)</[^>]+>' 
        matches = re.findall(pattern, html_content, re.DOTALL)
        # print(matches)
        return matches
    else:
        return None


def get_repo_forks(repo_owner=None, repo_name=None, repo_url=None)->Optional[List[int]]:
    repo_url = get_repo_url(repo_owner, repo_name, repo_url)
    response = requests.get(repo_url)

    if response.status_code == 200:
        html_content = response.text
        pattern = r'<[^>]+id="repo-network-counter"[^>]*>(.*?)</[^>]+>' 
        matches = re.findall(pattern, html_content, re.DOTALL)
        # print(matches)
        return matches
    else:
        return None


def get_repo_watchers(repo_owner=None, repo_name=None, repo_url=None)->Optional[List[int]]:
    repo_url = get_repo_url(repo_owner, repo_name, repo_url)
    response = requests.get(repo_url)

    if response.status_code == 200:
        html_content = response.text
        pattern = r'<[^>]+id="repo-notifications-counter"[^>]*>(.*?)</[^>]+>'
        matches = re.findall(pattern, html_content, re.DOTALL)
        # print(matches)
        if matches:
            return matches # 未登录状态下是看不到的，需要Cookies
        else:
            return None
    else:
        return None




def get_repo_url(repo_owner=None, repo_name=None, repo_url=None, repo_host="github.com"):
    # 如果repo_owner和repo_name均不为空，则构建repo_url
    if repo_owner and repo_name:
        if repo_host=="github.com":
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

def test_get_repo_stars():
    # case construct
    print(get_repo_stars(repo_owner="uni-gal", repo_name="ayaka"))
    # case specific
    # print(get_repo_stars(repo_url="https://github.com/uni-gal/ayaka"))

def test_get_repo_watchers():
    # 测试用例构造
    print(get_repo_watchers(repo_owner="uni-gal", repo_name="ayaka"))
    # 特定URL测试用例
    # print(get_repo_watchers(repo_url="https://github.com/uni-gal/ayaka"))

def test_get_repo_forks():
    # 测试用例构造
    print(get_repo_forks(repo_owner="uni-gal", repo_name="ayaka"))
    # 特定URL测试用例
    # print(get_repo_forks(repo_url="https://github.com/uni-gal/ayaka"))


if __name__ == "__main__":
    test_get_repo_stars()
    test_get_repo_watchers()
    test_get_repo_forks()