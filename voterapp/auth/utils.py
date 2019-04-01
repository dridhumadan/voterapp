class CL:
    con_list = [('', 'Select Constituency'),
                ('KA01', 'Chikkodi'),
                ('KA02', 'Belagavi'),
                ('KA03', 'Bagalkot'),
                ('KA04', 'Bijapur'),
                ('KA05', 'Kalaburgi'),
                ('KA06', 'Raichur'),
                ('KA07', 'Bidar'),
                ('KA08', 'Koppal'),
                ('KA09', 'Bellary'),
                ('KA10', 'Haveri'),
                ('KA11', 'Dharwad'),
                ('KA12', 'Uttara Kannada'),
                ('KA13', 'Davangere'),
                ('KA14', 'Shimoga'),
                ('KA15', 'Udupi'),
                ('KA16', 'Hassan'),
                ('KA17', 'Dakshina Kannada'),
                ('KA18', 'Chitradurga'),
                ('KA19', 'Tumkur'),
                ('KA20', 'Mandya'),
                ('KA21', 'Mysore'),
                ('KA22', 'Chamarajnagar'),
                ('KA23', 'Bengaluru Rural'),
                ('KA24', 'Bengaluru North'),
                ('KA25', 'Bengaluru Central'),
                ('KA26', 'Bengaluru South'),
                ('KA27', 'Chikballapur'),
                ('KA28', 'Kolar')]


def generate_voter_id(cvid, ccode):
    num = int(cvid[4:7])
    num = num + 1
    newstr = str(num).zfill(3)
    vid = ccode + newstr
    return vid