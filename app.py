
import streamlit as st
import pdfplumber
import os

st.set_page_config(page_title="Pankaj Kumar | AI Portfolio", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#050816,#0f172a,#111827);
color:white;
}
section[data-testid="stSidebar"]{
background:#020617;
}
.hero{
padding:35px;
border-radius:25px;
background:linear-gradient(90deg,#00E5FF,#7C3AED);
color:white;
text-align:center;
box-shadow:0 0 30px rgba(0,229,255,.3);
}
.card{
background:rgba(255,255,255,.06);
padding:20px;
border-radius:20px;
margin:10px 0;
border:1px solid rgba(255,255,255,.15);
}
.project{
background:linear-gradient(135deg,#111827,#1e293b);
padding:20px;
border-radius:20px;
margin-bottom:15px;
border-left:5px solid #00E5FF;
}
.tech{
display:inline-block;
padding:8px 14px;
margin:4px;
border-radius:20px;
background:#00E5FF;
color:black;
font-weight:bold;
}
h1,h2,h3,p,li,div,label{
color:white !important;
}
a{
color:#00E5FF !important;
}
</style>
""", unsafe_allow_html=True)

menu=st.sidebar.radio("🚀 Navigation",[
"Home","About","Experience","Skills","Projects",
"AI Playground","Resume","Contact"
])

if menu=="Home":

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        <div class="hero">
        <h1>🚀 Pankaj Kumar</h1>
        <h3>Data Analyst | Data Scientist | AI Engineer</h3>
        <p>
        Python • SQL • Power BI • Machine Learning • NLP • Automation
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Building AI-powered analytics solutions using
        Python, SQL, Machine Learning, NLP and Power BI.
        """)

    with col2:
        if os.path.exists("profile.jpg"):
            st.image("profile.jpg", width=280)
        else:
            st.warning("profile.jpg not found")

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Experience","3+ Years")

    with c2:
        st.metric("Projects","10+")

    with c3:
        st.metric("Technologies","15+")

    with c4:
        st.metric("Dashboards","20+")

    st.markdown("## 🌟 Highlights")

    st.info(
        "Building AI-powered solutions, dashboards, automation workflows and machine learning applications."
    )


elif menu=="About":

    st.header("👨‍💻 About Me")
    st.markdown("""
    Passionate Data Analyst and aspiring Data Scientist with expertise in:
    - Python
    - SQL
    - Power BI
    - Machine Learning
    - NLP
    - Power Apps
    - Automation
    """)

elif menu=="Experience":
    st.header("💼 Experience Timeline")

    exp=[
        ("Data Analyst","Jupitice Justice Technology","2025-Present"),
        ("Operations Analyst","Shriram Finance Limited","2024-2025"),
        ("Data Analyst","Zeoys Work-assist Pvt Ltd","2023-2024"),
        ("Data Scientist Intern","CSB Bank","2022")
    ]

    for role,company,period in exp:
        st.markdown(f"""
        <div class="card">
        <h3>{role}</h3>
        <p>{company}</p>
        <p>{period}</p>
        </div>
        """, unsafe_allow_html=True)

elif menu=="Skills":
    st.header("⚡ Technology Stack")

    skills=["Python","SQL","Power BI","Excel","Machine Learning","NLP",
            "TensorFlow","Scikit-Learn","AWS","Power Apps",
            "Power Automate","Django","Flask","Git","MySQL"]

    for s in skills:
        st.markdown(f'<span class="tech">{s}</span>',unsafe_allow_html=True)

elif menu=="Projects":
    st.header("🚀 Featured Projects")

    projects=[
        ("ATS Resume Analyzer","NLP based resume parsing and ATS scoring"),
        ("Job Recommender System","AI-powered recommendation engine"),
        ("Customer Segmentation","K-Means clustering analytics"),
        ("Customer Churn Prediction","ML classification model"),
        ("Litigation Analytics Dashboard","Business KPI monitoring"),
        ("Operational Dashboard","Power BI reporting solution")
    ]

    for title,desc in projects:
        st.markdown(f"""
        <div class="project">
        <h3>{title}</h3>
        <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif menu=="AI Playground":
    st.header("🤖 AI Playground")

    tab1,tab2=st.tabs(["ATS Analyzer","Loan Demo"])

    with tab1:
        uploaded=st.file_uploader("Upload Resume PDF",type=["pdf"])

        if uploaded:
            text=""

            try:
                with pdfplumber.open(uploaded) as pdf:
                    for page in pdf.pages:
                        t=page.extract_text()
                        if t:
                            text+=t

                skills=["python","sql","machine learning","power bi",
                        "nlp","excel","aws","tensorflow"]

                found=[]
                score=0

                for skill in skills:
                    if skill.lower() in text.lower():
                        found.append(skill)
                        score+=12

                score=min(score,100)

                st.success(f"ATS Score: {score}%")
                st.write("Detected Skills:", ", ".join(found))

            except Exception as e:
                st.error(str(e))

    with tab2:
        income=st.number_input("Monthly Income",0,500000,50000)

        if st.button("Predict Loan Eligibility"):
            if income>=50000:
                st.success("High Approval Probability")
            else:
                st.warning("Medium Approval Probability")

elif menu=="Resume":
    st.header("📄 Resume")

    if os.path.exists("resume.pdf"):
        with open("resume.pdf","rb") as f:
            st.download_button("Download Resume",f,"Pankaj_Kumar_Resume.pdf")
    else:
        st.warning("Place resume.pdf beside app.py")

elif menu=="Contact":
    st.header("📬 Contact")

    st.markdown("📧 pankaj.bharti1080@gmail.com")
    st.markdown("📱 9135857796")
    st.markdown("🔗 [LinkedIn](https://linkedin.com)")
    st.markdown("💻 [GitHub](https://github.com)")

    st.success("Open to Data Analyst, Data Scientist and AI opportunities.")
