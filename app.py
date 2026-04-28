import streamlit as st
import time
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Import your agent classes
from agents.research_agent import ResearchAgent
from agents.distillation_agent import DistillationAgent
from agents.content_creator_agent import ContentCreatorAgent
from agents.critic_agent import CriticAgent
from agents.adapter_agent import AdapterAgent

def main():
    st.set_page_config(page_title="Multi-Platform Content Orchestrator", page_icon="🚀")
    st.title("🚀 Multi-Platform Technical Content Orchestrator")
    st.write("Turn your weekly technical learnings into polished posts for LinkedIn, Twitter, and WhatsApp.")

    # Initialize the agents
    researcher = ResearchAgent()
    distiller = DistillationAgent()
    creator = ContentCreatorAgent()
    critic = CriticAgent()
    adapter = AdapterAgent()

    # Get user input
    topic = st.text_input("What did you learn or build this week?")

    if st.button("Generate Content"):
        if topic:
            try:
                # --- AGENT 1 ---
                with st.spinner("Agent 1: Researching latest docs..."):
                    raw_research = researcher.run(topic)
                st.success("Research complete!")
                time.sleep(2) 

                # --- AGENT 2 ---
                with st.spinner("Agent 2: Distilling knowledge..."):
                    structured_data = distiller.run(raw_research)
                st.success("Data distilled!")
                time.sleep(2)

                # --- AGENT 3 (Initial Draft) ---
                with st.spinner("Agent 3: Creating first draft..."):
                    first_draft = creator.run(structured_data)
                st.success("First draft ready!")
                time.sleep(2)

                # --- AGENT 4 (Self-Reflection Loop) ---
                with st.spinner("Agent 4: Critic reviewing the draft..."):
                    critique = critic.run(first_draft, structured_data)
                st.success("Critique finished!")
                time.sleep(2)

                # Final Refinement
                with st.spinner("Refining based on feedback..."):
                    final_post = creator.refine(first_draft, critique)
                
                # --- AGENT 5 (Multi-Platform Adapter) ---
                with st.spinner("Agent 5: Adapting for other platforms..."):
                    tweet = adapter.to_twitter(structured_data)
                    wa_message = adapter.to_whatsapp(structured_data)
                st.success("Platforms adapted!")

                # UI Output with Tabs
                st.subheader("📱 Finalized Content")
                tab1, tab2, tab3 = st.tabs(["LinkedIn", "Twitter (X)", "WhatsApp"])
                
                with tab1:
                    st.text_area("Share on LinkedIn:", value=final_post, height=400, key="li_post")
                
                with tab2:
                    st.text_area("Share on Twitter (X):", value=tweet, height=150, key="tw_post")
                
                with tab3:
                    st.text_area("Share on WhatsApp:", value=wa_message, height=150, key="wa_post")
                
                with st.expander("🔍 View AI Critic's Feedback"):
                    st.info(critique)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a topic before generating!")

if __name__ == "__main__":
    main()
