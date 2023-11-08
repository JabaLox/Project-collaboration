from app.Model.ReportModel import report
from app.Model.ViolationModel import Violation
from app.Model.database import *
import datetime
from flask import request, Blueprint, jsonify


report_bp = Blueprint('report', __name__)

@report_bp.route('/report/violation', methods=['GET'])
def get_violation():

    violation = db.session.query(Violation).all()

    return jsonify({
        "code": 200,
        "result": violation
    })