import os

from App.model import user_data
from flask import render_template, Blueprint, request, redirect, url_for

blue=Blueprint('first',__name__)


@blue.route("/index/")
def index():
    return render_template('test.html')

@blue.route('/welcome/',methods=['post','get'])
def welcome():
    name=request.form.get('name')
    print(name)
    return render_template('welcome.html', name=name)

@blue.route('/table/')
def table():

    return render_template('table.html',students=user_data)

@blue.route('/info/')
def info():
    stu_id=int(request.args.get('id'))
    info = user_data.get(stu_id)


    return render_template('info.html',stu_id=stu_id,info=info)


@blue.route('/update/',methods=('POST','GET'))
def update():
    if request.method =='POST':
        head = request.files.get("head")

        stu_id = int(request.form.get('id'))
        user_data[stu_id]['gender']=request.form.get('gender')
        user_data[stu_id]['birthday']=request.form.get('birthday')
        user_data[stu_id]['city']=request.form.get('city')
        user_data[stu_id]['description']=request.form.get('description')
        print(url_for('blue.table'))
        # 修改头像
        project_dir = os.path.dirname(os.path.abspath(__file__))  # 项目文件夹的绝对路径
        filepath = os.path.join(project_dir, 'static', 'img', f'{stu_id}.jpg')  # 拼接得到图片的上传路径
        head.save(filepath)  # 保存文件
        return redirect('/table/')
    else:
        stu_id=int(request.args.get('id'))
        info = user_data.get(stu_id)

        print(user_data[stu_id]['name'])


        return render_template('update.html', stu_id=stu_id, info=info)
