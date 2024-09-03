from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "About me"
PAGE_ICON = ":wave:"
NAME = "Yumeth Bandara"
DESCRIPTION = """
I am an enthusiastic and tech-savvy 13-year-old high school student with a strong foundation in programming languages such as Python, Java, Kotlin, and web development basics (HTML, CSS, JavaScript). Passionate about ethical hacking and AI development. Skilled in project management, team collaboration, and problem-solving. Aspiring to build innovative technology solutions that make a positive impact on the world...
"""
EMAIL = "yumeth.bandara2010@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/yumeth-bandara-6380b4327/",
    "GitHub": "https://github.com/YB2456",
    "Email me": "mailto:yumeth.bandara2010@gmail.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("My skills")
st.write(
    """
I have a diverse skill set in technology, programming, and innovative thinking. I am proficient in Python programming and completed a 30-hour training program with a certification from ICITB. I am also familiar with web development technologies like HTML, CSS, and JavaScript and have experience in other languages like Kotlin, Java, and GD Script. I enjoy game development and have created a few games using the Godot Engine, which are available on platforms like Itch.io.

My technical expertise extends to ethical hacking and cybersecurity, where I have learned various techniques, including MITM, WPA/WPA2 cracking, packet sniffing, and more, using tools such as Wireshark, Nmap, and Kali Linux. I am also exploring Artificial Intelligence and Machine Learning, working with frameworks like TensorFlow and PyTorch to delve into deep learning, NLP, and predictive modeling.

I have experience in app development, having designed and developed a Progressive Web App (PWA) using Flutterflow. I’ve been involved in various projects, such as creating games and participating in the science fair at my school, where I secured a 2nd runners-up position in the "Renewable Energy" category by demonstrating a practical prototype.

My academic foundation includes education at international schools in Papua New Guinea before continuing at Lyceum. I have earned awards like the bronze and silver in UNICEF’s Mathletics competition. With a balanced profile of technical, academic, and creative pursuits, I aim to leverage my skills for future endeavors in technology and entrepreneurship.
"""
)

st.write('\n')
st.subheader("My projects, works and ambitions")
st.write(
    """
I am passionate about technology and community service. I’m leading a Maths Club fundraiser with a goal of raising Rs. 50,000 through a movie screening, ticket sales, and raffles. I’ve created a desktop app called CashFlowCompanion (CFC), which uses AI to help users manage their finances. I’m exploring mobile app development with Flutterflow and diving into Ethical Hacking and Cybersecurity, aiming to become the world’s youngest Certified Ethical Hacker (C|EH). My dreams include launching several companies: Krate for flying cars, Etron for phones and laptops, Nature1st for using technology to protect the environment, and Galaxy, a space exploration venture similar to SpaceX. Balancing my technical interests, I enjoy Math, Commerce, Programming, chess, and basketball.
    """
)