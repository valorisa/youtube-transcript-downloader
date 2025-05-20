from youtube_transcript_api import YouTubeTranscriptApi
import re
import os

def extract_video_id(url):
    """
    Extrait l'ID de la vidéo à partir de différentes formes d'URL YouTube.
    """
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)
    return None

def main():
    url = input("Veuillez entrer l'URL de la vidéo YouTube : ").strip()
    video_id = extract_video_id(url)
    if not video_id:
        print("Impossible d'extraire l'ID de la vidéo. Vérifiez l'URL saisie.")
        return

    try:
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        print("\nLangues de sous-titres disponibles :")
        for t in transcripts:
            print(f"- {t.language} ({t.language_code}) {'[auto]' if t.is_generated else ''}")

        lang = input("\nEntrez le code de langue souhaité (ex : fr, en, es) : ").strip()
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])

        # Création du dossier 'transcriptions' si besoin
        dossier = "transcriptions"
        os.makedirs(dossier, exist_ok=True)
        filename = f"transcription_{video_id}_{lang}.txt"
        filepath = os.path.join(dossier, filename)

        print("\nTranscription :\n")
        with open(filepath, "w", encoding="utf-8") as f:
            for segment in transcript:
                print(segment['text'])
                f.write(segment['text'] + "\n")
        print(f"\nLa transcription a aussi été enregistrée dans '{filepath}'.")

    except Exception as e:
        print(f"\nErreur lors de la récupération de la transcription :\n{e}")

if __name__ == "__main__":
    main()
