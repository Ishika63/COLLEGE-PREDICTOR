#code to predict

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

#funtion to modify branch column
def modify_branch(df):
    size = df.shape[0]
    for i in range(0,size):
        df.branch[i] = df.branch[i].split('(')[0].strip()
    return df


#funtion to modify oprank column
def modify_oprank(df):
    size = df.shape[0]
    if type(df.oprank[0]) == str :
        toto = []
        for i in range(0,size):
            temp = df.oprank[i]
            if temp[len(temp)-1] == 'P':
                toto.append(i)
        df = df.drop(toto) 
        df = df.reset_index(drop=True)
        size = df.shape[0]
    for i in range(0,size):
        temp = int(float(df.oprank[i]))
        df.oprank[i] = temp
    df = df.sort_values(['oprank'])
    df = df.reset_index(drop=True)
    return df
    
 
 #funtion to modify csv
def modify_csv(file_name):
    df = pd.read_csv(file_name)
    df = modify_branch(df)
    df = modify_oprank(df)
    return df

#list of college names
college_names = ['IITBHU','IITBOMBAY','IITDELHI','IITKANPUR','IITKHAR','IITMADRAS','IITROORKEE','NITTIRUCHIRAPALLI','NITNAGPUR','NITROURKELA','NITSRINAGAR','NITWARANGAL']
 
 #list of branch names
branches = ['Aerospace Engineering',
 'Agricultural and Food Engineering',
 'Agricultural and Food Engineering with M.Tech. in any of the listed specializations',
 'Applied Geology',
 'Applied Mathematics',
 'Architecture',
 'BS in Mathematics',
 'Bio Medical Engineering',
 'Bio Technology',
 'Biological Engineering',
 'Biological Sciences',
 'Biological Sciences and Bioengineering',
 'Biotechnology and Biochemical Engineering',
 'Ceramic Engineering',
 'Ceramic Engineering and M.Tech Industrial Ceramic',
 'Chemical Engineering',
 'Chemistry',
 'Civil Engineering',
 'Civil Engineering and M. Tech. in Structural Engineering',
 'Civil Engineering and M.Tech in Transportation Engineering',
 'Civil Engineering and M.Tech. in Environmental Engineering',
 'Civil Engineering with any of the listed specialization',
 'Computer Science and Engineering',
 'Earth Sciences',
 'Economics',
 'Electrical Engineering',
 'Electrical Engineering and M.Tech Power Electronics and Drives',
 'Electrical Engineering with M.Tech. in any of the listed specializations',
 'Electrical and Electronics Engineering',
 'Electronics and Communication Engineering',
 'Electronics and Electrical Communication Engineering',
 'Electronics and Electrical Communication Engineering with M.Tech. in any of the\nlisted specializations',
 'Electronics and Instrumentation Engineering',
 'Energy Engineering with M.Tech. in Energy Systems Engineering',
 'Engineering Design',
 'Engineering Physics',
 'Environmental Science and Engineering',
 'Exploration Geophysics',
 'Food Process Engineering',
 'Geological Technology',
 'Geophysical Technology',
 'Industrial Design',
 'Industrial and Systems Engineering',
 'Industrial and Systems Engineering with M.Tech. in Industrial and Systems\nEngineering and Management',
 'Information Technology',
 'Instrumentation Engineering',
 'Instrumentation and Control Engineering',
 'Life Science',
 'Manufacturing Science and Engineering',
 'Manufacturing Science and Engineering with M.Tech. in Industrial and Systems\nEngineering and Management',
 'Materials Science and Engineering',
 'Mathematics',
 'Mathematics and Computing',
 'Mathematics and Scientific Computing',
 'Mechanical Engineering',
 'Mechanical Engineering and M. Tech. in Mechanical System Design',
 'Mechanical Engineering and M. Tech. in Thermal Science & Engineering',
 'Mechanical Engineering and M.Tech. in Computer Integrated Manufacturing',
 'Mechanical Engineering with M.Tech. in Manufacturing Engineering',
 'Mechanical Engineering with M.Tech. in any of the listed specializations',
 'Metallurgical Engineering & Materials Science',
 'Metallurgical Engineering and Materials Science',
 'Metallurgical and Materials Engineering',
 'Mining Engineering',
 'Mining Safety Engineering',
 'Naval Architecture and Ocean Engineering',
 'Ocean Engineering and Naval Architecture',
 'Physics',
 'Polymer Science and Engineering',
 'Production Engineering',
 'Production and Industrial Engineering',
 'Quality Engineering Design and Manufacturing',
 'Textile Technology']
 
 #list of all the seatpool's
