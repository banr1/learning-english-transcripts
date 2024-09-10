from youtube_transcript_api import YouTubeTranscriptApi


def get_youtube_transcript(video_id):
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        
        # Combine all text entries
        full_transcript = ' '.join([entry['text'] for entry in transcript])
        
        return full_transcript
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def main():
    # Example usage
    video_id = "5gfNUVmX3Es"  # Replace with the actual YouTube video ID
    transcript_text = get_youtube_transcript(video_id)

    if transcript_text:
        print(transcript_text)
    else:
        print("Failed to retrieve transcript.")


if __name__ == "__main__":
    main()
