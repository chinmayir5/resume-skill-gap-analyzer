from skills import JOB_SKILLS
from utils import extract_text_from_pdf
from analyzer import analyze_resume

def main():
    print("\n==============================")
    print(" RESUME SKILL GAP ANALYZER ")
    print("==============================\n")

    # INPUT 1: Resume path
    resume_path = input("Enter FULL path to resume PDF: ").strip()

    # INPUT 2: Job role
    print("\nSelect Job Role:")
    roles = list(JOB_SKILLS.keys())
    for i, role in enumerate(roles, start=1):
        print(f"{i}. {role}")

    choice = int(input("\nEnter role number: "))
    selected_role = roles[choice - 1]

    # PROCESS
    resume_text = extract_text_from_pdf(resume_path)
    job_skills = JOB_SKILLS[selected_role]

    score, matched, high, medium, low = analyze_resume(resume_text, job_skills)

    # OUTPUT
    print("\n========== RESULT ==========")
    print(f"Job Role: {selected_role}")
    print(f"Match Score: {score}%\n")

    print("Matched Skills:")
    print(", ".join(matched) if matched else "None")

    print("\nMissing Skills:")
    print("  Core      :", ", ".join(high) if high else "None")
    print("  Secondary :", ", ".join(medium) if medium else "None")
    print("  Optional  :", ", ".join(low) if low else "None")
    print("============================")

if __name__ == "__main__":
    main()
