from pathlib import Path

import streamlit as st

from view.classical_user_study.criteria import CRITERIA
from view.classical_user_study.suggest import get_leaf_subfolders
from view.read import read_prompt_and_generated_quest


def save_current_answers(quest_path: Path, answers: dict[str, int]) -> None:
    pass


def get_current_answers() -> dict[str, int]:
    return {
        title: st.session_state[f"criterion_{idx}"]
        for idx, (title, _description, _scale) in enumerate(CRITERIA, start=1)
    }


def handle_next_click(quest_path: Path) -> None:
    answers = get_current_answers()
    save_current_answers(quest_path, answers)
    st.session_state["current_selection_position"] += 1
    st.rerun()


def render_classical_study() -> None:

    quests_root = Path(__file__).resolve().parents[1] / "resources" / "quests"
    leaf_subfolders = get_leaf_subfolders(quests_root)

    st.session_state.setdefault("current_selection_position", 0)

    selection_indices = st.session_state.get("selection_indices", [])
    current_selection_position = st.session_state["current_selection_position"]

    if selection_indices and current_selection_position >= len(selection_indices):
        st.toast("Больше квестов нет, спасибо за участие")
        st.session_state["prompt_context_text"] = ""
        st.session_state["generated_quest_text"] = ""
        return

        selected_quest_path: Path | None = None

    if selection_indices and leaf_subfolders:
        selected_index = selection_indices[current_selection_position]
        selected_quest_path = Path(leaf_subfolders[selected_index]) / "content.yaml"
        prompt_text, generated_quest_text = read_prompt_and_generated_quest(selected_quest_path)

        st.session_state["prompt_context_text"] = prompt_text
        st.session_state["generated_quest_text"] = generated_quest_text



    st.markdown(

        """
        <style>
        .criterion-card {
            padding: 0.25rem 0 0.75rem 0;
            border-bottom: 1px solid rgba(250, 250, 250, 0.12);
            margin-bottom: 0.75rem;
        }
        .criterion-title {
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }
        .criterion-description {
            font-size: 0.92rem;
            opacity: 0.85;
            margin-bottom: 0.4rem;
            line-height: 1.35;
        }
        .criterion-scale {
            font-size: 0.85rem;
            opacity: 0.7;
            margin-bottom: 0.3rem;
            font-style: italic;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    left_col, middle_col, right_col = st.columns([1.05, 1.05, 1.0], gap="small")

    with left_col:
        st.header("Промпт и контекст")
        st.text_area(
            label="Промпт и контекст",
            value=st.session_state.get("prompt_context_text", ""),
            height=650,
            key="prompt_context_text",
            label_visibility="collapsed",
            placeholder="Здесь отображается промпт и контекст исследования...",
        )


    with middle_col:
        st.header("Сгенерированный квест")
        st.text_area(
            label="Сгенерированный квест",
            value=st.session_state.get("generated_quest_text", ""),
            height=650,
            key="generated_quest_text",
            label_visibility="collapsed",
            placeholder="Здесь отображается сгенерированный квест...",
        )


    with right_col:
        st.header("Критерии оценки")
        
        if st.button("Далее", use_container_width=True, key="next_button_1"):
            if selected_quest_path is not None:
                handle_next_click(selected_quest_path)


        for idx, (title, description, scale) in enumerate(CRITERIA, start=1):
            st.markdown(
                f"""
                <div class="criterion-card">
                    <div class="criterion-title">{idx}. {title}</div>
                    <div class="criterion-description">{description}</div>
                    <div class="criterion-scale">({scale})</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.slider(
                label=title,
                min_value=1,
                max_value=10,
                value=5,
                key=f"criterion_{idx}",
                label_visibility="collapsed",
            )

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Далее", use_container_width=True, key="next_button_2"):
            if selected_quest_path is not None:
                handle_next_click(selected_quest_path)

