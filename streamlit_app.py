import streamlit as st
import time
import pandas as pd
from datetime import datetime

# --- CONFIGURATION & THEME (Tesla/Jarvis Inspired) ---
st.set_page_config(page_title="Jarvis CS-1 Study OS", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #f4f4f4; color: #171a20; font-family: 'Segoe UI', sans-serif; }
    .stButton>button { background-color: #3d3d3d; color: white; border-radius: 20px; border: none; padding: 10px 24px; font-weight: 600; }
    .stButton>button:hover { background-color: #171a20; color: #ffffff; }
    .card { background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; border: 1px solid #e2e2e2; }
    .flashcard { background: #ffffff; border: 1px solid #6366f1; border-radius: 12px; padding: 20px; text-align: center; transition: 0.3s; cursor: pointer; }
    .flashcard:hover { transform: scale(1.02); box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15); }
    .mhtcet-sync { position: fixed; top: 20px; right: 20px; background: #ffeded; border: 1px solid #ff4d4d; color: #b91c1c; padding: 10px 20px; border-radius: 10px; font-size: 12px; z-index: 1000; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- MHTCET FLOATING SYNC ---
st.markdown('<div class="mhtcet-sync">⚠️ MHTCET SYNC: Day 3 Backlog (Matrices, Solutions, Dual Nature)</div>', unsafe_allow_html=True)

# --- SIDEBAR: GEMINI ASSISTANT PANEL ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Jarvis_Logo.png", width=100)
    st.title("Assistant Panel")
    st.markdown("---")
    st.subheader("Doubt Solver UI")
    st.info("Harsh, Binary Search algorithm aur C++ Inheritance 15+ marks guarantee karte hain. Inhe paper pe likh ke practice kar.")
    
    st.markdown("---")
    st.subheader("Motivational Quote")
    st.warning('"Precision in code leads to perfection in results."')
    
    st.markdown("---")
    st.subheader("Progress Analytics")
    prog = st.progress(0)
    st.write("Exam Readiness: 0%")

# --- MAIN CONTENT ---
st.title("CS-1: Professional Study Dashboard")
st.write("Saturday, Feb 28, 2026 | User: Harsh Dhondu Rasam La")

# --- ANALYTICS DASHBOARD ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Hours", "9.5 Hours")
with col2:
    st.metric("Micro-Topics", "12 Topics")
with col3:
    st.metric("MHTCET Backlog", "Day 3")

# --- DETAILED TIMETABLE (11 AM - 10 PM) ---
st.header("Detailed Performance Schedule")

# Micro-Topic Mapping
schedule_data = [
    {"Time": "11:00 AM - 12:00 PM", "Module": "Intro & C++ Basics", "Topic": "OOP Principles, Class Logic", "Goal": "POP vs OOP Difference"},
    {"Time": "12:00 PM - 01:30 PM", "Module": "C++ Logic Engine", "Topic": "Constructors & Destructors", "Goal": "Default vs Copy Const."},
    {"Time": "01:30 PM - 03:00 PM", "Module": "Advanced C++", "Topic": "Inheritance & File Streams", "Goal": "Multiple Inheritance Diagram"},
    {"Time": "03:00 PM - 03:30 PM", "Module": "REST PERIOD", "Topic": "LUNCH BREAK (DINNER)", "Goal": "Complete Nutrition"},
    {"Time": "03:30 PM - 05:30 PM", "Module": "OS Kernel", "Topic": "Memory Mgmt & Processes", "Goal": "Process States Diagram"},
    {"Time": "05:30 PM - 07:30 PM", "Module": "Interface & Data", "Topic": "HTML Tables & Binary Search", "Goal": "Rowspan/Colspan Logic"},
    {"Time": "07:30 PM - 09:30 PM", "Module": "PROGRAMMING LAB", "Topic": "Code Drill Execution", "Goal": "Paper-Pen Program Practice"},
    {"Time": "09:30 PM - 10:00 PM", "Module": "NIGHT MEAL", "Topic": "DINNER", "Goal": "Review Day Goals"}
]

df = pd.DataFrame(schedule_data)
st.table(df)

# --- INTERACTIVE TASKS & POMODORO ---
st.markdown("---")
st.subheader("Live Session Execution")

col_timer, col_task = st.columns([1, 2])

with col_timer:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("⏱ **Focus Timer (Pomodoro)**")
    count_time = st.empty()
    if st.button("Start 25m Focus Session"):
        for i in range(1500, -1, -1):
            mins, secs = divmod(i, 60)
            count_time.subheader(f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            if i == 0:
                st.balloons()
                st.error("Time's Up! Active Recall Required.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_task:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("✅ **Current Task Checklist**")
    t1 = st.checkbox("C++ OOP Principles (Abstraction/Encapsulation)")
    t2 = st.checkbox("Constructor Types & Destructor Syntax")
    t3 = st.checkbox("Inheritance Logic (Multiple/Multilevel)")
    st.markdown('</div>', unsafe_allow_html=True)

# --- RECALL ENGINE (Modal Style) ---
if st.button("Complete Session & Open Recall Engine"):
    with st.expander("🚨 ACTIVE RECALL: Verify Knowledge Before Break", expanded=True):
        st.write("1. Explain the difference between POP and OOP (4 Marks).")
        st.write("2. Can a Constructor have a return type? Why?")
        st.write("3. Draw the 5 states of a Process in an OS.")
        st.success("Mentally check these before your 5-min break.")

# --- FLASHCARD FLIP-DECK ---
st.markdown("---")
st.header("Flashcard Flip-Deck (Hover/Click)")
f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    with st.expander("Binary Search"):
        st.write("Divide and Conquer logic. O(log n) complexity. Array must be sorted.")
with f_col2:
    with st.expander("Virtual Memory"):
        st.write("Using disk space to simulate RAM. Allows running larger programs than physical RAM.")
with f_col3:
    with st.expander("Inheritance"):
        st.write("Capability of a class to derive properties from another class for reusability.")

# --- PROGRAMMING LAB (Night Session) ---
st.markdown("---")
st.header("The Programming Lab (6:00 PM - 9:30 PM)")
st.info("Write these programs on paper. Do not use a compiler today.")
lab_tasks = ["Factorial using Class", "HTML Table with Rowspan/Colspan", "Binary Search Algorithm"]
for task in lab_tasks:
    st.checkbox(f"Practice: {task}")

st.write("---")
st.caption("Jarvis OS v4.0 | Created for Harsh Dhondu Rasam La")
