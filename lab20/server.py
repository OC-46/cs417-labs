"""Lab 20: Build the Other Side — Server

Your FastAPI grading server. Build each section as you work
through the tasks. The TODOs tell you what to add and where.
"""

from fastapi import FastAPI
from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse

app = FastAPI()


# ---------------------------------------------------------------------------
# Task 1: The Naive Server
# ---------------------------------------------------------------------------
# Import the grade function from grading.py, then create a POST /grade
# endpoint that accepts {"student": ..., "lab": ...} and returns the score.

# TODO: import grade from grading
import grading

# TODO: POST /grade endpoint
@app.post("/grade")
def grade_endpoint(request: dict):
    student = request["student"]
    lab = request["lab"]
    score = grading.grade(student, lab)
    return {"student": student, "lab": lab, "score": score}


# ---------------------------------------------------------------------------
# Task 2: Retries Reveal a Problem
# ---------------------------------------------------------------------------
# Add a grading_log list that records every grading event.
# Update POST /grade to (1) accept an optional "slow" field and pass it
# to grade(), and (2) append each grading event to the log.
# Add GET /log and POST /reset-log endpoints.

# TODO: grading_log = []
grading_log = []

# TODO: update POST /grade to log events and support "slow"
@app.post("/grade")
def grade_endpoint(request: dict):
    student = request["student"]
    lab = request["lab"]
    slow = request.get("slow", False)
    score = grading.grade(student, lab, slow=slow)
    grading_log.append({"student": student, "lab": lab})
    return {"student": student, "lab": lab, "score": score}

# TODO: GET /log endpoint
@app.get("/log")
def get_log():
    return {"entries": grading_log}

# TODO: POST /reset-log endpoint
@app.post("/reset-log")
def reset_log():
    grading_log.clear()
    return {"entries": grading_log}

# ---------------------------------------------------------------------------
# Task 3: Idempotency Makes Retries Safe
# ---------------------------------------------------------------------------
# Add a completed dict that maps submission IDs to results.
# Update POST /grade to check for an optional "submission_id" field —
# if the ID is already in completed, return the cached result without
# grading again or logging.
# Add POST /reset-completed endpoint.

# TODO: completed = {}
completed = {}

# TODO: update POST /grade to check submission_id
@app.post("/grade")
def grade_endpoint(request: dict):
    student = request["student"]
    lab = request["lab"]
    slow = request.get("slow", False)
    submission_id = request.get("submission_id")

    if submission_id and submission_id in completed:
        return completed[submission_id]

    score = grading.grade(student, lab, slow=slow)
    result = {"student": student, "lab": lab, "score": score}
    grading_log.append({"student": student, "lab": lab})
    if submission_id:
        completed[submission_id] = result
    return result

# TODO: POST /reset-completed endpoint
@app.post("/reset-completed")
def reset_completed():
    completed.clear()
    return {"completed": completed}



# ---------------------------------------------------------------------------
# Task 4: Honest About Time
# ---------------------------------------------------------------------------
# You'll need: from fastapi import BackgroundTasks
#              from fastapi.responses import JSONResponse
#
# Add jobs dict, job_submission_map dict, and a job ID generator.
# Create POST /grade-async (returns 202, runs grading in background).
# Create a run_grade_job helper that does the actual grading.
# Create GET /grade-jobs/{job_id} to check job status.

# TODO: jobs = {}
jobs = {}
# TODO: job_submission_map = {}
job_submission_map = {}
# TODO: POST /grade-async endpoint
@app.post("/grade-async")
def grade_async(request: dict, background_tasks: BackgroundTasks):
    student = request["student"]
    lab = request["lab"]
    submission_id = f"{student}-lab{lab}"
    job_id = f"job-{len(jobs) + 1}"
    job_submission_map[job_id] = submission_id
    background_tasks.add_task(run_grade_job, student, lab, submission_id, job_id)
    return JSONResponse(status_code=202, content={"status": "accepted", "job_id": job_id})

# TODO: run_grade_job helper function
def run_grade_job(student: str, lab: int, submission_id: str, job_id: str):
    import time
    time.sleep(3)  # Simulate long grading time
    score = grading.grade(student, lab)
    result = {"student": student, "lab": lab, "score": score}
    jobs[job_id] = {"status": "complete", "result": result}
# TODO: GET /grade-jobs/{job_id} endpoint
@app.get("/grade-jobs/{job_id}")
def get_grade_job(job_id: str):
    if job_id not in jobs:
        return JSONResponse(status_code=404, content={"error": "job not found"})
    return jobs[job_id]