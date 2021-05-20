from fastapi import FastAPI
from starlette.requests import Request
from models.channelDetails import ChannelDetails

from os import path
import json


app = FastAPI(title="Web-Intercept")


@app.get("/channel/name/{channel_name}", response_model=ChannelDetails)
def channel(channel_name: str, req: Request) -> ChannelDetails:
    fpath = path.join('.', 'data', f'{channel_name}.json')

    if not path.isfile(fpath):
        return ChannelDetails(name=channel_name, title="This is a test object returned by Web-Intercepter")

    return ChannelDetails.parse_file(fpath)
