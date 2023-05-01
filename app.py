from flask import Flask, render_template, request

app = Flask(__name__)

class Employee:
    def __init__(self, name, attendance, work_output, quality, teamwork, communication, work_ethic):
        self.name = name
        self.attendance = attendance
        self.work_output = work_output
        self.quality = quality
        self.teamwork = teamwork
        self.communication = communication
        self.work_ethic = work_ethic

    def calculate_score(self):
        score = 0

        # Attendance
        if self.attendance < 0.1:
            score += 20
        elif self.attendance < 0.2:
            score += 15
        elif self.attendance < 0.3:
            score += 10
        elif self.attendance < 0.4:
            score += 5

        # Work Output
        if self.work_output > 100:
            score += 20
        elif self.work_output > 80:
            score += 15
        elif self.work_output > 60:
            score += 10
        elif self.work_output > 40:
            score += 5

        # Quality of Work
        if self.quality > 90:
            score += 20
        elif self.quality > 80:
            score += 15
        elif self.quality > 70:
            score += 10
        elif self.quality > 60:
            score += 5

        # Teamwork
        if self.teamwork > 90:
            score += 20
        elif self.teamwork > 80:
            score += 15
        elif self.teamwork > 70:
            score += 10
        elif self.teamwork > 60:
            score += 5

        # Communication
        if self.communication > 90:
            score += 20
        elif self.communication > 80:
            score += 15
        elif self.communication > 70:
            score += 10
        elif self.communication > 60:
            score += 5

        # Work Ethic
        if self.work_ethic > 90:
            score += 20
        elif self.work_ethic > 80:
            score += 15
        elif self.work_ethic > 70:
            score += 10
        elif self.work_ethic > 60:
            score += 5

        return score

    def get_feedback(self):
        score = self.calculate_score()

        if score > 90:
            feedback = f"{self.name}'s performance was exceptional!"
        elif score > 80:
            feedback = f"{self.name}'s performance was very good!"
        elif score > 70:
            feedback = f"{self.name}'s performance was good."
        elif score > 60:
            feedback = f"{self.name}'s performance was satisfactory."
        else:
            feedback = f"{self.name}'s performance needs improvement."

        return feedback


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        attendance = float(request.form['attendance'])
        work_output = int(request.form['work_output'])
        quality = int(request.form['quality'])
        teamwork = int(request.form['teamwork'])
        communication = int(request.form['communication'])
        work_ethic = int(request.form['work_ethic'])
        employee = Employee(name, attendance, work_output, quality, teamwork, communication, work_ethic)

        feedback = employee.get_feedback()

        return render_template('result.html', feedback=feedback)

    return render_template('form.html')

if __name__== '__main__':
    app.run(debug=True)