# src/comments.py
# Author: Nabil Orya
# Purpose: Fetch comments and commenter metadata from YouTube videos
# Requirements: google-api-python-client

def fetch_comments(youtube, video_id, max_pages=5):
    """
    Fetch top-level comments from a YouTube video along with author info.

    Parameters:
    - youtube : YouTube API client object
    - video_id : str, YouTube video ID
    - max_pages : int, how many pages of 100 comments to fetch

    Returns:
    - List of dicts: each dict contains comment info
    """
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,      # maximum allowed per page
        textFormat="plainText"
    )

    page = 0
    while request and page < max_pages:
        response = request.execute()
        for item in response["items"]:
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "video_id": video_id,
                "comment_id": item["id"],
                "author": snippet.get("authorDisplayName"),
                "author_channel_id": snippet.get("authorChannelId", {}).get("value"),
                "comment_text": snippet.get("textDisplay"),
                "like_count": snippet.get("likeCount"),
                "published_at": snippet.get("publishedAt")
            })
        # Get next page
        request = youtube.commentThreads().list_next(request, response)
        page += 1

    return comments
