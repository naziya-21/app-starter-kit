import streamlit as st
import pandas as pd
from datetime import datetime
import json

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

def load_knowledge_base():
    """Load the knowledge base"""
    return {
        "basic_questions": {
            "what is python": "Python is a high-level programming language known for its simplicity and readability.",
            "what is mathematics": "Mathematics is the study of numbers, quantities, and shapes.",
            "what is science": "Science is the systematic study of the natural world through observation and experiments.",
            "who was albert einstein": "Albert Einstein was a theoretical physicist who developed the theory of relativity.",
            "what is gravity": "Gravity is a force that attracts objects toward each other, most notably keeping planets in orbit.",
            "what is photosynthesis": "Photosynthesis is the process by which plants convert sunlight into energy."
        }
    }

def find_answer(question, knowledge_base):
    """Find answer from knowledge base"""
    question = question.lower()
    
    # Search in basic questions
    for q, a in knowledge_base["basic_questions"].items():
        if question in q.lower() or q.lower() in question:
            return a
    
    return "I'm sorry, I don't know the answer to that question yet. Try asking something about Python, mathematics, science, Einstein, gravity, or photosynthesis."

def save_conversation(question, answer):
    """Save conversation to history"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.conversation_history.append({
        "timestamp": timestamp,
        "question": question,
        "answer": answer
    })

def main():
    st.title("Educational Learning Assistant")
    st.write("Ask questions about Python, mathematics, science, and more!")
    
    # Load knowledge base
    knowledge_base = load_knowledge_base()
    
    # Main interface
    question = st.text_input("Type your question here:", key="question_input")
    
    if st.button("Get Answer"):
        if question:
            answer = find_answer(question, knowledge_base)
            st.write("---")
            st.write("📝 Your question:", question)
            st.write("💡 Answer:", answer)
            save_conversation(question, answer)
    
    # Sidebar for history
    st.sidebar.title("Learning History")
    if st.session_state.conversation_history:
        history_df = pd.DataFrame(st.session_state.conversation_history)
        st.sidebar.dataframe(history_df, use_container_width=True)
        
        # Show statistics
        st.sidebar.write("---")
        st.sidebar.subheader("Statistics")
        total_questions = len(st.session_state.conversation_history)
        st.sidebar.write(f"Total questions asked: {total_questions}")

if __name__ == "__main__":
    main()
