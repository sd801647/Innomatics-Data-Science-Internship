from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "resources" / "styles" / "main.css"
profile_pic = current_dir / "resources" / "images" / "profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Resume | Subhamay Dhara"
PAGE_ICON = ":wave:"
NAME = "Subhamay Dhara"
DESCRIPTION = """
:pushpin: Tech Enthusiast | Developer | Student | Siemens-Scholar
"""
EMAIL = ":e-mail: sd801647@gmail.com"
SOCIAL_MEDIA = {
    "Website": "https://dharasubhamay.github.io/",
    "LinkedIn": "https://www.linkedin.com/in/subhamay-dhara-018b621a2",
    "GitHub": "https://github.com/dharasubhamay"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader(":rocket: Education")
st.write(":blue_book:", "**B.Tech in Computer Science and Engineering**")
st.write(":timer_clock: 07/2019 - Present")
st.success(
    """
- ► University : Maulana Abul Kalam Azad University of Technology, West Bengal
- ► Current Semester : 8th
- ► Avg. CGPA : 9.52
"""
)
st.write(":blue_book:", "**Higher Secondary**")
st.write(":timer_clock: 2016 - 2018")
st.success(
    """
- ► School : Paschimpara High School (H.S)
- ► Board : West Bengal Council of Higher Secondary Education
- ► Obtained Percentage : 91.60
"""
)
st.write(":blue_book:", "**Secondary**")
st.write(":timer_clock: 2015 - 2016")
st.success(
    """
- ► School : Paschimpara High School (H.S)
- ► Board : West Bengal Board of Secondary Education
- ► Obtained Percentage : 91.71
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader(":rocket: Skills")
st.error(
    """
- 👩‍💻 Programming: C • C++ • Python • HTML • CSS • Javascript • MATLAB • PHP
- 📊 Data Visulization: MS Excel
- 📚 Framework: Angular • ASP.NET Core • Bootstrap
- 🗄️ Databases: MySQL • SQL Server
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader(":rocket: Internship Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Science Intern | Innomatics Research Labs**")
st.write(":timer_clock: 02/2023 - Present")
st.warning(
    """
- ► Using Python
"""
)

# --- JOB 2
st.write("🚧", "**Software Developer Intern | Siemens Digital Industries Software**")
st.write(":timer_clock: 07/2022 - 09/2022")
st.warning(
    """
- ► Full Stack Web Developer
- ► Implementing Translation service in an Angular Project by Web API developed in ASP.NET Core.
- ► Built a Locale Management System from where Developers can provide Translation service in different projects.
- ► Technology Used : Angular, C#, Siemens Core UI, ASP.NET Core, Web API.
"""
)

# --- JOB 3
st.write("🚧", "**Summer Project Intern | Siemens**")
st.write(":timer_clock: 05/2021 - 08/2021")
st.warning(
    """
- ► Made an Appointment Management System for RT-PCR Test of Employees.
- ► Language/Technology Used : HTML, CSS, JS, PHP, MySQL.
"""
)

# --- Achievements ---
st.write('\n')
st.subheader(":rocket: Achievements")
st.success(
    """
- ✔️ 2018 - Student Of The Year
- ✔️ 2020 - Siemens Scholarship’ 2020
- ✔️ 2021 - President of CodeChef GCETTB Chapter
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader(":rocket: Projects & Accomplishments")
st.write("---")

st.write("🏆 **:red[Pointo - An Appointment Management System]**")
st.write("• Language/Technology Used : HTML, CSS, JS, PHP, MySQL.")
st.write("• During Covid-19 pandemic situation, every employee of each company needs to do RT-PCR Test. But standing in queue creates gathering and affect in work-time. So, we, 4 members in a group made a web based application for employees to take appointment in free time. Admin can give flexible days, times, counters for each test period. I implemented the Admin Dashboard portion.Admin can get total appointments of a particulartest period as well as in a single day, can add orremove employee name, delete appointment etc.")

st.write("🏆 **:red[My NoteBook App - An App to save personal notes]**")
st.write("• Language/Technology Used : Angular, Bootstrap, C#, ASP.NET Core, Web API, SQL Server")
st.write("• We can Add notes, Read notes, Update notes Delete notes by this Application.")

st.write("🏆 **:red[Multi Region Sales Analysis using Excel]**")
st.write("• Tool Used : Excel.")
st.write("• This is a project made in Excel and completed by me. Macro, Pivot table, Charts etc. are used in this project. Company can upload their sales report in differentregions and analysis their auto-generated report in Dashboard. It is well visible to anyone by used charts and different sections.")


st.write("---")