import streamlit as st

from view.classical_user_study.criteria import CRITERIA

def render_classical_study() -> None:
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
            value="",
            height=650,
            key="prompt_context_text",
            label_visibility="collapsed",
            placeholder="Здесь отображается промпт и контекст исследования...",
        )

    with middle_col:
        st.header("Сгенерированный квест")
        st.text_area(
            label="Сгенерированный квест",
            value="",
            height=650,
            key="generated_quest_text",
            label_visibility="collapsed",
            placeholder="Здесь отображается сгенерированный квест...",
        )

    with right_col:
        st.header("Критерии оценки")
        
        if st.button("Далее", use_container_width=True, key="next_button_1"):
            print(f"User random number: {st.session_state.user_random_number}")

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
            print(f"User random number: {st.session_state.user_random_number}")
