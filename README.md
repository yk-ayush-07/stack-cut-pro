# Stack Cut Pro

Stack Cut Pro is an automated command-line toolkit designed for content creators, video editors, and streamers. It detects high-energy moments from live broadcast archives and gameplay recordings, converting horizontal streams into optimized 9:16 vertical videos suitable for YouTube Shorts, Instagram Reels, and TikTok.

## Core Features

- **Automated Stream Discovery**: Search and retrieve recent high-performing broadcasts by game category or topic.
- **Stacked Vertical Layout**: Automatically separates facecam and gameplay footage into a structured 9:16 stacked presentation.
- **Whisper Speech Recognition**: Local on-device transcription generating timed subtitles synced to speech.
- **Audio Mastering & Loudness Normalization**: Normalizes final audio delivery to industry-standard -14 LUFS for consistent loudness across mobile platforms.
- **Intelligent Highlight Selection**: Evaluates volume surges, audience reactions, and speech pacing to isolate the most engaging segments.

## Prerequisites

- Python 3.9+
- FFmpeg (for video and audio processing)
- Deno or Node.js runtime

## Quickstart

### 1. Initialize Environment
```bash
python scripts/stack_cut_pro.py setup
```

### 2. Discover Content
Scan for relevant streams matching a target topic:
```bash
python scripts/stack_cut_pro.py find --topic Valorant
```

### 3. Generate Highlight Clips
Clip highlights directly from a broadcast URL:
```bash
python scripts/stack_cut_pro.py clip <URL> --topic Valorant
```

## Configuration & Watchlist

Configure your target creators inside `watchlist.txt`:
```text
twitch:streamer_name | Valorant
youtube:@channel_handle
```

## Author & Maintainer

Created and maintained by **Ayush kumar**
- GitHub: [@yk-ayush-07](https://github.com/yk-ayush-07)

## License

Released under the permissive MIT License. See [LICENSE](LICENSE) for details.
