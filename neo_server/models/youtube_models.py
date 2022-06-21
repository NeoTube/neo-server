from typing import List

from pydantic import BaseModel


class YoutubeID(BaseModel):
    """
    Youtube ID model for the Youtube API
    videoId: str - The video ID
    playListId : str - The playlist ID
    """
    videoId: str = None
    playlistID: str = None


class YoutubeSearchResult(BaseModel):
    """
    Youtube Search Result model for the Youtube API
    title: str - The title of the video
    description: str - The description of the video
    channelId: str - The channel ID
    channelTitle: str - The channel title
    """
    title: str = None
    description: str = None


class YoutubeResource(BaseModel):
    """
    Youtube Resource model for the Youtube API
    id: YoutubeID - The video ID : YoutubeID(BaseModel)
    search_result: YoutubeSearchResult - The search Result : YoutubeSearchResult(BaseModel)
    """
    id: YoutubeID = None
    search_result: YoutubeSearchResult = None


class YoutubeSearchItems(BaseModel):
    """
    Youtube Search Items model for the Youtube API
    items: List[YoutubeResource] - The list of Youtube Resources
    """
    item: List[YoutubeResource] = None
