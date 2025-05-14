import joblib
import streamlit as st

# ---------- Load the trained pipeline ----------
clf = joblib.load("spam_pipeline.pkl")

# ---------- GUI ----------
st.set_page_config(page_title="Spam-Mail Classifier")
st.title("📧 Spam-Mail Classifier")

user_text = st.text_area(
    "Paste the email text here:",
    height=200,
    placeholder="e.g. \"Congratulations! You’ve won a free cruise…\""
)

if st.button("Classify"):
    if not user_text.strip():
        st.warning("Please enter some text first ✍️")
    else:
        pred = clf.predict([user_text])[0]          # 0 = spam, 1 = ham 
        label = "🚫  Spam" if pred == 0 else "✅  Legitimate / ham"
        st.success(f"Result: **{label}**")
