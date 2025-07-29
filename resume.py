from dataclasses import dataclass
from typing import List
import argparse

@dataclass
class Summary:
    description: str

@dataclass
class ContactInfo:
    name: str
    email: str
    phone: str
    linkedin: str
    github: str

@dataclass
class Project:
    title: str
    description: str

@dataclass
class SkillSection:
    title: str
    skills: List[str]

class Resume:
    def __init__(self):
        self.summary = None
        self.contact = None
        self.projects = []
        self.skills = []

    def set_contact(self, name, email, phone, linkedin, github):
        self.contact = ContactInfo(name, email, phone, linkedin, github)

    def set_summary(self, description):
        self.summary = Summary(description)

    def add_project(self, title, description):
        self.projects.append(Project(title, description))

    def add_skills(self, title, skills):
        self.skills.append(SkillSection(title, skills))

    def render(self):
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{self.contact.name}'s Resume</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        h1, h2 {{ color: #2c3e50; }}
        .section {{ margin-bottom: 30px; }}
        ul {{ padding-left: 20px; }}
    </style>
</head>
<body>
    <h1>{self.contact.name}</h1>
    <p>Email: {self.contact.email} | Phone: {self.contact.phone}</p>
    <p>LinkedIn: <a href="{self.contact.linkedin}">{self.contact.linkedin}</a> | GitHub: <a href="{self.contact.github}">{self.contact.github}</a></p>

    <div class="section">
        <h2>Summary</h2>
        <p>{self.summary.description}</p>
    </div>

    <div class="section">
        <h2>Projects</h2>
        <ul>
"""
        for p in self.projects:
            html += f"<li><strong>{p.title}</strong>: {p.description}</li>\n"
        html += """
        </ul>
    </div>

    <div class="section">
        <h2>Skills</h2>
"""
        for s in self.skills:
            html += f"<h3>{s.title}</h3><ul>\n"
            for sk in s.skills:
                html += f"<li>{sk}</li>\n"
            html += "</ul>\n"
        html += """
    </div>
</body>
</html>
"""
        return html

    def save(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.render())

def main():
    parser = argparse.ArgumentParser(description="Generate an HTML resume.")
    parser.add_argument("--output", type=str, default="resume.html", help="Output HTML file name")
    args = parser.parse_args()

    r = Resume()
    r.set_contact(
        name="Laksha Karimuthu",
        email="laksha@example.com",
        phone="+91-9876543210",
        linkedin="https://www.linkedin.com/in/laksha-karimuthu-3a815a299?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
        github="https://github.com/Laksha-python"
    )
    r.set_summary("Passionate and driven software engineer skilled in full-stack development, Python projects, and AI/ML applications. Strong focus on solving real-world problems through technology.")

    r.add_project("Reef Rescuers", "A Pygame-based interactive 2D coral reef conservation game with real-time gameplay, multiple coral types, and educational elements.")
    r.add_project("CVWizard", "A CLI-based Python tool to generate clean resumes in text and HTML formats.")
    r.add_project("AI Face Detector", "AI-vs-Human face detection model integrated with real-time webcam and screen capture.")
    r.add_project("Climate Dashboard", "Web dashboard visualizing CO2, temperature, sea level data using Python and Plotly.")
    r.add_skills("Programming", ["Python", "Java", "JavaScript", "HTML/CSS"])
    r.add_skills("Frameworks & Tools", ["Pygame", "JavaFX", "MongoDB", "Ursina Engine"])
    r.add_skills("AI/ML", ["Scikit-learn", "Face Detection", "Model Fine-tuning"])
    r.add_skills("Soft Skills", ["Problem Solving", "Team Collaboration", "Creative Thinking"])

    r.save(args.output)
    print(f"Resume saved to {args.output}")

if __name__ == "__main__":
    main()
