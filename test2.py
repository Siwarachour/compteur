import streamlit as st
import test

if 'counters' not in st.session_state:
    st.session_state.counters = [
        {"title": "Counter 1", "initValue": 10},
        {"title": "Counter 2", "initValue": 20},
        {"title": "Counter 3", "initValue": 30},
        {"title": "Counter 4", "initValue": 40},
        {"title": "Counter 5", "initValue": 50}
    ]

def add_counter():
    new_counter_index = len(st.session_state.counters)
    st.session_state.counters.append({
        "title": f"Counter {new_counter_index + 1}",
        "initValue": 0
    })
    update_sum()  # Update the sum after adding a counter

def delete_counter(index):
    # Call the test.reset() method if necessary
    test.reset(str(index))

    # Remove the counter from the list
    st.session_state.counters.pop(index)

    # Remove the counter's state
    if f'count_{index}' in st.session_state:
        st.session_state['total_sum'] -= st.session_state[f'count_{index}']
        del st.session_state[f'count_{index}']

    # Reindex counters after deletion
    for i in range(index, len(st.session_state.counters)):
        if f'count_{i+1}' in st.session_state:
            st.session_state[f'count_{i}'] = st.session_state.pop(f'count_{i+1}', 0)

    # Update the sum
    update_sum()


def update_sum():
    st.session_state.sum = test.get_sum()

def reset_all():
    for i in range(len(st.session_state.counters)):
        test.reset(str(i))
    update_sum()

# Initialize sum
if 'sum' not in st.session_state:
    update_sum()

# Add "Add Counter" button
col1, col2 = st.columns([1, 1])
with col2:
    st.button("Add Counter", on_click=add_counter)

# Add "Reset" button
with col1:
    if st.button('Reset'):
        reset_all()

# Display the counters with delete buttons
for i, counter in enumerate(st.session_state.counters):
    col1, col2 = st.columns([4, 1])
    with col1:
        test.compteur(index=str(i), title=counter["title"], initvalue=int(counter["initValue"]))
    with col2:
        if st.button(f"Delete {counter['title']}", key=f"delete_{i}"):
            delete_counter(i)
            st.experimental_rerun()  # Re-run the app to reflect changes

# Display the sum
st.write('Sum:', test.get_sum())
