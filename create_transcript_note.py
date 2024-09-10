import os
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build


def get_video_title(video_id: str) -> str:
    api_key = os.environ.get('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    
    if 'items' in response and len(response['items']) > 0:
        return response['items'][0]['snippet']['title']
    return "Untitled Video"


def get_youtube_transcript(video_id: str) -> str | None:
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        
        # Combine all text entries
        full_transcript = ' '.join([entry['text'] for entry in transcript])
        
        return full_transcript
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def create_markdown_file(video_title: str, transcript: str):
    # Remove any characters that are not allowed in filenames
    safe_title = ''.join(c for c in video_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    filename = f"{safe_title}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {video_title}\n\n")
        f.write("## Transcript\n\n")
        f.write(transcript)
    
    print(f"Markdown file '{filename}' has been created.")


def main():
    video_id = "5gfNUVmX3Es"
    
    video_title = get_video_title(video_id)
    transcript_text = get_youtube_transcript(video_id)

    if transcript_text is None:
        print("Failed to retrieve transcript.")
        return

    create_markdown_file(video_title, transcript_text)
    print("Transcript:")
    print(transcript_text)


if __name__ == "__main__":
    main()
