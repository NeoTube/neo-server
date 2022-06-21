#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: ytm.py

from typing import List

from neo_server.log import get_logger
from neo_server.models.youtube_models import YoutubeID, YoutubeResource, YoutubeSearchItems, YoutubeSearchResult
from neo_server.utils.ytm_header_utils import setup

log = get_logger(__name__)


class YtmCommands:

    def __init__(self):
        self.ytmusic = setup()

    def validator(self, item: List[dict]) -> bool:
        video_id = YoutubeID(videoId=item.get("videoId"))

        video_search = YoutubeSearchResult(title=item.get("title"), description=item.get("description"),)
        return YoutubeResource(id=video_id, search_result=video_search)

    #  TODO(vsedov) (23:42:03 - 20/06/22): Improve this code
    def search(self, search_query: str = None, max_results: int = 10) -> YoutubeSearchItems:
        container = []
        if search_query is None or search_query == "":
            log.error("Search query is None")
        search_result = self.ytmusic.search(query=search_query, limit=max_results, filter=None)
        if search_result is not None and len(search_result) > 0:

            for i, item in enumerate(search_result):
                if i == max_results:
                    break
                container.append(self.validator(item))
            return YoutubeSearchItems(items=container)
        else:
            log.info("Nothing was found")
            return YoutubeSearchItems(items=[])
