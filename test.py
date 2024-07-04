import streamlit as st

def initialize_sum(initial_counters):
    if 'total_sum' not in st.session_state:
        st.session_state['total_sum'] = sum(counter['initValue'] for counter in initial_counters)

def compteur(key, initvalue, title):
    if f'count_{key}' not in st.session_state:
        st.session_state[f'count_{key}'] = initvalue

    def increment():
        st.session_state[f'count_{key}'] += 1
        st.session_state['total_sum'] += 1

    def decrement():
        if st.session_state[f'count_{key}'] > 0:
            st.session_state[f'count_{key}'] -= 1
            st.session_state['total_sum'] -= 1

    st.markdown(f"<h2 style=' margin-left : 170px'>{title}</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col3:
        st.button("\+", on_click=increment, key=f"{key}_increment")

    with col2:
        st.write(st.session_state[f'count_{key}'])

    with col1:
        st.button("\-", on_click=decrement, disabled=st.session_state[f'count_{key}'] == 0, key=f"{key}_decrement")

def get_sum():
    return st.session_state['total_sum']
