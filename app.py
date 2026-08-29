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
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    .main {
        background-color: #f7f7f5;
    }
    .court-title {
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    .court-subtitle {
        text-align: center;
        color: #666;
        font-size: 16px;
        margin-bottom: 30px;
    }
    .legal-box {
        background: white;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #ddd;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }
    .case-number {
        text-align: right;
        color: #777;
        font-size: 13px;
    }
    .charge {
        padding: 12px 15px;
        background: #fafafa;
        border-left: 4px solid #333;
        margin: 10px 0;
        border-radius: 5px;
    }
    .verdict {
        text-align: center;
        padding: 25px;
        background: #fff;
        border-radius: 12px;
        border: 2px solid #222;
        margin-top: 25px;
    }
    .big-wish {
        text-align: center;
        font-size: 30px;
        font-weight: 800;
        margin-top: 20px;
    }
    .small-note {
        text-align: center;
        color: #777;
        font-size: 14px;
    }
    .captcha-title {
        text-align: center;
        font-size: 35px;
        font-weight: 800;
        margin-top: 80px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# LOCKED STATE
# ============================================================

if not st.session_state.unlocked:

    st.markdown(
        '<div class="captcha-title">🔐 SECURITY CLEARANCE REQUIRED</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center;color:#777;">
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
    st.caption("⚠️ Unauthorized access will be reported to the imaginary Registrar.")
    st.stop()


# ============================================================
# UNLOCKED STATE (MAIN LEGAL DOCUMENT)
# ============================================================

st.markdown(
    '<div class="court-title">⚖️ HIGH COURT OF BENGALURU</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="court-subtitle">SPECIAL BIRTHDAY BENCH • CLASSIFIED CASE FILE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="legal-box">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="case-number">CASE NO. 21/2026 • BIRTHDAY BENCH</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <h2 style="text-align:center;">
    HIGH COURT OF BENGALURU<br>
    SPECIAL BIRTHDAY DECREE
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown("""
### 👩‍⚖️ IN THE MATTER OF:

**The State of Junior Affairs**  
**Vs.**  
**Harshiii, Age 21**

---

### 🧑‍⚖️ DEFENDANT

**Name:** Harshiii  
**Age:** 21  
**Occupation:** Law Student / Intern  
**Current Status:** Suspiciously senior.

---

### 📜 CHARGES FILED

<div class="charge">
<b>Charge 1 — Section 420</b><br>
Scamming an innocent junior out of a promised coffee.
</div>

<div class="charge">
<b>Charge 2 — Section 420.1</b><br>
Fleeing the scene immediately after asking for flowers.
</div>

<div class="charge">
<b>Charge 3 — Section 420.2</b><br>
Unlawful intimidation for scolding of an innocent & cute junior.
</div>

<div class="charge">
<b>Charge 4 — Special Provision</b><br>
Being unnecessarily cute while pretending to be extremely serious.
</div>

---

### 🔎 EVIDENCE ON RECORD

**Exhibit A:** The coffee that was promised but never delivered. ☕  
**Exhibit B:** Flowers are wating to presente to the accused. 🌷  
**Exhibit C:** scolding the inocent pyara cute junior.  
**Exhibit D:** Witness testimony confirming that the accused melts over puppies. 🐶

---

### ⚖️ OBSERVATION OF THE COURT

After carefully examining the evidence, the Court finds that the accused is:

> **Guilty of being 21, unnecessarily adorable, and extremely difficult to impress.**

However, considering the accused's birthday, the Court is inclined to show mercy.

""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# VERDICT
# ============================================================

st.markdown(
    """
    <div class="verdict">
        <h2>⚖️ FINAL VERDICT</h2>
        <p>
        order enandre: ivatthu full khushiyagi irbeku, sakkath aagi thindu enjoy madbeku. 
        and please, ondh dina aadru innocent juniors ge baiyodu nilsi boss 😂
        </p>
        <p>
        <b>Further proceedings are suspended until coffee is produced.</b> ☕
        </p>
    </div>
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

    st.markdown(
        '<div class="big-wish">🎉 HAPPY 21ST HARSHIII! 🎉</div>',
        unsafe_allow_html=True
    )

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
        st.info("🐶 Exhibit E (puppy_pic.jpg) is currently unavailable. The Court suspects the puppies are on recess.")

    st.success(
        "happy 21st harshiii ✨ pls don't run away from this website like u ran away from the flowers 😂 "
        "have a good one senior, u still owe me that treat"
    )
    
    st.markdown(
        """
        <p class="small-note">
        — From your favourite junior (allegedly) ⚖️
        </p>
        """,
        unsafe_allow_html=True
    )
