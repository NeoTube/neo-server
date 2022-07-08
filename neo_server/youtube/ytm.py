#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: ytm.py

from collections import defaultdict
from typing import Dict, List

from neo_server import constants
from neo_server.log import get_logger
# yapf no format
# yapf: disable
from neo_server.models.youtube_models import (
    Al1bumsSearchResult, ArtistsSearchResult, PlaylistSearchResult, SongresultSearch, TopResultSearch,
    VideoResultSearch, YoutubeID, YoutubeSearchItems
)
# yapf: enable
from neo_server.utils.debug_tools import write_to_file
from neo_server.utils.ytm_header_utils import setup

log = get_logger(__name__)


def enforce() -> str:
    """
    Enforce the youtube search model.
    """

    def decorator(func: callable) -> callable:
        """decorator for youtube search model.

        Parameters
        ----------
        func : callable
            function to be decorated with youtube search model.

        Returns
        -------
        callable
            decorated function.
        """

        def wrapper(*args, **kwargs) -> callable:
            """
            wrapper for youtube search modelse.
            """

            filter_list = [
                "albums", "artists", "playlists", "community_playlists", "featured_playlists", "songs", "videos"
            ]

            scope_list = ["library", "uploads", "", None]
            current_filter = kwargs.get("filter", "")
            current_scope = kwargs.get("scope", "")
            if current_filter in filter_list and current_scope in scope_list:
                return func(*args, **kwargs)
            else:
                log.warn(current_filter)
                log.warn(current_scope)
                log.exception(f"{current_filter} is not a valid filter or {current_scope} is not a valid scope ")

        return wrapper

    return decorator


class YtmCommands:

    def __init__(self):
        self.ytmusic = setup()
        self.switch = {
            "Top result": TopResultSearch,
            "Videos": VideoResultSearch,
            "Songs": SongresultSearch,
            "Albums": Al1bumsSearchResult,
            "Artists": ArtistsSearchResult,
            "Playlists": PlaylistSearchResult,
            "Community playlists": PlaylistSearchResult
        }

    def create_identifier(self, video: List[Dict]) -> YoutubeID:
        """Create identifier for youtube search result.

        Parameters
        ----------
        video : List[Dict]
            video: List of valid Dictionaries - this function creates identifier for the video

        Returns
        -------
        YoutubeID
            BaseModel Instance: YoutubeID

        """
        video_id = YoutubeID(
            title=video.get("title"),
            videoId=video.get("videoId"),
            category=video.get("category"),
            resultType=video.get("resultType"),
            thumbnail=video.get("thumbnails"))
        return video_id

    @enforce()
    def search(
            self,
            search_query: str = "Never going to give you up",
            filter: str = None,
            scope: str = None,
            max_results: int = 10,
            ignore_spelling: bool = False) -> YoutubeSearchItems:
        """Search:


        Parameters
        ----------
        search_query : str
            search query : search basis for youtube
        filter : str
            Filter : of following types:
            "Top result", "Videos", "Songs", "Albums", "Artists", "Playlists", "Community playlists"
        scope : str
            Scope - how is it created : of the following types:
            "uploads", "library"
        max_results : int
            amount of results returned
        ignore_spelling : bool
            Spelling / case sensitive

        Returns
        -------
        YoutubeSearchItems
            BaseModel Instance YouTubeSearchItems

        """
        dict_container = defaultdict(list)
        if search_query is None or search_query == "":
            log.error("Search query is None")
        search_result = self.ytmusic.search(
            query=search_query, filter=filter, scope=scope, limit=max_results, ignore_spelling=ignore_spelling)
        if search_result is not None and len(search_result) > 0:

            for count, video in enumerate(search_result):
                if count == max_results:
                    break

                video_id = self.create_identifier(video)
                if video_id.category in self.switch:
                    dict_container[video_id.category].append(self.switch[video_id.category](id=video_id, **video))
        if constants.DEBUG:
            write_to_file(dict_container, "ytm_playlist")

        return YoutubeSearchItems(items=dict_container)
