# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from SurveyBuilderWebsite.models import serverconnection
from SurveyBuilderWebsite.models import registeration
from SurveyBuilderWebsite.models import responsemodel
from email.message import EmailMessage
import pyodbc
import smtplib
import json
conn=pyodbc.connect('Driver={SQL server};'
                        r'Server=DESKTOP-I40FBR6\SQLEXPRESS;'
                        'Database=projectformdatabase;'
                        'Trusted_Connection=yes;')
cursor=conn.cursor()
# Create your views here.
def homepageform(request):
    PersonId=request.GET.get("PersonID")
    return render(request,'projectform.html',{'PersonId':PersonId})
def ajaxform(request):
    insertdata=serverconnection()
    insertdata.FormContent=request.POST.get("pagecontent")
    insertdata.Nameofsurvey=request.POST.get('nameofsurvey')
    insertdata.Formattrndvalues=request.POST.get('contentattrandvalues')
    insertdata.PersonID=request.POST.get('PersonId')
    id_=request.POST.get("idofform")
    if(id_==""):
        cursor.execute("insert into formtype values(?,?,?,?)", insertdata.PersonID,insertdata.Nameofsurvey,insertdata.FormContent,insertdata.Formattrndvalues)
    else:
        cursor.execute("UPDATE formtype SET Nameofsurvey= (?), FormContent = (?) , Formattrndvalues=(?) WHERE Formid =(?)",insertdata.Nameofsurvey,insertdata.FormContent,insertdata.Formattrndvalues,id_)
    conn.commit()
    return render(request,'showsurveys.html')
def showcontent(request):
    PersonID=request.GET.get("id")
    cursor.execute("select * from formtype where PersonID=(?)",PersonID)
    result=cursor.fetchall()
    return render(request,'showsurveys.html',{'res':result,'PersonID':PersonID})
def edit(request):
    idvalue=request.GET.get("btnid")
    PersonID=request.GET.get("PersonID")   
    cursor.execute("select * from formtype where Formid=(?)",idvalue)
    results=cursor.fetchall()
    result=json.loads(results[0][4])
    nameofsurvey=results[0][2]
    return render(request,'projectform.html',{'listofcontent':result,'id':idvalue ,'nameofsurvey':nameofsurvey,'PersonId':PersonID})
def delete(request):
    idvalue=request.POST.get("idofbtn")
    PersonID=request.GET.get("id")
    cursor.execute("select * from response where Formid=(?)",idvalue)
    res_=cursor.fetchall()
    if(res_):
        return HttpResponse("False")
    else:
        cursor.execute("Delete from formtype where Formid=(?)",idvalue)
        #a=PersonID
        return HttpResponse(PersonID)
    conn.commit()
def usersideform(request):
    idvalue=request.GET.get("id")
    cursor.execute("select * from formtype where Formid=(?)",idvalue)
    results=cursor.fetchall()
    result=json.loads(results[0][4])
    NameofSurvey=results[0][2]
    PersonID=int(results[0][1])
    return render(request,'Usersideform.html',{'listofcontent':result,'id':idvalue ,'NameofSurvey':NameofSurvey,'PersonID':PersonID})
def ajaxresponse(request):
    insertresponse=responsemodel()
    insertresponse.PersonID=request.POST.get("PersonID") #insertresponse.
    insertresponse.Formid=request.POST.get("idofform") #insertresponse.
    insertresponse.Nameofsurvey=request.POST.get("NameofSurvey")
    insertresponse.Formattrndvalues=request.POST.get("responsecontent")
    cursor.execute("insert into response values(?,?,?,?)",insertresponse.PersonID,insertresponse.Formid,insertresponse.Nameofsurvey,insertresponse.Formattrndvalues)
    cursor.commit()
    return render(request,'response.html')
def showresponse(request):
    return render(request,'response.html')
def homepageofwebsite(request):
      return render(request,'frontpage.html')
def ajaxregisterrequest(request):
    insertuserdetails=registeration()
    insertuserdetails.Position=request.POST.get('Position')
    insertuserdetails.Email=request.POST.get('Email')
    insertuserdetails.Password_=request.POST.get('Password')
    cursor.execute('insert into registrationdetais values(?,?,?)',insertuserdetails.Position,insertuserdetails.Email,insertuserdetails.Password_)
    conn.commit()
    return HttpResponse("Yes Done")
def ajaxloginrequest(request):
    Position=request.POST.get('Position')
    Email=request.POST.get('Email')
    Password_=request.POST.get('Password')
    cursor.execute("Select * from registrationdetais where Email=(?)",Email)
    res1=cursor.fetchall()
    cursor.execute("Select PersonID from registrationdetais where Position=(?) and Email=(?) and Password_=(?)",Position,Email,Password_)
    res2=cursor.fetchall()
    if(res1):
        if(res2):

            return HttpResponse(res2[0][0])
        else:
            return HttpResponse("Your Password is incorrect")
    else:
         return HttpResponse("This email is not registered")

def sendmail(request):
    id_=request.POST.get("idofbtn")
    mail=request.POST.get("mail")
    Nameofsurvey=request.POST.get('Nameofsurvey')
    PersonID=request.POST.get('PersonID')
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("","") #Write email credentials from which id you want to send the mail to user
    msg=EmailMessage()
    msg['Subject'] ="Check out this"
    msg['From']=""    #Write id from which id you want to send the mail to user
    msg['To']=mail
    msg.add_alternative("""\
        <!DOCTYPE html>
            <html>
            <body>
            <a href="http://127.0.0.1:8000/usersideform?id="""+id_+"""&Nameofsurvey="""+Nameofsurvey+"""&PersonID="""+PersonID+"""">Click this please</a>
            </body>
        </html>
    """,subtype='html')
    server.send_message(msg)
    return HttpResponse("True")

def loginformforsurveybuilder(request):
    return render(request,'loginformforsurveybuilder.html')

def Registerforsurveybuilder(request):
    return render(request,'Registerforsurveybuilder.html')
