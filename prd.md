# 📝 PRD: VibeCheck AI

**Project:** AI-Powered Vibe-to-Playlist Generator

**Version:** 1.0 (MVP)

**Status:** Ready for Development

---

## 1. Executive Summary

**VibeCheck AI** is a niche AI wrapper designed to solve the "I don't know what to listen to" problem by focusing on atmospheric and emotional context. Unlike standard music search engines, it uses a Large Language Model (LLM) to interpret complex, abstract user descriptions and translate them into a curated 10-song playlist.

---

## 2. Target Audience

- **The Atmospheric Listener:** People who want music for specific moods (e.g., "studying in a rainy castle").
- **The Trend Follower:** Users looking for music that fits social media "aesthetics" (e.g., Cottagecore, Dark Academia).
- **The Music Explorer:** People bored of their own algorithm who want a "curated" feel.

---

## 3. User Stories

- **Input:** "As a user, I want to describe my vibe in my own words so I don't have to guess genre tags."
- **Curation:** "As a user, I want the AI to explain _why_ it chose a song so I feel a connection to the playlist."
- **Utility:** "As a user, I want the output to be a clear list so I can quickly search for the songs on my streaming app."

---

## 4. Functional Requirements

| Feature               | Description                                                       | Priority        |
| --------------------- | ----------------------------------------------------------------- | --------------- |
| **Vibe Input Field**  | A text box that accepts up to 500 characters of natural language. | **Must-Have**   |
| **LLM Integration**   | A backend connection to Gemini or OpenAI to process the prompt.   | **Must-Have**   |
| **Formatted Output**  | Displaying the playlist in a structured Markdown table.           | **Must-Have**   |
| **Reset/Clear**       | A button to quickly start a new vibe search.                      | **Should-Have** |
| **Copy to Clipboard** | A one-click button to copy the song list.                         | **Could-Have**  |

---

## 5. Technical Architecture

The app follows a classic "AI Wrapper" architecture:

1. **Frontend:** Built with **Streamlit** (Python-based) for rapid prototyping.
2. **Logic Layer:** A Python script that takes user input, combines it with a "System Prompt," and sends it to the API.
3. **API:** **Gemini 1.5 Flash** (chosen for high speed and low cost).

---

## 6. The "System Prompt" Logic

The core "product" of a wrapper is the instructions hidden from the user.

> **Developer Note:** Use the following instructions in your API call to ensure the AI behaves correctly:
> _"You are a world-class DJ and music historian. Your goal is to create a 10-song playlist based on the user's vibe description. Your response must ONLY be a Markdown table with the following columns: Track Number, Song Title, Artist, and 'Why it fits'. Do not provide any conversational text before or after the table."_

---

## 7. Success Metrics & Future Roadmap

- **Success Metric:** Time-to-Playlist (Target: < 4 seconds).
- **Success Metric:** User retention (Do people come back for a second vibe?).

### **Future Versions (v1.1+)**

- **Direct Export:** Integrate with the Spotify API to create the playlist automatically in the user's account.
- **Album Art:** Use a second AI (like DALL-E or Imagen) to generate a "Cover Art" image for the vibe.
