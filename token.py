from github import Github, GithubIntegration
import os

private_key = os.environ['SUPER_SECRET_PEM']
print(GithubIntegration(236743, private_key).get_access_token(29073911))
