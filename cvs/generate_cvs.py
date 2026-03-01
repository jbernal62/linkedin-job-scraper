"""
Generates two ATS-friendly PDF CVs for Jefferson Gonzalez:
  1. DevOps / Cloud Architecture focus
  2. Data / AI focus

Usage:
    pip install fpdf2
    python cvs/generate_cvs.py
"""

import os

from fpdf import FPDF

from cv_data import (
    CERTIFICATIONS,
    EDUCATION,
    EXPERIENCE,
    LANGUAGES,
    PERSONAL_INFO,
    SKILLS_DATA_AI,
    SKILLS_DEVOPS,
    SUMMARY_DATA_AI,
    SUMMARY_DEVOPS,
)

BLUE = (27, 56, 100)
BLACK = (0, 0, 0)
DARK_GRAY = (51, 51, 51)
MARGIN_LEFT = 20
MARGIN_RIGHT = 20
LH = 5


class CVGenerator(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(MARGIN_LEFT, 15, MARGIN_RIGHT)

    def _reset_x(self):
        self.set_x(MARGIN_LEFT)

    def section_header(self, title: str):
        self.ln(4)
        self._reset_x()
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*BLUE)
        w = self.w - MARGIN_LEFT - MARGIN_RIGHT
        self.multi_cell(w, 7, title)
        y = self.get_y()
        self.set_draw_color(*BLUE)
        self.line(MARGIN_LEFT, y, self.w - MARGIN_RIGHT, y)
        self.ln(3)
        self._reset_x()

    def body_text(self, text: str):
        self._reset_x()
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*DARK_GRAY)
        w = self.w - MARGIN_LEFT - MARGIN_RIGHT
        self.multi_cell(w, LH, text)

    def bold_line(self, text: str, size=10):
        self._reset_x()
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*BLACK)
        w = self.w - MARGIN_LEFT - MARGIN_RIGHT
        self.multi_cell(w, LH + 1, text)

    def italic_line(self, text: str):
        self._reset_x()
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(*DARK_GRAY)
        w = self.w - MARGIN_LEFT - MARGIN_RIGHT
        self.multi_cell(w, LH, text)

    def bullet(self, text: str):
        self._reset_x()
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*DARK_GRAY)
        w = self.w - MARGIN_LEFT - MARGIN_RIGHT
        self.multi_cell(w, LH, f"  -  {text}")

    def small_text(self, text: str):
        self._reset_x()
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*DARK_GRAY)
        w = self.w - MARGIN_LEFT - MARGIN_RIGHT
        self.multi_cell(w, LH, text)

    def build_cv(self, profile: str, output_path: str):
        self.add_page()
        w = self.w - MARGIN_LEFT - MARGIN_RIGHT

        # --- Header ---
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(*BLACK)
        self.multi_cell(w, 12, PERSONAL_INFO["name"])

        title = PERSONAL_INFO["title_devops"] if profile == "devops" else PERSONAL_INFO["title_data_ai"]
        self._reset_x()
        self.set_font("Helvetica", "", 12)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(w, 6, title)

        self._reset_x()
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*DARK_GRAY)
        contact = f"{PERSONAL_INFO['location']}  |  {PERSONAL_INFO['email']}  |  {PERSONAL_INFO['phone']}"
        self.multi_cell(w, 5, contact)

        self._reset_x()
        self.set_text_color(*BLUE)
        links = f"GitHub: {PERSONAL_INFO['github']}  |  LinkedIn: {PERSONAL_INFO['linkedin']}"
        self.multi_cell(w, 5, links)

        # --- Summary ---
        self.section_header("Summary")
        summary = SUMMARY_DEVOPS if profile == "devops" else SUMMARY_DATA_AI
        self.body_text(summary)

        # --- Skills ---
        self.section_header("Skills & Technologies")
        skills = SKILLS_DEVOPS if profile == "devops" else SKILLS_DATA_AI
        for category, techs in skills.items():
            self._reset_x()
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(*DARK_GRAY)
            self.multi_cell(w, LH, f"{category}:")
            self._reset_x()
            self.set_font("Helvetica", "", 9)
            self.multi_cell(w, LH - 0.5, techs)
            self.ln(1)

        # --- Experience ---
        self.section_header("Experience")
        bullet_key = "bullets_devops" if profile == "devops" else "bullets_data_ai"

        freelance_roles = [e for e in EXPERIENCE if e.get("is_freelance")]
        regular_roles = [e for e in EXPERIENCE if not e.get("is_freelance")]

        for role in regular_roles:
            self.bold_line(f"{role['title']}  |  {role['company']}")
            self.italic_line(f"({role['dates']})  {role['location']}")
            for b in role.get(bullet_key, []):
                self.bullet(b)
            self.ln(2)

        # --- Freelance ---
        if freelance_roles:
            self.section_header("Freelance & Contract Projects")
            for role in freelance_roles:
                self.bold_line(f"{role['title']}  |  {role['company']}")
                self.italic_line(f"({role['dates']})  {role['location']}")
                for b in role.get(bullet_key, []):
                    self.bullet(b)
                self.ln(2)

        # --- Education ---
        self.section_header("Education")
        for edu in EDUCATION:
            self.bold_line(edu["degree"])
            self.small_text(f"{edu['institution']}  |  {edu['dates']}")
            self.ln(1)

        # --- Certifications ---
        self.section_header("Certifications")
        certs = list(CERTIFICATIONS)
        if profile == "data_ai":
            gen_ai = "Generative AI with Large Language Models - DeepLearning.AI"
            if gen_ai in certs:
                certs.remove(gen_ai)
                certs.insert(0, gen_ai)
        for cert in certs:
            self.bullet(cert)

        # --- Languages ---
        self.section_header("Languages")
        for lang, level in LANGUAGES:
            self.bullet(f"{lang} ({level})")

        self.output(output_path)
        print(f"Generated: {output_path}")


def main():
    out_dir = os.environ.get("CV_OUTPUT_DIR", os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(out_dir, exist_ok=True)

    devops_cv = CVGenerator()
    devops_cv.build_cv("devops", os.path.join(out_dir, "Jefferson_Gonzalez_DevOps_Cloud.pdf"))

    data_ai_cv = CVGenerator()
    data_ai_cv.build_cv("data_ai", os.path.join(out_dir, "Jefferson_Gonzalez_Data_AI.pdf"))


if __name__ == "__main__":
    main()
