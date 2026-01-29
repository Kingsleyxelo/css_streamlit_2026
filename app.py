# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

# ---------- Safe Background Color ----------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;  /* Light blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.set_page_config(page_title="The Smart Student App", layout="centered")

st.title("🎓 The Smart Student App")
st.write("A simple app to calculate grades and track expenses.")

# Create tabs
tab1, tab2 = st.tabs(["📊 Grade Calculator", "💰 Expense Tracker"])

# -------------------------
# GRADE CALCULATOR
# -------------------------
with tab1:
    st.header("Grade Calculator")

    mark = st.number_input(
        "Enter your mark (%)",
        min_value=0.0,
        max_value=100.0,
        format="%.2f"
    )

    if st.button("Calculate Grade"):
        if mark >= 75:
            st.success("🎉 Distinction")
        elif mark >= 60:
            st.info("✅ Pass")
        elif mark >= 50:
            st.warning("⚠️ Sub-minimum")
        else:
            st.error("❌ Fail")

# -------------------------
# EXPENSE TRACKER
# -------------------------
with tab2:
    st.header("Expense Tracker")

    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    expense_name = st.text_input("Expense name")
    expense_amount = st.number_input(
        "Amount",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("Add Expense"):
        if expense_name != "":
            st.session_state.expenses.append((expense_name, expense_amount))
            st.success("Expense added!")
        else:
            st.warning("Please enter an expense name.")

    st.subheader("Expenses")

    total = 0
    for name, amount in st.session_state.expenses:
        st.write(f"- {name}: R{amount:.2f}")
        total += amount

    st.info(f"💸 Total Spent: R{total:.2f}")



