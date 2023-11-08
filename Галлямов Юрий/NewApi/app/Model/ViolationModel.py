from app.Model.database import db
from app.Model.ReportModel import report

class Violation(db.Model):
    ID_Violation = db.Column(db.Integer, primary_key=True, nullable=False)
    Title_Violation = db.Column(db.String, nullable=False)

    # Определение отношения
    reports = db.relationship('report', backref='violation', lazy='dynamic', foreign_keys='report.ID_Violation')
