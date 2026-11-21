# Changelog

All notable changes to **Stack Cut Pro** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-21

### Added
- **Audio-First Highlight Detection**: Downloads only stream audio to analyze speech patterns and volume surges before video processing.
- **Stacked Vertical Studio (9:16)**: Places streamer facecam on top (35%) and gameplay on bottom (65%).
- **Multi-Layout Modes**: Added support for Stacked, Dynamic Face Follow (YuNet OpenCV tracking), and Cinematic Fit & Blur.
- **Word-by-Word Synced Captions**: On-device Whisper transcription with animated active word highlight styling.
- **Broadcast Audio Normalization**: Automatic mastering to EBU R128 standard (-14 LUFS).
- **Automated Stream Discovery**: Query live YouTube broadcasts and Twitch/Kick watchlist channels.
- **Metadata Generator**: Automatic `POSTING.md` production with ready-to-copy viral captions and hashtag strategies.
- **Root CLI Entrypoint**: Seamless root-level `python cli.py` wrapper alongside package scripts.
- **Continuous Integration**: Multi-OS GitHub Actions workflow validating Python 3.10-3.12 compatibility.
