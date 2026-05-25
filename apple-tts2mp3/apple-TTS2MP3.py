#!/usr/bin/env python3
"""
tts.py — Apple TTS (say) → MP3
Usage:
  python3 tts.py "Hello world"
  python3 tts.py "Hello" 220
  python3 tts.py "Hello" 220 -o hello.mp3 -v Samantha
  echo "text from stdin" | python3 tts.py -
"""

import sys
import argparse
import subprocess
import tempfile
import os
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(
        description="Converts text to MP3 using the macOS say command."
    )
    p.add_argument(
        "text",
        nargs="?",
        help="Text to synthesize. Use '-' to read from stdin.",
    )
    p.add_argument(
        "-r", "--rate",
        type=int,
        default=175,
        help="Speech rate in words per minute (default: 175).",
    )
    p.add_argument(
        "-v", "--voice",
        default=None,
        help="Voice to use (e.g. Thomas, Samantha). Default: system voice.",
    )
    p.add_argument(
        "-o", "--output",
        default="output.mp3",
        help="Output MP3 file (default: output.mp3).",
    )
    p.add_argument(
        "--list-voices",
        action="store_true",
        help="List available voices and exit.",
    )
    return p.parse_args()


def list_voices():
    result = subprocess.run(["say", "-v", "?"], capture_output=True, text=True)
    print(result.stdout)


def synthesize(text: str, rate: int, voice: str | None, output: str):
    output_path = Path(output)
    if output_path.suffix.lower() != ".mp3":
        output_path = output_path.with_suffix(".mp3")

    with tempfile.NamedTemporaryFile(suffix=".aiff", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # ── Step 1: say → AIFF ───────────────────────────────────────────
        say_cmd = ["say", "-r", str(rate), "-o", tmp_path]
        if voice:
            say_cmd += ["-v", voice]
        say_cmd.append(text)

        print(f"🗣  Synthesizing  | voice: {voice or 'system'}  |  rate: {rate} wpm")
        result = subprocess.run(say_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"say error: {result.stderr.strip()}")
            return False

        # ── Step 2: AIFF → MP3 via ffmpeg ────────────────────────────────
        ffmpeg_cmd = [
            "ffmpeg", "-y",           # overwrite without asking
            "-i", tmp_path,
            "-codec:a", "libmp3lame",
            "-q:a", "2",              # high VBR quality (~190 kbps)
            str(output_path),
        ]

        print(f"🔄  Converting to MP3…")
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"ffmpeg error: {result.stderr.strip()}")
            return False

        size_kb = output_path.stat().st_size // 1024
        print(f"✅  File created: {output_path}  ({size_kb} KB)")
        return True

    finally:
        os.unlink(tmp_path)


def main():
    if sys.platform != "darwin":
        print("This script requires macOS (say command).")
        sys.exit(1)

    args = parse_args()

    if args.list_voices:
        list_voices()
        return

    # Read the input text
    if args.text == "-" or (args.text is None and not sys.stdin.isatty()):
        text = sys.stdin.read().strip()
    elif args.text:
        text = args.text
    else:
        print("Error: provide text or use '-' to read from stdin.")
        print("       python3 tts.py --help")
        sys.exit(1)

    if not text:
        print("Error: text is empty.")
        sys.exit(1)

    success = synthesize(text, args.rate, args.voice, args.output)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
