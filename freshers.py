import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Freshers Job Portal", page_icon="💼", layout="wide")

st.markdown(
    """
    <style>
    body {
        background: radial-gradient(circle at top left, #dbe9ff 0%, #f8fbff 35%, #ffffff 100%);
    }
    .hero-section {
        border-radius: 32px;
        padding: 34px;
        margin-bottom: 28px;
        background: linear-gradient(135deg, #ffffff 0%, #d7e8ff 45%, #bfd9ff 100%);
        box-shadow: 0 28px 70px rgba(39, 108, 218, 0.16);
        transform: perspective(1200px) rotateX(1deg);
    }
    .hero-title { font-size: 3rem; color: #0b3161; font-weight: 900; margin-bottom: 0.6rem; }
    .hero-subtitle { font-size: 1.15rem; color: #214a84; line-height: 1.7; }
    .job-card {
        border-radius: 28px;
        padding: 24px;
        margin-bottom: 24px;
        background: linear-gradient(180deg, #ffffff 0%, #eef4ff 100%);
        box-shadow: 0 22px 45px rgba(27, 79, 164, 0.14);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }
    .job-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 32px 60px rgba(27, 79, 164, 0.23);
    }
    .job-header { color: #0e3772; font-size: 1.4rem; font-weight: 800; margin-bottom: 12px; }
    .job-badges span {
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 10px;
        padding: 9px 16px;
        border-radius: 20px;
        font-size: 0.94rem;
        font-weight: 700;
    }
    .badge-remote { background: #e7f1ff; color: #114d95; }
    .badge-fulltime { background: #e6fbf0; color: #1e7c42; }
    .badge-intern { background: #fff6e8; color: #b56700; }
    .badge-contract { background: #f4ebff; color: #5f39a6; }
    .job-image { border-radius: 22px; width: 100%; height: auto; object-fit: cover; margin-bottom: 18px; }
    .application-card {
        border-radius: 22px;
        background: linear-gradient(180deg, #f9fbff 0%, #e9f1ff 100%);
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 16px 32px rgba(24, 76, 158, 0.1);
    }
    .sidebar .stTextInput>div>div>input,
    .sidebar .stSelectbox>div>div>div>select,
    .sidebar .stButton>button {
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

jobs =[
    {
        "id": 1,
        "title": "Junior Software Engineer",
        "company": "TechLaunch",
        "location": "Remote",
        "type": "Full-time",
        "description": "Build web features, work with mentors, and learn Python/JavaScript on real projects.",
        "image": "https://media.geeksforgeeks.org/wp-content/uploads/20240524191901/The-Struggles-of-a-Junior-Software-Developer.webp",
    },
    {
        "id": 2,
        "title": "Graduate Data Analyst",
        "company": "Insight Labs",
        "location": "Bangalore",
        "type": "Internship",
        "description": "Analyze datasets, create dashboards, and support business decisions with clean reports.",
        "image": "https://tse3.mm.bing.net/th/id/OIP.xv0hgpiszhKshxCtwMz3OwHaEU?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
    },
    {
        "id": 3,
        "title": "Entry-Level UI/UX Designer",
        "company": "DesignNest",
        "location": "Delhi",
        "type": "Contract",
        "description": "Design wireframes, prototypes, and collaborate with product and development teams.",
        "image": "https://th.bing.com/th/id/OIP.clLrArcPvkTUjsSpzPkOWwHaE8?w=289&h=193&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    },
    {
        "id": 4,
        "title": "Customer Support Executive",
        "company": "HelpWave",
        "location": "Hyderabad",
        "type": "Full-time",
        "description": "Support freshers hiring drives, resolve candidate queries, and manage onboarding workflows.",
        "image": "https://th.bing.com/th/id/OIP.xv0hgpiszhKshxCtwMz3OwHaEU?w=257&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    },
    {
       "id": 5,
              "title": "Frontend Developer",
              "company": "CodeCrafters",
              "location": "Bangalore",
              "type": "Full-time",
              "description": "Develop responsive UI using HTML, CSS, JavaScript and React.",
              "image": "https://th.bing.com/th/id/OIP.BpI22bamwP6rGBh0bzQiKQHaD8?w=264&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",  
    },
    {
           "id": 6,
                  "title": "Backend Developer",
                  "company": "DataForge",
                  "location": "Hyderabad",
                  "type": "Full-time",
                  "description": "Build APIs using Pyhton/Django and manage databases.",
                  "image": "https://th.bing.com/th/id/OIP.0iOAPCEg3YVFNcdFLPuIQgHaHa?w=184&h=184&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",  
    },
    {
        "id":7,
        "title":"AI/ML Intern",
        "company":"NextGen AI",
        "location":"Remote",
        "type":"Internship",
        "description":"Work on machine learning models, data preprocessing, and model evaluation.",
        "image":"https://th.bing.com/th/id/OIP.StqXNK1niiqKwyAjRp-EFgAAAA?w=230&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    },
    {
        "id":8,
        "title":"Software Tester",
        "company":"QualityWorks",
        "location":"Chennai",
        "type":"Contract",
        "description":"Perform manual and automated testing of applications.",
        "image":"https://th.bing.com/th/id/OIP.SSqPy3C7B1l8BOPl4Fw7uQHaFN?w=229&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    },
]

if "applications" not in st.session_state:
    st.session_state["applications"] = []

st.markdown(
    """
    <div class="hero-section">
        <div class="hero-title">Freshers Job Portal 💼</div>
        <div class="hero-subtitle">
            Discover vibrant entry-level roles, apply instantly, and impress hiring teams with every click.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 🔎 Find Jobs")
    keyword = st.text_input("Search keyword", placeholder="e.g. Software, Data, Design")
    location = st.selectbox(
        "Location",
        options=["All"] + sorted({job["location"] for job in jobs}),
    )
    job_type = st.selectbox(
        "Job type",
        options=["All"] + sorted({job["type"] for job in jobs}),
    )
    st.markdown("---")
    st.markdown("### 📌 Posted jobs")
    st.write(f"**{len(jobs)} opportunities available**")

def filter_jobs(job_list, keyword="", location="All", job_type="All"):
    filtered = []
    keyword_lower = keyword.strip().lower()
    for job in job_list:
        match_keyword = (
            keyword_lower == ""
            or keyword_lower in job["title"].lower()
            or keyword_lower in job["company"].lower()
            or keyword_lower in job["description"].lower()
        )
        match_location = location == "All" or job["location"] == location
        match_type = job_type == "All" or job["type"] == job_type
        if match_keyword and match_location and match_type:
            filtered.append(job)
    return filtered

filtered_jobs = filter_jobs(jobs, keyword, location, job_type)

if not filtered_jobs:
    st.warning("No jobs match your search. Try a different keyword or filter.")
else:
    for job in filtered_jobs:
        badge_class = {
            "Full-time": "badge-fulltime",
            "Internship": "badge-intern",
            "Contract": "badge-contract",
        }.get(job["type"], "badge-remote")

        with st.container():
            st.markdown(
                f"""
                <div class="job-card">
                    <div class="job-header">✨ {job['title']} — {job['company']}</div>
                    <img class="job-image" src="{job['image']}" alt="{job['title']}">
                    <div class="job-badges" style="margin-top: 16px;">
                        <span class="badge-remote">📍 {job['location']}</span>
                        <span class="{badge_class}">🧾 {job['type']}</span>
                    </div>
                    <div style="color: #23396b; line-height: 1.8; margin-top: 16px;">
                        {job['description']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            with st.expander("📝 Apply for this job"):
                with st.form(key=f"apply_form_{job['id']}"):
                    name = st.text_input("Full name", key=f"name_{job['id']}")
                    email = st.text_input("Email address", key=f"email_{job['id']}")
                    resume = st.text_input(
                        "Resume link or LinkedIn profile",
                        placeholder="https://",
                        key=f"resume_{job['id']}",
                    )
                    submitted = st.form_submit_button("Submit application")

                    if submitted:
                        if not name or not email or not resume:
                            st.error("Please fill in all fields before applying.")
                        else:
                            st.session_state.applications.append(
                                {
                                    "job_id": job["id"],
                                    "job_title": job["title"],
                                    "company": job["company"],
                                    "name": name,
                                    "email": email,
                                    "resume": resume,
                                    "applied_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                }
                            )
                            st.success("✅ Application submitted successfully!")
                            st.info("Your application has been recorded for review.")

st.markdown("---")
st.markdown("## 📄 Recent Applications")
if st.session_state.applications:
    for app in reversed(st.session_state.applications[-5:]):
        st.markdown(
            f"""
            <div class="application-card">
                <strong>👤 {app['name']}</strong> applied for
                <strong>{app['job_title']}</strong> at <strong>{app['company']}</strong><br>
                <small>🕒 {app['applied_at']}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.info("No applications submitted yet. Apply to a job to see it appear here.")
