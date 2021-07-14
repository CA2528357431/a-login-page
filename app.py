from flask import Flask,render_template,request,redirect,session #加cookie

app = Flask(__name__)
app.secret_key="wobuxiangxuexi"#cookie密钥

data = ["caoan", "zhanglinghao", "zhangyifan"]
@app.route('/myhk',methods=["POST","GET"])
def hello_world():


    file=open("user","r")
    use=file.read()
    user=eval(use)

    keyff=open("key","r")
    keyf=keyff.read()
    key=eval(keyf)

    if request.method=="GET":
        return render_template("bata.html",data=data)
    #设置默认界面
    ac=request.form.get("account")
    pw = request.form.get("password")
    #获取post参数

    if key["ac"]==ac and key["pw"]==pw:
        return redirect("manager")


    for x in user:

        if ac==x["ac"] and pw==x['pw']:
            session["ac"] = ac
            session["pw"] = pw
            # 保存cookie
            return redirect("log")
            #render是返回一个新的HTML,而redirect则是重新指向新的函数
    else:
        return render_template("bata.html",data=data,msg="WRONG")




@app.route("/log",methods=["GET","POST"])
def log():
    return render_template("log.html",data=data)
@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")
@app.route("/logout",methods=["GET","POST"])
def logout():
    session.clear()
    return render_template("logout.html")
@app.route("/register",methods=["GET","POST"])
def register():

    a={}
    a["ac"]=request.form.get("account")
    a["pw"]=request.form.get("password")
    if request.method=="GET":
        return render_template("register.html")
    file=open("user",'r')
    use=file.read()
    user=eval(use)
    l=len(user)
    a["id"]=l
    if a["ac"]==None:
        return render_template("register.html", msg="请输入用户名")
    if a["pw"]==None:
        return render_template("register.html", msg="请输入密码")
    if len(a["ac"])<=1:
        return render_template("register.html", msg="用户名过短")
    if len(a["pw"])<=1:
        return render_template("register.html", msg="密码过短")

    for x in user:


        if x["ac"]==a["ac"]:
            return render_template("register.html", msg="用户名已存在")

    user.append(a)
    file.close()
    f=open("user","w")
    f.write(str(user))
    return render_template("log.html",data=data)

@app.route("/manager", methods=["GET", "POST"])
def manager():
    userff=open("user","r")
    userf=userff.read()
    user=eval(userf)


    return render_template("manager.html",user=user)

@app.route("/managedo", methods=["GET", "POST"])
def managedo():
    userff = open("user", "r")
    userf = userff.read()
    user = eval(userf)

    uid = int(request.args.get("id"))
    if request.method=="GET":
        return render_template("managedo.html",detail=user[uid])
    neopw=request.form.get("password")
    neoac = request.form.get("account")
    user[uid]["pw"]=neopw
    user[uid]["ac"]=neoac
    userff.close()
    f = open("user", "w")
    f.write(str(user))
    return render_template("managedo.html", detail=user[uid],msg="成功修改")

if __name__ == '__main__':
    app.run(debug=True)
