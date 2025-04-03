import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    st.error("The environment variable GOOGLE_API_KEY is not set. Please make sure the .env file is configured correctly.")
    st.stop()

genai.configure(api_key=google_api_key)

def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])
        transcript_text = " ".join([line['text'] for line in transcript])
        return transcript_text
    except Exception:
        return None

def summarize_transcript(transcript_text):
    if not transcript_text:
        return "Transcript not available for this video."
    try:
        llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key)
        summarize_chain = load_summarize_chain(llm, chain_type="stuff")
        document = [Document(page_content=transcript_text)]
        summary_output = summarize_chain.run(document)
        return summary_output
    except Exception as e:
        st.error(f"Error summarizing transcript: {e}")
        return "Error summarizing."

st.markdown("""
<style>
.big-title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}
.section-title {
    font-size: 24px;
    color: #2e8aff;
    margin-bottom: 10px;
    margin-top: 30px;
}
.summary-box {
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
}
.summary-text {
    font-size: 16px;
    line-height: 1.6;
}
.stTextInput label {
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-title'>Summarize YouTube Videos with Gemini and Langchain</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Paste the YouTube video link</h2>", unsafe_allow_html=True)
video_url = st.text_input("YouTube video URL:")

if video_url:
    video_id = video_url.split("v=")[-1]
    if "&" in video_id:
        video_id = video_id.split("&")[0]
    st.markdown("<h2 class='section-title'>Watch the video here:</h2>", unsafe_allow_html=True)
    st.video(f"https://www.youtube.com/watch?v={video_id}")
    with st.spinner("Extracting transcript and summarizing..."):
        transcript_text = get_youtube_transcript(video_id)
        if transcript_text:
            summary = summarize_transcript(transcript_text)
            st.markdown("<h2 class='section-title'>Summary:</h2>", unsafe_allow_html=True)
            st.markdown(f"<div class='summary-box'><p class='summary-text'>{summary}</p></div>", unsafe_allow_html=True)
            with st.expander("View full transcript"):
                st.write(transcript_text)
        else:
            st.error("Could not retrieve the transcript for this video. Make sure the video has either automatically generated subtitles or ones provided by the creator.")
