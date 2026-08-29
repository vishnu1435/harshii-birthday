import streamlit as st
from PIL import Image

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Harshiii v. The Junior",
    page_icon="⚖️",
    layout="centered",
)

# ============================================================
# SESSION STATE
# ============================================================

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if "verdict_accepted" not in st.session_state:
    st.session_state.verdict_accepted = False


# ============================================================
# LOCKED STATE
# ============================================================

if not st.session_state.unlocked:

    st.markdown("<h2 style='text-align:center;'>🔐 SECURITY CLEARANCE REQUIRED</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align:center;color:gray;">
        HIGH COURT OF BENGALURU — Restricted Birthday File<br>
        Identity verification required before accessing classified material.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    with st.container(border=True):
        st.subheader("⚖️ Identity Verification")
        st.caption("Only the actual accused party should be able to pass this test.")

        q1 = st.radio(
            "Security Question — What is the appropriate response when someone brings you flowers at the High Court?",
            ["Say thank you politely", "Running behind the senior"],
            index=None
        )

        st.write("")

        unlock = st.button(
            "🔓 Unlock Classified Birthday File",
            use_container_width=True,
            type="primary"
        )

        if unlock:
            if q1 == "Running behind the senior":
                st.session_state.unlocked = True
                st.rerun()
            else:
                st.error("Liar. Try again.")

    st.write("")
    st.markdown("<p style='text-align:center;color:gray;font-size:12px;'>⚠️ Unauthorized access will be reported to the imaginary Registrar.</p>", unsafe_allow_html=True)
    st.stop()


# ============================================================
# UNLOCKED STATE (MAIN LEGAL DOCUMENT)
# ============================================================

st.markdown("<h1 style='text-align:center;'>⚖️ HIGH COURT OF BENGALURU</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>SPECIAL BIRTHDAY BENCH • CLASSIFIED CASE FILE</p>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("<p style='text-align:right;color:gray;font-size:12px;'>CASE NO. 21/2026 • BIRTHDAY BENCH</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center;'>SPECIAL BIRTHDAY DECREE</h2>", unsafe_allow_html=True)
    
    st.divider()

    st.markdown("### 👩‍⚖️ IN THE MATTER OF:\n**The State of Junior Affairs**  \n**Vs.**  \n**Harshiii, Age 21**")
    
    st.divider()

    st.markdown("### 🧑‍⚖️ DEFENDANT\n**Name:** Harshiii  \n**Age:** 21  \n**Occupation:** Law Student / Intern  \n**Current Status:** Suspiciously senior.")
    
    st.divider()

    st.markdown("### 📜 CHARGES FILED")
    
    st.error("**Charge 1 — Section 420**  \nScamming an innocent junior out of a promised coffee.")
    st.error("**Charge 2 — Section 420.1**  \nFleeing the scene immediately after asking for flowers.")
    st.error("**Charge 3 — Section 420.2**  \nUnlawful intimidation for scolding of an innocent & cute junior.")
    st.error("**Charge 4 — Special Provision**  \nBeing unnecessarily cute while pretending to be extremely serious.")
    
    st.divider()

    st.markdown("### 🔎 EVIDENCE ON RECORD")
    
    st.markdown("**Exhibit A:** The coffee that was promised but never delivered. ☕")
    st.markdown("**Exhibit B:** Flowers are waiting to be presented to the accused. 🌷")
    st.markdown("**Exhibit C:** Scolding the innocent pyara cute junior.")
    st.markdown("**Exhibit D:** Witness testimony confirming that the accused melts over puppies. 🐶")
    
    st.divider()

    st.markdown("### ⚖️ OBSERVATION OF THE COURT")
    st.info("After carefully examining the evidence, the Court finds that the accused is:\n\n> **Guilty of being 21, unnecessarily adorable, and extremely difficult to impress.**\n\nHowever, considering the accused's birthday, the Court is inclined to show mercy.")

st.write("")

# ============================================================
# VERDICT
# ============================================================

with st.container(border=True):
    st.markdown("<h2 style='text-align:center;'>⚖️ FINAL VERDICT</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align:center;'>
        order enandre: ivatthu full khushiyagi irbeku, sakkath aagi thindu enjoy madbeku. 
        and please, ondh dina aadru innocent juniors ge baiyodu nilsi boss 😂
        </p>
        <p style='text-align:center;'>
        <b>Further proceedings are suspended until coffee is produced.</b> ☕
        </p>
        """,
        unsafe_allow_html=True
    )

st.write("")

if not st.session_state.verdict_accepted:
    if st.button("🎂 ACCEPT VERDICT & UNLOCK TRUE BIRTHDAY WISH", use_container_width=True, type="primary"):
        st.session_state.verdict_accepted = True
        st.balloons()
        st.rerun()

# ============================================================
# FINAL BIRTHDAY REVEAL
# ============================================================

if st.session_state.verdict_accepted:
    st.divider()

    st.markdown("<h1 style='text-align:center;'>🎉 HAPPY 21ST HARSHIII! 🎉</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <p style="text-align:center;font-size:18px;">
        The Court has officially concluded that the strict senior
        actually has a soft side. ❤️
        </p>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # Puppy Image
    # --------------------------------------------------------
    try:
        puppy = Image.open("puppy_pic.jpg")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(puppy, caption="Exhibit E — The only witnesses the Court trusts.", use_container_width=True)
    except Exception:
        st.warning("🐶 Exhibit E is missing! Double check that the file on GitHub is named EXACTLY 'puppy_pic.jpg' with no capital letters or double extensions.")

    st.success(
        "happy 21st harshiii ✨ pls don't run away from this website like u ran away from the flowers 😂 "
        "have a good one senior, u still owe me that treat"
    )
    
    st.markdown(
        """
        <p style="text-align:center;color:gray;">
        — From your favourite junior (allegedly) ⚖️
        </p>
        """,
        unsafe_allow_html=True
    )
