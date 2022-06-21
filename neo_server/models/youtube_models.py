from __future__ import annotations

from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class YoutubeID(BaseModel):
    """
    Model for a YouTube ID:
    -----------------------
    videoId : str videoid of the youtube video
    category : str category [video, song, artist, playlist ...]
    resultType : str result type [video, song, artist, playlist ...]
    thumbnail : Optional[List[dict]] thumbnail url / link
    """
    title: Optional[str] = None
    videoId: Optional[str] = None
    category: Optional[str] = None
    resultType: Optional[str] = None
    thumbnail: Optional[List[Dict]] = None


class TopResultSearch(BaseModel):
    """
    Model for a top result search:
    --------------------------------
    artist : Optional[List[dict]] artist of the youtube video
    duration : Optional[str] duration of the youtube video
    """
    id: Optional[YoutubeID] = None
    artist: Union[List[Dict], str] = None
    duration: Optional[str] = None


class VideoResultSearch(BaseModel):
    """
    Model for Category: video
    ----------------------------
    artist : Optional[List[dict, str]] artist of the youtube video
    """
    id: Optional[YoutubeID] = None
    artist: Union[List[Dict], str] = None


class SongresultSearch(BaseModel):
    """
    Model for Category: song
    ----------------------------
    artist : Optional[List[dict, str]] artist of the youtube video
    album : Optional[List[dict, str]] album of the youtube video
    duration : Optional[str] duration of the youtube video
    isExplicit : Optional[bool] is explicit
    """
    id: Optional[YoutubeID] = None
    duration: Optional[str] = None
    artist: Union[List[Dict], str] = None
    album: Union[List[Dict], str, Dict] = None
    isExplicit: Optional[bool] = None


class Al1bumsSearchResult(BaseModel):
    """
    Model for Category: album
    ----------------------------
    browserID : str browser id of the youtube video
    type : str album type
    artist : Optional[List[dict, str]] artist of the youtube video
    isExplicit : Optional[bool] is explicit
    """
    id: Optional[YoutubeID] = None
    browseId: Optional[str] = None
    type: Optional[str] = None
    artist: Union[List[Dict], str] = None
    isExplicit: Optional[bool] = None


class PlaylistSearchResult(BaseModel):
    """
    Model for Category: playlist
    ----------------------------
    browserID : str browser id of the youtube video
    type : str playlist type
    """
    id: Optional[YoutubeID] = None
    author: Optional[str] = None
    itemCount: Optional[int] = None
    browseId: Optional[str] = None
    type: Optional[str] = None


class ArtistsSearchResult(BaseModel):
    """
    Model for Category: artist
    ----------------------------
    browserID : str browser id of the youtube video
    artist : Optional[List[dict, str]] artist of the youtube video
    shuffle : Optional[bool] is shuffle
    radioId : Optional[str] radio id
    """

    id: Optional[YoutubeID] = None
    browseId: Optional[str] = None
    artist: Union[List[Dict], str] = None
    shuffle: Optional[str] = None
    radioID: Optional[str] = None


class YoutubeSearchItems(BaseModel):
    """
    Model for a youtube search items:
    --------------------------------
    items : Dict[str, List] list of youtube search items
    """
    items: Dict[str, List] = None
