---
name: stack-cut-pro
description: Automated stream clipping and highlight processing skill for video editors and AI agents. Ingests long-form streams and videos, transcribes speech with local Whisper models, detects exciting moments via audio peaks and activity, and exports ready-to-publish 9:16 vertical clips with stacked layouts, dynamic subtitles, and normalized loudness.
---

# Stack Cut Pro

Stack Cut Pro automates highlight extraction and 9:16 vertical clip creation from gaming streams and online broadcasts.

## CLI Entrypoint

All operations are executed through the main driver script:
```bash
python scripts/stack_cut_pro.py <command> [options]
```

## Setup & Verification

1. **Environment Setup**:
   ```bash
   python scripts/stack_cut_pro.py setup
   ```
   Installs required dependencies into an isolated runtime (`~/.stackcutpro`), including Whisper models, OpenCV, and yt-dlp.
   Ensure system dependencies (FFmpeg and Deno/Node) are installed.

2. **Diagnostics**:
   ```bash
   python scripts/stack_cut_pro.py doctor
   ```
   Verifies Python packages, external binaries, and disk availability.

## Processing Pipeline

### 1. Stream Discovery (`find`)
Search for recent broadcasts matching a topic or check channels configured in `watchlist.txt`:
```bash
python scripts/stack_cut_pro.py find --topic "Valorant"
```

### 2. Highlight Extraction & Rendering (`clip`)
Process a stream directly from a URL:
```bash
python scripts/stack_cut_pro.py clip <URL> --topic "Valorant"
```

Options:
- `--count <N>`: Maximum number of highlight clips to generate.
- `--brain <engine>`: Intelligence provider for ranking segments (`auto`, `gemini`, `codex`, `claude`, `opencode`, or `agent`).
- `--cookies <browser>`: Authenticated session extraction for restricted video streams.

## Output Artifacts

Generated clips are organized in the workspace output directory:
- 9:16 vertical MP4 video files with stacked layout (facecam on top, gameplay underneath).
- Synchronized subtitle tracks rendered on-screen.
- `POSTING.md` containing recommended titles, captions, and hashtags.
- `clips.json` structured metadata describing timestamp offsets and highlight scores.
