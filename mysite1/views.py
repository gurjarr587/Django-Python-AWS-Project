from __future__ import unicode_literals
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.db import connection,transaction
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
#from django.core.context_processors import csrf
from django.contrib import auth
from .models import admin_user,building_user,normal_user,room,message,department,room_type
# Create your views here.

def createuser(request):

    id_createuser = request.POST.get('id_createuser',False)

    if id_createuser:
        createuserid = id_createuser
        return render(request,"createuser.html",createuserid)

    else:
        return render(request, "createuser.html")

def newuser(request):
    id_submit = request.POST.get('id_submit', False)
    if request.method == 'POST':
        adminid = request.POST.get('adminid',False)
        username = request.POST.get('username', False)
        lastname = request.POST.get('lastname', False)
        password = request.POST.get('password', False)
        email = request.POST.get('email', False)
        ub = admin_user(admin_id=adminid,F_NAME=username,ADMIN_PASS=password,L_NAME=lastname,ADMIN_EMAIL_ID=email)
        ub.save()
        return redirect('/index')
    else:
        return render(request, "newuser.html")

def query(request):
    return render(request,"query.html")

def index(request):

    return render(request,"index.html")


def login(request):
    '''
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
            adminuser = admin_user.objects.get(F_NAME=username)

            if adminuser.ADMIN_PASS == password:
                #request.session['member_id']=adminuser.ADMIN_ID
                #request.session['member_id'] = normaluser.ADMIN_ID
                #request.session['member_id'] = buildinguser.ADMIN_ID
                context = {
                    'result': username,

                }
            return render(request, 'login.html', context)
        except:
            print("Invalid User Credentials")
            return redirect('/index')
            '''
    if request.method == 'POST' and request.POST['password'] :
        username = request.POST['username']
        password = request.POST['password']


        try:
            normaluser = normal_user.objects.get(F_NAME=username)

            send_mail(
                'Subject here',
                'Welcome to UBClassRoom you are logged in now',
                settings.EMAIL_HOST_USER,
                ['gurjarr36@gmail.com'],
                fail_silently=False,
            )
            if normaluser.NORMAL_USER_PASS == password:
                context = {
                    'result': username,

                }
            return render(request, 'login.html', context)
        except:
            print("Invalid User Credentials")
            return redirect('/index')
    else:
        return render(request, 'index.html')
'''
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        try:
            buildinguser = building_user.objects.get(F_NAME=username)

            if buildinguser.B_ADMIN_PASS == password:
                context = {
                    'result': username,

                }
            return render(request, 'login.html', context)
        except:
            print("Invalid User Credentials")
            return redirect('/index')


    else:
        return render(request, 'index.html')
'''

def roomv(request):
    if request.method == 'POST':

        command = request.POST['text']
        room_info = room.objects.raw(command)
        context ={
            'room_info':room_info
        }
        return render(request,'room.html',context)


    else:
        return render(request,'room.html')


def roomt(request):
    if request.method == 'POST':

        command = request.POST['text']
        room_info = room_type.objects.raw(command)
        context ={
            'room_info':room_info
        }
        return render(request,'roomt.html',context)


    else:
        return render(request,'roomt.html')


def normaluser(request):
    if request.method == 'POST':

        command = request.POST['text']
        sqlTokens = command.split(' ')

        index = 0

        parenthesis_index = 0
        if 'insert' in sqlTokens:
            for eachToken in sqlTokens:
                index += 1
                if eachToken == '(':
                    parenthesis_index = index

            print(parenthesis_index)

            index = 0

            values_list = []

            for eachToken in sqlTokens:
                index += 1
                if index > parenthesis_index:
                    if index != len(sqlTokens):
                        values_list.append(eachToken)

            adm = normal_user(USER_ID=values_list[0],F_NAME=values_list[1],L_NAME=values_list[2],NORMAL_USER_EMAIL_ID=values_list[3],NORMAL_USER_PASS=values_list[4],admin_id=values_list[5],B_ADMIN_ID=values_list[6])
            adm.save()
            return render(request, 'queryexecute.html')

        elif 'delete' in sqlTokens:
            for eachToken in sqlTokens:
                index += 1
                if eachToken == '(':
                    parenthesis_index = index
            print(parenthesis_index)

            index = 0

            values_list = []

            for eachToken in sqlTokens:
                values_list.append(eachToken)
            print(values_list)

            instance = normal_user.objects.get(admin_id = values_list[-1])
            instance.delete()
            return render(request, 'queryexecute.html')

        else:
            command = request.POST['text']
            x = normal_user.objects.raw(command)
            context = {
                'x': x,
            }
            return render(request, 'queryexecute.html', context)
    else:
        return render(request, 'queryexecute.html')


def adminuserv(request):
    if request.method == 'POST':

        command = request.POST['text']
        sqlTokens = command.split(' ')

        index = 0

        parenthesis_index = 0
        if 'insert' in sqlTokens:
            for eachToken in sqlTokens:
                index += 1
                if eachToken == '(':
                    parenthesis_index = index

            print(parenthesis_index)

            index = 0

            values_list = []

            for eachToken in sqlTokens:
                index += 1
                if index > parenthesis_index:
                    if index != len(sqlTokens):
                        values_list.append(eachToken)

            adm = admin_user(admin_id=values_list[0],F_NAME=values_list[1],L_NAME=values_list[2],ADMIN_EMAIL_ID=values_list[3],ADMIN_PASS=values_list[4],M_NAME=values_list[5])
            adm.save()
            return render(request, 'adminuser.html')

        elif 'delete' in sqlTokens:
            for eachToken in sqlTokens:
                index += 1
                if eachToken == '(':
                    parenthesis_index = index
            print(parenthesis_index)

            index = 0

            values_list = []

            for eachToken in sqlTokens:
                values_list.append(eachToken)
            print(values_list)

            instance = admin_user.objects.get(admin_id = values_list[-1])
            instance.delete()
            return render(request, 'adminuser.html')

            '''
        elif 'update' in sqlTokens:
            for eachToken in sqlTokens:
                index += 1
                if eachToken == '(':
                    parenthesis_index = index
            print(parenthesis_index)

            index = 0

            values_list = []

            for eachToken in sqlTokens:
                values_list.append(eachToken)
            print(values_list)

            instance = admin_user.objects.get(admin_id = values_list[-1])
            instance.commit()
            return render(request, 'adminuser.html')
            '''

        else:
            command = request.POST['text']
            admin_info = admin_user.objects.raw(command)
            context = {
                'x': admin_info,
            }
            return render(request, 'adminuser.html', context)


    else:
        return render(request,'adminuser.html')


def buildinguserv(request):
    if request.method == 'POST':
        command = request.POST['text1']
        build_info = building_user.objects.raw(command)
        context ={
            'x':build_info,
        }
        return render(request,'buildinguser.html',context)
    else:
        return render(request, 'buildinguser.html')

def departmentv(request):
    if request.method == 'POST':
        command = request.POST['text1']
        build_info = department.objects.raw(command)
        context ={
            'x':build_info,
        }
        return render(request,'department.html',context)
    else:
        return render(request, 'department.html')

def messagev(request):
    if request.method == 'POST':
        command = request.POST['text']
        message_info = message.objects.raw(command)
        context ={
            'x':message_info,
        }
        return render(request,'message.html',context)
    else:
        return render(request, 'message.html')


def logout(request):
    try:
        del request.session['member_id']
        return redirect('/index')
    except KeyError:
        pass
    return redirect('/index')