seatpool = ['Gender-Neutral', 'Female-Only']

#list of all the categories
categories = ['GEN-EWS(PwD)',
 'SC',
 'OPEN',
 'ST (PwD)',
 'SC (PwD)',
 'OBC-NCL',
 'OBC-NCL(PwD)',
 'GEN-EWS',
 'ST',
 'OPEN (PwD)']

#list of degrees of round 1
degrees = [1,1,1,3,1,1,2,1,1,1,1,1,9,4,7,1,1,1,1,4,1,2,4,1,1,2,4,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,10,1,1,1,1,1,1,1,7,2,1,1,1,4,1,1,2,1,1]


#code for app.py
from flask import Flask,url_for,render_template,request

app = Flask(__name__) 

@app.route('/new',methods=['POST','GET'])
def data():
    if request.method == 'POST':
        rank = request.form["rank"]
        round =request.form["round"]
        branchoo = request.form["branch"]
        seatpooloo= request.form["seatpool"]
        categoryoo = request.form["category"]
        toto = []
        for i in college_names:
            toto.append(modify_csv('./ROUND'+round+'/'+i+'.csv'))
        #function to add college name column in dataframe
        c = 0;
        for i in range(0,12):
            size = toto[i].shape[0]
            toto[i]['college_name'] = [college_names[c]]*size
            c  += 1
        #funtion to create a branch dataframe
        def create_branch_df(df,branch_name,seat_type,category_name):
            df = df[df.branch == branch_name]
            df = df[df.category == category_name]
            df = df[df.seatpool == seat_type]
            df = df.sort_values(by=['oprank'])
            df = df.reset_index(drop = True)
            size = df.shape[0]
            if size > 1:
                df = df.drop(list(range(1,size)))
            return df
        #intializing a empty dataframe
        new_df = pd.DataFrame({
            'branch' : [] ,
            'seatpool' : [] ,
            'oprank' : [] ,
            'closerank' : [] ,
            'category' : [] ,
            'college_name' : []
        })
        branch_df = new_df
        #from user input we will take branch_name,seat_type,category
        branch_name = 'Computer Science and Engineering'
        seat_type = 'Gender-Neutral'
        category = 'OPEN'
        #pandas empty dataframe to hold the result
        branch_df = pd.concat([create_branch_df(toto[i], branchoo, 'Gender-Neutral', 'OPEN') for i in range(12)], ignore_index=True)

        if branch_df.shape[0] == 0:
            return f"<h1>WE DIDN'T FIND ANYTHING THAT MATCHED YOUR REQUIREMENTS</h1>"
        sns.set_style('darkgrid')
        branch_df = branch_df.reset_index(drop=True)
        for i in range(0,branch_df.shape[0]):
            branch_df.closerank[i] = int(float(branch_df.closerank[i]))
        branch_df = branch_df.sort_values(by=['closerank']).reset_index(drop=True)
        fun = np.poly1d(np.polyfit(branch_df.closerank.tolist(),list(range(0,branch_df.shape[0])),degrees[branches.index(branchoo)]))
        rank = int(rank)
        index = int(fun(rank))
        display = branch_df.college_name.tolist()[index:]
        string = ""
        for i in range(0,len(display)):
            string += "<h1>"+display[i]+"</h1>"
        return string
    else:
        return render_template('temp.html') 

if __name__ == "__main__":
    app.run(debug=True)