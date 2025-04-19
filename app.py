import streamlit as st
import datetime
import json

# Load knowledge base
try:
    with open("knowledge_base.json", "r") as f:
        knowledge_base = json.load(f)
except FileNotFoundError:
    knowledge_base = {"advice": "No advice available. Please update the knowledge base."}

def get_training_advice():
    return knowledge_base.get("advice", "Keep training consistent and positive!")

def view_logs():
    try:
        with open("training_log.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No logs found."

def log_entry(entry):
    with open("training_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {entry}\n")

# Streamlit UI
st.title("🐴 Horse Training AI Assistant")

menu = st.sidebar.selectbox("Menu", ["Get Training Advice", "View Logs", "Add Log Entry"])

if menu == "Get Training Advice":
    st.subheader("Training Advice")
    st.write(get_training_advice())

elif menu == "View Logs":
    st.subheader("Training Logs")
    st.text(view_logs())

elif menu == "Add Log Entry":
    st.subheader("New Log Entry")
    note = st.text_area("Write a note about today’s session:")
    if st.button("Save Entry"):
        log_entry(note)
        st.success("Entry saved!")
