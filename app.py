from flask import Flask, render_template, request
from faculty_list import faculty_members
app = Flask(__name__)
@app.route('/')
def home():
    return render_template(
        'index.html',
        faculty_list=faculty_members,
        search_term=""
    )
@app.route('/search')
def search():
    search_term = request.args.get('search', '').lower()
    department_filter = request.args.get('department', '')
    results = []
    for faculty in faculty_members:
        matches_search = (
            search_term == "" or
            search_term in faculty['name'].lower() or
            search_term in faculty['department'].lower() or
            any(search_term in skill.lower() for skill in faculty['expertise'])
        )
        matches_department = (
            department_filter == "" or
            faculty['department'] == department_filter
        )
        if matches_search and matches_department:
            results.append(faculty)
    return render_template(
        'index.html',
        faculty_list=results,
        search_term=search_term
    )
if __name__ == '__main__':
    print("Starting Faculty Expertise Finder...")
    app.run(debug=True)