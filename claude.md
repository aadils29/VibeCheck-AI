# VibeCheck AI — Project Context

## Overview

VibeCheck AI is an AI-powered vibe-to-playlist generator. Users describe a mood or atmosphere in natural language, and the app returns a curated 10-song playlist using an LLM. This is an MVP (v1.0).

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM API:** Google Gemini 1.5 Flash
- **No database** — stateless, no user accounts

## Architecture

Simple 3-layer "AI wrapper":

1. **Streamlit UI** — text input (500 char max), display playlist as Markdown table, reset button
2. **Logic layer** — Python module that builds the prompt (system + user input) and calls the API
3. **Gemini API** — processes the prompt and returns the playlist

## Key Behaviors

- The system prompt instructs the LLM to act as a DJ/music historian and return ONLY a Markdown table with columns: Track Number, Song Title, Artist, Why it fits
- No conversational text before or after the table in the LLM response
- Target response time: < 4 seconds

## Project Structure Conventions

- Keep the app simple and flat — avoid unnecessary abstraction for an MVP
- Use `app.py` as the Streamlit entry point
- Store API key via environment variable (`GOOGLE_API_KEY`) or Streamlit secrets
- Use a `.env` file for local development (never commit it)

## Code Style

- Use clear, readable Python — this is a learning/portfolio project
- Add docstrings to functions
- Keep the system prompt as a constant, easy to find and tweak
- Handle API errors gracefully with user-friendly messages in the UI

## Important Context

- See `prd.md` for the full product requirements document
- Future versions may add Spotify API integration and AI-generated cover art — don't over-engineer for these now, but don't make choices that block them either
