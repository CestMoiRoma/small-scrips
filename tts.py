#!/usr/bin/env python3
"""
tts.py — Apple TTS (say) → MP3
Usage:
  python3 tts.py "Bonjour le monde"
  python3 tts.py "Bonjour" 220
  python3 tts.py "Hello" 220 -o hello.mp3 -v Samantha
  echo "texte depuis stdin" | python3 tts.py -
"""

import sys
import argparse
import subprocess
import tempfile
import os
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(
        description="Convertit du texte en MP3 via la commande say de macOS."
    )
    p.add_argument(
        "text",
        nargs="?",
        help="Texte à synthétiser. Utilisez '-' pour lire depuis stdin.",
    )
    p.add_argument(
        "-r", "--rate",
        type=int,
        default=175,
        help="Vitesse de parole en mots/minute (défaut : 175).",
    )
    p.add_argument(
        "-v", "--voice",
        default=None,
        help="Voix à utiliser (ex: Thomas, Samantha). Défaut : voix système.",
    )
    p.add_argument(
        "-o", "--output",
        default="output.mp3",
        help="Fichier MP3 de sortie (défaut : output.mp3).",
    )
    p.add_argument(
        "--list-voices",
        action="store_true",
        help="Affiche les voix disponibles et quitte.",
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
        # ── Étape 1 : say → AIFF ─────────────────────────────────────────
        say_cmd = ["say", "-r", str(rate), "-o", tmp_path]
        if voice:
            say_cmd += ["-v", voice]
        say_cmd.append(text)

        print(f"🗣  Synthèse  | voix: {voice or 'système'}  |  rate: {rate} wpm")
        result = subprocess.run(say_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Erreur say : {result.stderr.strip()}")
            return False

        # ── Étape 2 : AIFF → MP3 via ffmpeg ─────────────────────────────
        ffmpeg_cmd = [
            "ffmpeg", "-y",           # écraser sans demander
            "-i", tmp_path,
            "-codec:a", "libmp3lame",
            "-q:a", "2",              # qualité VBR haute (~190 kbps)
            str(output_path),
        ]

        print(f"🔄  Conversion MP3…")
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Erreur ffmpeg : {result.stderr.strip()}")
            return False

        size_kb = output_path.stat().st_size // 1024
        print(f"✅  Fichier créé : {output_path}  ({size_kb} Ko)")
        return True

    finally:
        os.unlink(tmp_path)


def main():
    if sys.platform != "darwin":
        print("Ce script nécessite macOS (commande say).")
        sys.exit(1)

    args = parse_args()

    if args.list_voices:
        list_voices()
        return

    # Lecture du texte
    if args.text == "-" or (args.text is None and not sys.stdin.isatty()):
        text = sys.stdin.read().strip()
    elif args.text:
        text = args.text
    else:
        print("Erreur : fournissez un texte ou utilisez '-' pour stdin.")
        print("         python3 tts.py --help")
        sys.exit(1)

    if not text:
        print("Erreur : le texte est vide.")
        sys.exit(1)

    success = synthesize(text, args.rate, args.voice, args.output)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
