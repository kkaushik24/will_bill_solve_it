from constants import TAGS, SKILLS, USER_TYPE
levels = ['', 'E', 'E-M', 'M', 'M-H', 'H']

# read training set

# read training/problems.csv

tr_problems_file = open('train/problems.csv')
tr_problems_data = tr_problems_file.read()
rows_tr_problems_data = tr_problems_data.split('\n')
tr_problems_txt = open('tr_problems.txt', 'w')
tr_data = ''
d = {}
level=[]
tags = TAGS
for k,row in enumerate(rows_tr_problems_data):
    if k==0:
        row_list = row.split(',')
        print row_list[0],row_list[2],row_list[3],row_list[4],row_list[5]
    elif k < len(rows_tr_problems_data)-1:
        row_list = row.split(',')
        print row_list
        problem_id, level, accuracy, solved_count, error_count,rating, tag1, tag2, tag3, tag4, tag5 = row_list
        t1 = tags.index(tag1) + 1
        t2 = 1 + tags.index(tag2)
        t3 = 1 + tags.index(tag3)
        t4 = 1 + tags.index(tag4)
        t5 = 1 + tags.index(tag5)
        lev = levels.index(level) + 1
        d.update({problem_id: [accuracy, solved_count, error_count,lev,t1,t2, t3,t4,t5]})

# read training/users.csv

tr_users_file = open('train/users.csv')
tr_users_data = tr_users_file.read()
rows_tr_users_data = tr_users_data.split('\n')
tr_users_txt = open('tr_users.txt', 'w')
tr_data = ''
du = {}
sk = []
for k,row in enumerate(rows_tr_users_data):
    if k==0:
        row_list = row.split(',')
        print row_list[0],row_list[2],row_list[3]
    elif k < len(rows_tr_users_data)-1:
        row_list = row.split(',')
        rl = row_list
        user_id, skills, solved_count, attempts, user_type = rl
        ski = 1
        for skill in skills:
            try: 
                ski = ski * (SKILLS.index(skill)+1)
            except:
                pass
        u_t = USER_TYPE.index(user_type) +1
            
        du.update({user_id: [solved_count, attempts, ski,u_t]})
print len(du.keys())

# read training/submissions.csv

tr_sub_file = open('train/submissions.csv')
tr_sub_data = tr_sub_file.read()
rows_tr_sub_data = tr_sub_data.split('\n')
tr_data_txt = open('tr_data.txt', 'w')
tr_data = ''
training_mat = []
result = []
print rows_tr_sub_data.__len__()

for k,row in enumerate(rows_tr_sub_data):
    if k==0:
        row_list = row.split(',')
        print row_list[0],row_list[1],row_list[2]
    elif k < len(rows_tr_sub_data)-1:
        r_l = row.split(',')
        u_d = du[r_l[0]]
        p_d = d[r_l[1]]
        solved_status = 0
        print k
        if r_l[2] == 'SO':
            solved_status = 1
        accuracy, solved_count, error_count,lev,t1,t2,t3,t4,t5 = p_d
        u_solved_count, u_attempts, ski, u_t = u_d
        result.append(r_l[4])
        print u_d, 'pd', p_d
        tr_data = tr_data + '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15}\n'.format(accuracy,solved_count,
                error_count,lev, t1,
                t2, t3, t4, t5,t1+t2+t3+t4+t5, (u_solved_count),
                u_attempts,int(int(u_solved_count)+1) *int(int(u_attempts)+1),ski, u_t, solved_status)
tr_data_txt.write(tr_data)
print set(sk)
