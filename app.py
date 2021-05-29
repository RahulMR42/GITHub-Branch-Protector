import json
from fastapi import FastAPI,Request,Response,status
from resources.repo_event_handler import git_repo

app = FastAPI()


@app.post("/repoevent")
async def git_Repo_webhook_listner(values: Request,response:Response):
    payload = await values.json()
    try:
         if payload['action'] == "created":
             repo= git_repo()
             output = repo.protect_branch(payload)
             if output['status'] == "ok":
                 response.status_code = 201
             elif output['status'] == "invalid":
                 response.status_code = 403
             else:
                 response.status_code = 500
             print(output)
             return output
             
         else:
             response.status_code = 403
             return {"message":"Invalid request","Details":"Out of context,enabled for repo create events only"}
    
    except Exception as error:
        response.status_code = 500
        print(error)
        return {"message":"Errored request","Details":"Out of context,enabled for repo create events only"}

   
    