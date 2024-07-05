import streamlit as st


def initialize_sum(initial_counters):
    if 'total_sum' not in st.session_state:
        st.session_state['total_sum'] = sum(counter['initValue'] for counter in initial_counters)
    if 'counters' not in st.session_state:
        st.session_state['counters'] = initial_counters


def reset(index):
    if f'count_{index}' in st.session_state:
        st.session_state['total_sum'] -= st.session_state[f'count_{index}']
        st.session_state[f'count_{index}'] = 0



def compteur(index, initvalue, title):
    if f'count_{index}' not in st.session_state:
        st.session_state[f'count_{index}'] = initvalue
        if 'total_sum' not in st.session_state:
            st.session_state['total_sum'] = 0
        st.session_state['total_sum'] += initvalue

    def increment():
        st.session_state[f'count_{index}'] += 1
        st.session_state['total_sum'] += 1

    def decrement():
        if st.session_state[f'count_{index}'] > 0:
            st.session_state[f'count_{index}'] -= 1
            st.session_state['total_sum'] -= 1

    display_title = f"{title} ({st.session_state[f'count_{index}']})"
    st.markdown(f"<h2 style='margin-left: 170px'>{display_title}</h2>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col3:
        st.button("\+", on_click=increment, key=f"{index}_increment")

    with col2:
        st.write(st.session_state[f'count_{index}'])

    with col1:
        st.button("\-", on_click=decrement, disabled=st.session_state[f'count_{index}'] == 0, key=f"{index}_decrement")

    with col4:
        st.button("Reset", on_click=reset, args=(index,), key=f"{index}_reset")



def get_sum():
    if 'total_sum' not in st.session_state:
        st.session_state['total_sum'] = 0
    return st.session_state['total_sum']


