"""

"""
import os
from uuid import uuid4 # generates unique ids 
# from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.tools.eleven_labs import ElevenLabsTools
from agno.tools.firecrawl import FirecrawlTools
from agno.agent import Agent,RunResponse
from agno.utils.audio import write_audio_to_file
from agno.utils.log import logger
import streamlit as st
st.set_page_config(page_title='📄🎤 Blog to Podcast Agent',page_icon='🎤')
st.title('📄 ➡️🎤 Blog to Podcast Agent')
st.sidebar.header('🔑API Keys')
# anthropic_key=st.sidebar.text_input("Anthropic API Key",type="password")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
elevenlabs_key=st.sidebar.text_input('ElevenLabs API Key', type="password")
firecrawl_key=st.sidebar.text_input("Firecrawl API Key",type='password')
keys=all([openai_api_key,elevenlabs_key,firecrawl_key]) # It checks all the keys are listed , if any one of them is missing then it will show false
url=st.text_input('Enter the blog URL:',"")
generate_button =st.button("Generate Podcast",disabled=not keys) # if keys are not given then the button
if not keys:
    st.warning("Please enter all the required API keys to enable podcast generation")
if generate_button:
    if url.strip()=="":
        st.warning("Please enter a blog URL first.")
    else:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ['ELEVEN_LABS_API_KEY']=elevenlabs_key
        os.environ['FIRECRAWL_API_KEY']=firecrawl_key
        with st.spinner("Processing.. Scrapping blog, summarizing and generating podcast "):
            try:
                blog_to_podcast_agent=Agent(
                    name="Blog To Podcast Aent",
                    agent_id="blog_to_podcast_agent",
                    model=OpenAIChat(id="gpt-4.1-nano"),
                    tools=[
                        ElevenLabsTools(
                            voice_id="JBFqnCBsd6RMkjVDRZzb",
                            model_id="eleven_multilingual_v2",
                            target_directory="audio_generations",                            
                        ),
                        FirecrawlTools(),
                    ],
                    description="You are an AI agent that can generate audio using the ElevenLabs API.",
                    instructions=[
                        "When the user provides a blog URL:",
                        "1. Use FirecrawlTools to scrape the blog content",
                        "2. Create a concise summary of the blog content that is NO MORE than 2000 characters long",
                        "3. The summary should capture the main points while being engaging and conversational",
                        "4. Use the ElevenLabsTools to convert the summary to audio",
                        "Ensure the summary is within the 2000 character limit to avoid ElevenLabs API limits",
                    ],
                    markdown=True,
                    debug_mode=True,
                )
                podcast: RunResponse = blog_to_podcast_agent.run(
                    f"Convert the blog content to a podcast: {url}"
                )
                save_dir="Audio_Generation"
                os.makedirs(save_dir,exist_ok=True)
                if podcast.audio and len(podcast.audio) > 0:
                    filename=f"{save_dir}/podcast_{uuid4()}.wav"
                    write_audio_to_file(
                        audio=podcast.audio[0].base64_audio,
                        filename=filename
                    )
                    st.success("Podcast Generated Successfully! 🎧")
                    audio_bytes=open(filename,"rb").read()
                    st.audio(audio_bytes, format="audio/wav")
                    st.download_button(
                        label="Donwload Podcast",
                        data=audio_bytes,
                        file_name='Generated_podcast.wav',
                        mime='audio/wav'
                        
                    )
                else:
                    st.error('No audio was generated.Please try again')
            
            except Exception as e:
                st.error(f'An eror has occured: {e}')
                logger.error(f"Streamlit app error: {e}")
        
    