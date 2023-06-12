from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from project.models import *
from user_profile.models import *
from django.db.models import Sum
# Create your views here.



### create project ###
#add
def createProject(req):
    # if('username' in req.session):
        context={}
        allCategory=Category.objects.all()
        context['allCategory']=allCategory
        if(req.method=='POST'):
            myCategory = req.POST['get_category']
            myEmail = MyUser.objects.get(id=1)
            Projects.objects.create(title=req.POST['title'],details=req.POST['details'],category=myCategory,target=req.POST['target'],start_date=req.POST['start_date'],end_date=req.POST['end_date'],owner_id=myEmail,report_count=1)
            return HttpResponseRedirect('/')
        return render(req,'createProject.html',context)
       #id,title,details,category,target,start_date,end_date,owener_email,total_rate,repor_count

#### display project
def displayProject(req,id):
        # req.session.clear()
        context={}
    ######## set the data into context to send it for display page
        req.session['username']='noor@gmail.com'
        getProject = Projects.objects.get(id=id)
        getComment = Comment.objects.filter(project=id)
        getDonation= Donation.objects.filter(project=id)
        getOwnerProject=MyUser.objects.get(id=id)  
        context['setProject']=getProject
        context['setComment']=getComment
        context['setOwnerProject']=getOwnerProject

        sumDonate= 0
    ####################################################################
        
        ####### get all donate for 1 project
        for donate in getDonation:
            sumDonate+=donate.donate_amount
        context['setDonation']=sumDonate
        ###################################
        getUserID = MyUser.objects.get(email=req.session['username'])

        ### check if this user had report project before or not 
        check_if_user_did_report=Report.objects.filter(project=id,user_id=getUserID)
        if(check_if_user_did_report):
           context['reportState']='done'
        ###################################

        ###### check if user rate the project before 
        check_if_user_did_rate=Rating.objects.filter(project=id,user_id=getUserID)
        print(check_if_user_did_rate)
        if(check_if_user_did_rate):
            context['rateState']='done'
        ############################################
        if(req.method=='POST'):
            ########## get report project from user            
            if('report' in req.POST):
                Report.objects.create(project=getProject,user_id=getUserID,report_state=req.POST['report'])

                
                return HttpResponseRedirect('/project/display/{}'.format(int(id)))
            
            ########## get report from user            
            if('reportComment' in req.POST):
                # commentUserID = MyUser.objects.get(email=req.POST['reportCommentUser'])
                Comment.objects.filter(project=getProject,user_id=req.POST['reportCommentUser']).update(report_comment=True)

                #project=projectID,user_id=userID,comment_body=req.POST['commentUser']
                return HttpResponseRedirect('/project/display/{}'.format(int(id)))
            
            ###### get donate from user
            if('donateUser' in req.POST):
                projectID=Projects.objects.get(id=id)
            # myCategory = Category.objects.get(name='help')
                userID = MyUser.objects.get(email=req.session['username'])
                if(req.POST['donateUser']):  ####### check donate not empty
                    Donation.objects.create(project=projectID,user_id=userID,donate_amount=req.POST['donateUser'])
                return HttpResponseRedirect('/project/display/{}'.format(int(id)))
            #############################

        
            ###### get Rate from user
            if('rateValue' in req.POST):
                
            # myCategory = Category.objects.get(name='help')
                userID = MyUser.objects.get(email=req.session['username'])
                print(userID)
                if(req.POST['rateValue']):  ####### check donate not empty
                    Rating.objects.create(project=getProject,user_id=getUserID,rate=req.POST['rateValue'])

                return HttpResponseRedirect('/project/display/{}'.format(int(id)))
            #############################
            ##### get comment from user
            if('commentUser' in req.POST):
                projectID=Projects.objects.get(id=id)
                userID = MyUser.objects.get(email=req.session['username'])
                if(req.POST['commentUser']): ####### check comment not empty
                    Comment.objects.create(project=projectID,user_id=userID,comment_body=req.POST['commentUser'])
            #############################        
                return HttpResponseRedirect('/project/display/{}'.format(int(id)))
        
        ########### check if u are owner of project or just user
        if(req.session['username']=='noor@gmail.com'):
            project = Projects.objects.get(id=id)
            ############check if total donta more tha25% from target or can delete
            total_donations = Donation.objects.filter(project=id).aggregate(Sum('donate_amount'))['donate_amount__sum'] or 0
            deleteProject = True if total_donations < 0.25 * project.target else False
            context['deleteProject']=deleteProject
            return render(req,'displayprojectOwner.html',context)
        else:
            return render(req,'displayprojectUser.html',context)
        #######################################################
        
              
def deleteProject(req,ID):
    if('username' in req.session):
        Projects.objects.filter(id=ID).delete()
        return HttpResponseRedirect('/')
    else:
         return HttpResponseRedirect('/')
