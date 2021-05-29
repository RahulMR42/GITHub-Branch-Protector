import os
import json
import requests

class git_repo():
    def __init__(self):
        self.git_user="RahulMR42" #os.enviorn["git_user"]
        self.git_pat="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" #os.environ["git_pat"]
        self.branch_to_protect="main"
        self.branch_protection_rules=branch_protection = {
                "required_status_checks": {"strict": True, "contexts": ["default"]},
                "enforce_admins": False,
                "required_pull_request_reviews": {
                    "dismissal_restrictions": {
                              "users": ['user1'],
                              "teams": ['myteam1']
                                },
                       "dismiss_stale_reviews": True,
                       "require_code_owner_reviews": True,
                       #"required_approving_review_count": 2
                },
                "restrictions": None,
            }
        self.issue_body = {
                            "title": f'[Branch-{self.branch_to_protect}] - Added protection rules',
                            "body": f'@{self.git_user}:An automated protection added for branch {self.branch_to_protect}'
                           }
        self.session = requests.session()
        self.session.auth = (self.git_user,self.git_pat)
        self.session.headers.update({"Accept": "application/vnd.github.v3+json"})

    def protect_branch(self,payload):
        try:
            repo_url=payload['repository']['url']
            protect_branch_url=f'{repo_url}/branches/{self.branch_to_protect}/protection'
            create_issue_url=f'{repo_url}/issues'
            response = self.session.put(protect_branch_url,json.dumps(self.branch_protection_rules),headers={"Accept": "application/vnd.github.nebula-preview+json"})
            print(response.text,response.status_code)
            a=self.session.get(protect_branch_url)
            print(a.text)
            if response.status_code != 200:
                return {"status":"invalid","details":response.json()}
            response = self.session.post(create_issue_url,json.dumps(self.issue_body))
            self.session.close()
            if response.status_code != 200:
                return {"status":"invalid","details":response.json()}
            self.session.close()
            print(response.text,response.status_code)
                     
            return {"status":"created"}
        except Exception as error:
            print(error)
            return {"status":"error","Details":str(error)}