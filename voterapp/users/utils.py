from voterapp.models import Voter, Constituency, Candidate
from flask_login import current_user

def getResultData():
    c_code = current_user.const_code
    candidates = Candidate.query.filter_by(const_code = c_code).all()

    cand_ids = []
    
    for cand in candidates:
        cand_ids.append(cand.cand_id)
    cand_ids.append('CKAXXNO')
    cand_ids.append('Not Voted')
    
    votes = {}
    voters = Voter.query.filter_by(const_code = c_code).all()

    for cid in cand_ids:
        votes[cid] = 0

    for voter in voters:
        if voter.cand_id is None:
                votes['None'] += 1
        for cid in cand_ids:
            if voter.cand_id == cid:
                votes[cid] += 1
    
    return votes
