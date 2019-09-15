from flask import *
import sqlite3
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('test1.html')

@app.route('/submit',methods=['GET','POST'])
def blogpostsubmit():
    if request.method=='POST':
        Title=request.form['BlogPostTitle']
        Content=request.form['blogcontent']
        author=request.form['author']
        print (Title+Content+author)
        
        try:
            with sqlite3.connect("/home/aravind/Desktop/blogs.db") as conn:
                cursor = conn.cursor()
                sql='''INSERT INTO blogpost (Author,Title,Content,Date,Time) values (?,?,?,?,?)'''
                params=(Title,Content,author,'13/09/2019','19:30')
                a=cursor.execute(sql,params)
                print (a)
                conn.commit()
                return 'Successfully Added'
    
        except:
            conn.rollback()
            return 'Failed to Add'
        
        finally:
            conn.close()
    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)