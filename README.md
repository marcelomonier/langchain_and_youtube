# Summarize YouTube Videos with Gemini and Langchain

This project allows you to extract the transcript of a YouTube video and use Google's Gemini model (via the [Google Generative AI](https://github.com/google/generative-ai-python) library) in combination with [Langchain](https://github.com/hwchase17/langchain) to generate a concise summary directly in a [Streamlit](https://streamlit.io/) application.

## Overview

- **Purpose**: Provide a simple and elegant web interface to:
  1. Extract a video's transcript from YouTube.
  2. Automatically summarize that transcript using Google's Gemini model.
  3. Display the video itself and the resulting summary on a single page.

- **Key Technologies**:
  - [Streamlit](https://streamlit.io/): Quickly build data and AI web apps in Python.
  - [Google Generative AI](https://github.com/google/generative-ai-python): Access to Google’s LLMs (Gemini in this case).
  - [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/): Retrieve subtitles (transcripts) from YouTube videos.
  - [Langchain](https://github.com/hwchase17/langchain): A framework for orchestrating LLM usage.
  - [Python-dotenv](https://pypi.org/project/python-dotenv/): Manages environment variables securely.

## Prerequisites

1. **Python 3.7+**  
   Make sure you have Python installed on your system.

2. **Google API Key**  
   - You need a Google Cloud developer account and must enable the Generative AI (PaLM) API.
   - Create and obtain your `GOOGLE_API_KEY` to use the Gemini model.

3. **Package Installation**  
   In the project directory, run:
   ```bash
   pip install -r requirements.txt
   ```
   If you don’t have a `requirements.txt` file yet, create one containing the packages used:
   ```text
   streamlit
   google-generativeai
   youtube_transcript_api
   langchain
   langchain_google_genai
   python-dotenv
   ```

4. **Environment Variables**  
   Create a `.env` file at the project root with the following content:
   ```
   GOOGLE_API_KEY=YOUR_KEY_HERE
   ```

- **.env**: File that stores the `GOOGLE_API_KEY` environment variable.
- **requirements.txt**: List of the necessary libraries to run the application.
- **app.py**: Main script containing the Streamlit code.

## How to Run

1. **Clone this repository** (or download as a ZIP and extract):
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. **Navigate to the project folder**:
   ```bash
   cd your-repo
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Create the `.env` file** with your API key, for example:
   ```
   GOOGLE_API_KEY=YOUR_API_KEY_HERE
   ```
5. **Start the application**:
   ```bash
   streamlit run app.py
   ```
6. **Open your browser** at the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

1. **Paste the YouTube video link**: Enter the URL in the text input field.
2. **Wait for the transcript**: The app automatically fetches the subtitles (transcript) from the video.
3. **Summary**: The Gemini model processes the transcript and displays a summary on the same page.
4. **Optional**: Click on **"View full transcript"** to see the entire video transcript.

## Customization

- You can change the look and feel (colors, fonts, sizes) by editing the `<style>` section within `app.py`.
- To switch to a different LLM model, modify the `model` parameter when instantiating `GoogleGenerativeAI`.

## Contributing

Contributions are welcome! Follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b my-new-feature
   ```
3. Commit your changes.
4. Open a pull request (PR) for this repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for more details (if present).

---

<sub>**Note**: Make sure the YouTube video has subtitles (automatic or creator-provided) to successfully retrieve the transcript.</sub>