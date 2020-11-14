from flask import request
from pony.orm.serialization import to_dict
from models import *
from pony.orm.serialization import to_dict
from flask_jwt_extended import jwt_required


class profile(object):


    @db_session
    @jwt_required
    def addProfile(self):
        email_user = request.form["email_user"]
        company_name = request.form['company_name']
        street_number = request.form['street_number']
        street_name = request.form['street_name']
        zip = request.form['zip']
        city = request.form['city']
        office_phone = request.form['office_phone']
        mobile_phone = request.form['mobile_phone']
        company_reg_numb = request.form['company_reg_numb']
        subc = request.form['subc']
        approval = request.form['approval']

        try:
            saveProfile = Profile(email_user = email_user, company_name=company_name,street_number=street_number,
                              street_name=street_name,zip=zip,city=city,office_phone=office_phone,
                              mobile_phone=mobile_phone,company_reg_numb=company_reg_numb,subc=subc,approval=approval)

            return "success"
        except:
            return "error"

    @db_session
    @jwt_required
    def getProfile(self):
        user = request.args.get('email')
        userProfile = Profile.get(email_user=user)
        return to_dict(userProfile)["Profile"][1]

    def delProfile(self):
        pass

    @db_session
    @jwt_required
    def updateProfile(self):
        email_user = request.form["email_user"]
        company_name = request.form['company_name']
        street_number = request.form['street_number']
        street_name = request.form['street_name']
        zip = request.form['zip']
        city = request.form['city']
        office_phone = request.form['office_phone']
        mobile_phone = request.form['mobile_phone']
        company_reg_numb = request.form['company_reg_numb']
        subc = request.form['subc']
        approval = request.form['approval']

        userProfile = Profile.get(email_user=email_user)
        profile = Profile[userProfile.id]

        # update datas
        try:
            profile.company_name=company_name
            profile.street_number = street_number
            profile.street_name = street_name
            profile.zip = zip
            profile.city = city
            profile.office_phone = office_phone
            profile.mobile_phone = mobile_phone
            profile.company_reg_numb = company_reg_numb
            profile.subc = subc
            profile.approval = approval
            return  "success"
        except:
            return "error updare"