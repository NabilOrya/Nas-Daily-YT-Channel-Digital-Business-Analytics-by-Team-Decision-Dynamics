from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def get_transcript(video_id, languages=["en"]):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=languages
        )
        return " ".join([item["text"] for item in transcript])

    except (TranscriptsDisabled, NoTranscriptFound):
        return None
