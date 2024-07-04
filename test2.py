import streamlit as st
import test

array_of_counters = [
    {"title": "Counter 1", "initValue": 10},
    {"title": "Counter 2", "initValue": 20},
    {"title": "Counter 3", "initValue": 30},
    {"title": "Counter 4", "initValue": 40},
    {"title": "Counter 5", "initValue": 50}
]

test.initialize_sum(array_of_counters)

st.write('Sum:', test.get_sum())

for i, counter in enumerate(array_of_counters):
    test.compteur(key=str(i), title=counter["title"], initvalue=counter["initValue"])

