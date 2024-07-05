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


if 'sum' not in st.session_state:
    st.session_state.sum = sum(counter['initValue'] for counter in st.session_state.counters)


if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False

def add_counter(title, init_value):
    new_counter = {
        "title": title,
        "initValue": init_value
    }
    st.session_state.counters.append(new_counter)
    update_sum()
    st.session_state.show_popup = False
    st.experimental_rerun()

def delete_counter(index):
    test.reset(str(index))

    st.session_state.counters.pop(index)


    if f'count_{index}' in st.session_state:
        st.session_state['total_sum'] -= st.session_state[f'count_{index}']
        del st.session_state[f'count_{index}']

    # Reindex counters after deletion
    for i in range(index, len(st.session_state.counters)):
        if f'count_{i+1}' in st.session_state:
            st.session_state[f'count_{i}'] = st.session_state.pop(f'count_{i+1}', 0)


    update_sum()
    st.experimental_rerun()

def update_sum():
    st.session_state.sum = test.get_sum()

def reset_all():
    for i in range(len(st.session_state.counters)):
        test.reset(str(i))
    update_sum()
    st.experimental_rerun()


st.session_state.counters = sorted(st.session_state.counters, key=lambda x: st.session_state.get(f"count_{st.session_state.counters.index(x)}", x['initValue']), reverse=True)


if st.button("Add Counter"):
    st.session_state.show_popup = True


if st.session_state.show_popup:
    with st.form("add_counter_form"):
        title = st.text_input("Title")
        init_value = st.number_input("Initial Value", min_value=0, value=0)
        submitted = st.form_submit_button("Add ")
        if submitted:
            add_counter(title, init_value)


if st.button('Reset All'):
    reset_all()


for i, counter in enumerate(st.session_state.counters):
    col1, col2 = st.columns([4, 1])
    with col1:
        test.compteur(index=str(i), title=counter["title"], initvalue=int(counter["initValue"]))
    with col2:
        if st.button(f"Delete {counter['title']}", key=f"delete_{i}"):
            delete_counter(i)


st.write('Sum:', test.get_sum())
