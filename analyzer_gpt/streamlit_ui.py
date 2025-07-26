import streamlit as st
import asyncio
import os

st.title("Analyzer GPT - Digital Data Analyzer")

upload_file = st.file_uploader("Upload as CSV file")

task = st.chat_input("Enter your task here...")

if task:
    async def analyze_data(task):