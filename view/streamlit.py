import random

import streamlit as st

from view.classical_user_study.render import render_classical_study


st.set_page_config(page_title="User Study", layout="wide")


if "user_random_number" not in st.session_state:
    st.session_state.user_random_number = random.randint(1, 1_000_000_000)


def main() -> None:
    instructions, classical_tab  = st.tabs(['Инструкция', 'Исследование'])

    with classical_tab:
        render_classical_study()


if __name__ == "__main__":
    main()


