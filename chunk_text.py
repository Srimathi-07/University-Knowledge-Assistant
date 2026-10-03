text = """
1. Minimum Attendance:
Students must maintain a minimum attendance of 75% in
each course to be eligible to attend the semester
examination.

2. Attendance Shortage:
Students whose attendance is below 75% may not be
eligible to appear for the semester examination.

3. Medical Leave:
Students with valid medical reasons may apply for
attendance consideration by submitting the required
medical documents to the university.
"""

chunks = text.split("\n\n")

for i, chunk in enumerate(chunks):
    print("CHUNK", i + 1)
    print(chunk.strip())
    print("----------------")