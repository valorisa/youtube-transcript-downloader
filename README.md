# YouTube Transcript Downloader

Un outil simple en Python pour extraire, afficher et sauvegarder les sous-titres (transcriptions) de n'importe quelle vidéo YouTube, dans la langue de votre choix.

## Fonctionnalités

- Extraction des sous-titres d'une vidéo YouTube à partir de son URL
- Affichage des langues disponibles pour la transcription
- Sélection interactive de la langue souhaitée
- Sauvegarde automatique de la transcription dans un fichier texte nommé selon l’ID de la vidéo et la langue
- Organisation des transcriptions dans un dossier dédié
- Compatible avec les sous-titres générés automatiquement ou ajoutés manuellement

## Prérequis

- Python 3.7 ou supérieur
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-utilisateur/youtube-transcript-downloader.git
   cd youtube-transcript-downloader
   ```

2. Installez la dépendance principale :
   ```
   pip install youtube-transcript-api
   ```

## Utilisation

Lancez le script principal :

```
python transcription_youtube.py
```

### Déroulement

1. **Saisissez l’URL de la vidéo YouTube** lorsque le script le demande.
2. **Choisissez la langue** parmi celles proposées (ex : `fr`, `en`, `es`).
3. **La transcription** s’affiche à l’écran et est enregistrée dans le dossier `transcriptions/` sous la forme :
   ```
   transcription_<ID_VIDEO>_<lang>.txt
   ```

### Exemple

```
Veuillez entrer l'URL de la vidéo YouTube : https://www.youtube.com/watch?v=dQw4w9WgXcQ

Langues de sous-titres disponibles :
- English (en)
- German (Germany) (de-DE)
- Japanese (ja)
- Portuguese (Brazil) (pt-BR)
- Spanish (Latin America) (es-419)

Entrez le code de langue souhaité (ex : fr, en, es) : en

Transcription :

[...]
```

## Structure du projet

```
youtube-transcript-downloader/
├── transcription_youtube.py
├── transcriptions/
│   ├── transcription_<ID_VIDEO>_<lang>.txt
│   └── ...
└── README.md
```

## Limitations

- Certains lives YouTube ou vidéos très récentes peuvent ne pas proposer immédiatement de sous-titres via l’API.
- Les vidéos sans sous-titres ou avec des restrictions d’accès ne sont pas supportées.

## Idées d’amélioration

- Export au format SRT ou VTT
- Traduction automatique de la transcription
- Interface graphique simple

## Licence

Ce projet est sous licence MIT.

---

**Auteur :** valorisa
**Contact :** valorisa

---

*Contributions et suggestions bienvenues !*

---
