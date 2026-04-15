import random
from pathlib import Path

import streamlit as st

from view.classical_user_study.render import render_classical_study
from view.classical_user_study.suggest import get_leaf_subfolders, prepare_selection

st.set_page_config(page_title="User Study", layout="wide")

if "selection_indices" not in st.session_state:
    quests_root = Path(__file__).resolve().parent / "resources" / "quests"
    leaf_subfolders = get_leaf_subfolders(quests_root)
    st.session_state.selection_indices = prepare_selection(leaf_subfolders)


def main() -> None:
    instructions, classical_tab  = st.tabs(['Инструкция', 'Исследование'])

    with classical_tab:
        render_classical_study()


if __name__ == "__main__":
    main()


