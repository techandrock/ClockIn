import json ,time, subprocess, os
from collections import defaultdict

def add_firstname():
    employee_name_file = open('employee_firstname_file.py', 'r')
    read_the_file = employee_name_file.readline()
    decode_data = json.loads(read_the_file)
    employee_name_file.close()
    add_employee = input("Add employee firstname to database:")
    decode_data.append(add_employee)
    encode_data = json.dumps(decode_data)
    write_file = open('employee_firstname_file.py', 'w')
    write_file.write(encode_data)
    write_file.close()

def add_lastname():
    employee_name_file = open('employee_lastname_file.py', 'r')
    read_the_file = employee_name_file.readline()
    decode_data = json.loads(read_the_file)
    employee_name_file.close()
    add_employee = input("Add employee lastname to database:")
    decode_data.append(add_employee)
    encode_data = json.dumps(decode_data)
    write_file = open('employee_lastname_file.py', 'w')
    write_file.write(encode_data)
    write_file.close()

def add_pay():
    employee_name_file = open('employee_pay_file.py', 'r')
    read_the_file = employee_name_file.readline()
    decode_data = json.loads(read_the_file)
    employee_name_file.close()
    add_employee = input("Add employee pay to database: $")
    decode_data.append(add_employee)
    #print(dec)
    encode_data = json.dumps(decode_data)
    write_file = open('employee_pay_file.py', 'w')
    write_file.write(encode_data)
    write_file.close()

def add_tax_withholding():
    employee_name_file = open('employee_withholding_file.py', 'r')
    read_the_file = employee_name_file.readline()
    decode_data = json.loads(read_the_file)
    employee_name_file.close()
    add_employee = input("Add employee tax withholding to database:")
    decode_data.append(add_employee)
    #print(dec)
    encode_data = json.dumps(decode_data)
    write_file = open('employee_withholding_file.py', 'w')
    write_file.write(encode_data)
    write_file.close()

def add_employee():
    add_firstname()
    add_lastname()
    add_pay()
    add_tax_withholding()
    print("Employee added!")
    time.sleep(2)

def add_first_employee_name():
    employee_first_name = []
    employee_name_file = open('employee_firstname_file.py', 'w')
    add_employee = input("Add employee firstname to database:")
    employee_first_name.append(add_employee)
    encode_data = json.dumps(employee_first_name)
    employee_name_file.write(encode_data)
    employee_name_file.close()

def add_last_employee_name():
    employee_last_name = []
    employee_name_file = open('employee_lastname_file.py', 'w')
    add_employee = input("Add employee lastname to database:")
    employee_last_name.append(add_employee)
    encode_data = json.dumps(employee_last_name)
    employee_name_file.write(encode_data)
    employee_name_file.close()

def add_first_employee_pay():
    employee_pay = []
    employee_name_file = open('employee_pay_file.py', 'w')
    add_employee = input("Add employee pay to database: $")
    employee_pay.append(add_employee)
    encode_data = json.dumps(employee_pay)
    employee_name_file.write(encode_data)
    employee_name_file.close()

def add_first_employee_id():
    employee_id = []
    employee_name_file = open('employee_withholding_file.py', 'w')
    add_employee = input("Add employee tax withholding to database:")
    employee_id.append(add_employee)
    encode_data = json.dumps(employee_id)
    employee_name_file.write(encode_data)
    employee_name_file.close()

def add_first_employee():
    add_first_employee_name()
    add_last_employee_name()
    add_first_employee_pay()
    add_first_employee_id()
    print("Employee added!")
    time.sleep(2)

def add_time():
    insert_time_dict = {}
    employee = input("Enter the firstname of the employee to add the time to.").lower()
    timefile = open(employee + "inout.txt", 'a')
    newtime = input("Enter the date (mm/dd/yyyy): ")
    time_in = input("Enter the time in. (12 hour clock)  (hh:mm)")
    am_or_pm = input("AM or PM?").lower()
    if am_or_pm == 'pm':
        the_hours = time_in[0:2]
        if time_in[0]== '0':
            the_hours = time_in[1:2]
        to_military = eval(the_hours)
        military_time = str(to_military + 12)
        minutes_to_add = time_in[2:5]
        time_in = military_time + minutes_to_add

    time_out = input("Enter the time out (12 hour clock)  (hh:mm)")
    am_or_pm = input("AM or PM?").lower()
    if am_or_pm == 'pm':
        the_hours = time_out[0:2]
        if time_out[0]== '0':
            the_hours = time_out[1:2]
        to_military = eval(the_hours)
        military_time = str(to_military + 12)
        minutes_to_add = time_out[2:5]
        time_out = military_time + minutes_to_add
    insert_time_dict['DATE'] = newtime
    insert_time_dict['IN'] = time_in
    insert_time_dict['OUT'] = time_out
    encode_json = json.dumps(insert_time_dict)
    timefile.write(encode_json + '\n')
    timefile.close()

def delete_time_files():
    employee_name_file = open("employee_firstname_file.py" , 'r')
    read_the_file = employee_name_file.readline()
    employee_name_file.close()
    decode_data = json.loads(read_the_file)
    length = len(decode_data)
    for name in range(length):
        employee_name = decode_data[name]
        subprocess.call("mv " + employee_name + "inout.txt /home/pi/time_files/" , shell = True)
        #subprocess.Popen("rm " + employee_name + "inout.txt" , shell = True)
        subprocess.Popen("rm " + employee_name + "in.txt" , shell = True)
        print(employee_name.upper() + "'S timefile has been moved to /home/pi/time_files/.")
        time.sleep(6)

def clockin():
    clockin_time_dict = {}
    timefile = open(employee + "in.txt", 'w')
    clockin_time_dict['DATE'] = time.strftime("%m/%d/%Y")
    clockin_time_dict['IN'] = time.strftime("%H:%M")
    encode_json = json.dumps(clockin_time_dict)
    timefile.write(encode_json + '\n')
    timefile.close()
    print("Thank you," , employee.upper() +" ," ,"you have been clocked in." )
    time.sleep(2)

def clockout():
    timefile = open(employee+ "in.txt", 'r')
    for line in timefile:
        decode_json = json.loads(line)
        #return decode_json
    timefile.close()
    open(employee + "in.txt", 'w').close()
    timefile = open(employee + "inout.txt", 'a')
    decode_json['OUT'] = time.strftime("%H:%M")
    encode_json = json.dumps(decode_json)
    timefile.write(encode_json + '\n')
    timefile.close()
    print("Thank you,", employee.upper() +' , ' "you have been clocked out")
    time.sleep(2)

def checkaction():
    try:
        x = open(employee + "in.txt", 'r')
        y = x.read()
        x.close()
        z = len(y)
        if z > 0:
            action = input("You are clocked in. Clock out?").lower()
            clockout_action = action[0]
            if clockout_action == 'y':
                clockout()
            elif clockout_action == 'n':
                newaction = input("Do you want to clock in?")
                clockout_newaction = newaction[0]
                if clockout_newaction == 'y':
                    print("Be aware your never clocked out from the last time you worked")
                    clockin()
            else:
                print("Returning to main screen to try again.")
                time.sleep(1)
        elif z ==0:
            clockin()
    except IOError:
        open(employee + 'in.txt', 'w').close()
        clockin()

def total_hours():
    timefile = open(person + "inout.txt", 'r')
    totalhrs = 0
    totalminute = 0
    for line in timefile:
        #print(line)
        decode_json = json.loads(line)
        time_dict = decode_json
        intime = time_dict['IN']
        outtime = time_dict['OUT']
        out_time = outtime.split(':')
        intime_num = intime.split(':')
        #print(intime_num)
        hourin_str = intime_num[0]
        hourin = int(hourin_str)
        minutein_str = intime_num[1]
        minutein = int(minutein_str)
        hourout_str = out_time[0]
        hourout = int(hourout_str)
        minuteout_str = out_time[1]
        minuteout = int(minuteout_str)
        totalhrs = (hourout - hourin) + totalhrs
        #print(totalhrs)
        totalminute = (minuteout - minutein) + totalminute
        #print(totalminute)
    minstohr = totalminute/60
    total_time_float = totalhrs + minstohr
    total_time = round(total_time_float , 2)
    total_time_str = str(total_time)
    return(total_time_str)

def print_total_hours():
    timefile = open(employeeHr + "inout.txt", 'r')
    totalhrs = 0
    totalminute = 0
    for line in timefile:
        #print(line)
        decode_json = json.loads(line)
        time_dict = decode_json
        intime = time_dict['IN']
        outtime = time_dict['OUT']
        out_time = outtime.split(':')
        intime_num = intime.split(':')
        #print(intime_num)
        hourin_str = intime_num[0]
        hourin = int(hourin_str)
        minutein_str = intime_num[1]
        minutein = int(minutein_str)
        hourout_str = out_time[0]
        hourout = int(hourout_str)
        minuteout_str = out_time[1]
        minuteout = int(minuteout_str)
        totalhrs = (hourout - hourin) + totalhrs
        #print(totalhrs)
        totalminute = (minuteout - minutein) + totalminute
        #print(totalminute)
    minstohr = totalminute/60
    total_time_float = totalhrs + minstohr
    total_time = round(total_time_float , 2)
    total_time_str = str(total_time)
    print(total_time_str + " hours.")

def create_report(person):
    timefile = open(person + "inout.txt", 'r')
    report_file = open(person + 'report.txt', 'a')
    report_file.write(person.upper() +' '+ lastname.upper())
    payperiodtitle = 'PAY PERIOD ENDING: __/__/__'.rjust(40)
    report_file.write(payperiodtitle + '\n' + '\n')
    datetitle = 'DATE'.ljust(15)
    report_file.write(datetitle)
    intitle = 'IN'.ljust(15)
    report_file.write(intitle)
    outtitle = 'OUT'.ljust(15)
    report_file.write(outtitle)
    hourtitle = 'HOURS\n'
    report_file.write(hourtitle)
    for line in timefile:
        decode_json = json.loads(line)
        time_dict = decode_json
        intime = time_dict['IN']
        outtime = time_dict['OUT']
        date = time_dict['DATE']
        formatdate = date.ljust(15)
        formatintime = intime.ljust(15)
        formatoutime = outtime.ljust(15)
        report_file.write(formatdate)
        report_file.write(formatintime)
        report_file.write(formatoutime)

        out_time = outtime.split(':')
        intime_num = intime.split(':')
        #print(intime_num)
        hourin_str = intime_num[0]
        hourin = int(hourin_str)
        minutein_str = intime_num[1]
        minutein = int(minutein_str)
        hourout_str = out_time[0]
        hourout = int(hourout_str)
        minuteout_str = out_time[1]
        minuteout = int(minuteout_str)
        hours = (hourout - hourin)
        #print(totalhrs)
        totalminute = (minuteout - minutein)
        minstohr = totalminute/60
        total_time_float = hours + minstohr
        total_time = round(total_time_float , 2)
        stringtime = str(total_time)

        totalTime = eval(total_hours())
        grosspay = pay * totalTime
        grosspay_round = round(grosspay,2)
        grosspay_round_string = str(grosspay_round)
        grosspay_decimal = grosspay_round_string.split('.')
        check_decimal = (grosspay_decimal[1])
        try:
            check_decimal[1]
        except IndexError:
            grosspay_round_string = grosspay_round_string + '0'
        fica = .0620 * grosspay
        fica_round = round(fica,2)
        fica_round_str = str(fica_round)
        try:
            fica_round_str[3]
        except IndexError:
            fica_round_str = fica_round_str +'0'
        medicare = .0145 * grosspay
        medicare_round = round(medicare, 2)
        medicare_round_str = str(medicare_round)
        try:
            medicare_round_str[3]
        except IndexError:
            medicare_round_str = medicare_round_str +'0'
        totalTax = fica_round + medicare_round + state_tax(grosspay, id_number) + federal_tax(grosspay, id_number)
        totalTax_round = round(totalTax, 2)
        totalTax_string = str(totalTax_round)
        totalTax_decimal = totalTax_string.split('.')
        check_tax_decimal = totalTax_decimal[1]
        try:
            check_tax_decimal[1]
        except IndexError:
            totalTax_string = totalTax_string + '0'
        netPay = grosspay_round - totalTax_round
        netPay_round = round(netPay, 2)
        netPay_string = str(netPay_round)
        netPay_decimal = netPay_string.split('.')
        check_net_decimal = netPay_decimal[1]
        try:
            check_net_decimal[1]
        except IndexError:
            netPay_string = netPay_string + '0'
        report_file.write(stringtime+'\n')

    report_file.write("\nTOTAL TIME:    " + total_hours() +'       STATE TAX: $'+ str(state_tax(grosspay, id_number))+'.00')
    report_file.write("\nPAY:         * $" + str(pay)+'0' +'      FEDERAL TAX: $' + str(federal_tax(grosspay, id_number))+'.00')
    report_file.write("\nGROSS:         $" +(grosspay_round_string) + '     FICA: $'+ fica_round_str)
    report_file.write("\n                           MEDICARE: $" + medicare_round_str)
    report_file.write("\n                           TOTAL TAX: $" + totalTax_string)
    report_file.write("\nNET PAY: $" + netPay_string)
    report_file.write("\n\nCHECK NUMBER: _______")
    report_file.write("\n\nDATE: __/__/__")

def state_tax(grosspay, id_number):
    if grosspay >= 0 and grosspay < 50:
        statetax = 0
        return statetax
    elif grosspay >= 50 and grosspay < 100 and id_number == 0:
        statetax = 1
        return statetax
    elif grosspay >= 50 and grosspay < 100 and id_number > 0:
        statetax = 0
        return statetax
    elif grosspay >= 100 and grosspay < 150 and id_number == 0:
        statetax = 2
        return statetax
    elif grosspay >= 100 and grosspay < 150 and id_number == 1:
        statetax = 1
        return statetax
    elif grosspay >= 100 and grosspay < 150 and id_number > 1:
        statetax = 0
        return statetax
    elif grosspay >= 150 and grosspay < 200 and id_number == 0:
        statetax = 3
        return statetax
    elif grosspay >= 150 and grosspay < 200 and id_number == 1:
        statetax = 2
        return statetax
    elif grosspay >= 150 and grosspay < 200 and id_number  > 1:
        statetax = 0
        return statetax
    elif grosspay >= 200 and grosspay < 250 and id_number == 0:
        statetax = 4
        return statetax
    elif grosspay >= 200 and grosspay < 250 and id_number == 1:
        statetax = 3
        return statetax
    elif grosspay >= 200 and grosspay < 250 and id_number == 2:
        statetax = 1
        return statetax
    elif grosspay >= 200 and grosspay < 250 and id_number > 2:
        statetax = 0
        return statetax
    elif grosspay >= 250 and grosspay < 300 and id_number == 0:
        statetax = 5
        return statetax
    elif grosspay >= 250 and grosspay < 300 and id_number == 1:
        statetax = 4
        return statetax
    elif grosspay >= 250 and grosspay < 300 and id_number == 2:
        statetax = 2
        return statetax
    elif grosspay >= 250 and grosspay < 300 and id_number == 3:
        statetax = 1
        return statetax
    elif grosspay >= 250 and grosspay < 300 and id_number > 3:
        statetax = 0
        return statetax
    elif grosspay >= 300 and grosspay < 350 and id_number == 0:
        statetax = 7
        return statetax
    elif grosspay >= 300 and grosspay < 350 and id_number == 1:
        statetax = 4
        return statetax
    elif grosspay >= 300 and grosspay < 350 and id_number == 2:
        statetax = 3
        return statetax
    elif grosspay >= 300 and grosspay < 350 and id_number == 3:
        statetax = 2
        return statetax
    elif grosspay >= 300 and grosspay < 350 and id_number > 3:
        statetax = 0
        return statetax
    elif grosspay >= 350 and grosspay < 400 and id_number == 0:
        statetax = 9
        return statetax
    elif grosspay >= 350 and grosspay < 400 and id_number == 1:
        statetax = 5
        return statetax
    elif grosspay >= 350 and grosspay < 400 and id_number == 2:
        statetax = 4
        return statetax
    elif grosspay >= 350 and grosspay < 400 and id_number == 3:
        statetax = 2
        return statetax
    elif grosspay >= 350 and grosspay < 400 and id_number == 4:
        statetax = 1
        return statetax
    elif grosspay >= 350 and grosspay < 400 and id_number > 4:
        statetax = 0
        return statetax
    elif grosspay >= 400 and grosspay < 450 and id_number == 0:
        statetax = 11
        return statetax
    elif grosspay >= 400 and grosspay < 450 and id_number == 1:
        statetax = 8
        return statetax
    elif grosspay >= 400 and grosspay < 450 and id_number == 2:
        statetax = 5
        return statetax
    elif grosspay >= 400 and grosspay < 450 and id_number == 3:
        statetax = 3
        return statetax
    elif grosspay >= 400 and grosspay < 450 and id_number == 4:
        statetax = 2
        return statetax
    elif grosspay >= 400 and grosspay < 450 and id_number == 5:
        statetax = 1
        return statetax
    elif grosspay >= 400 and grosspay < 450 and id_number > 5:
        statetax = 0
        return statetax
    elif grosspay >= 450 and grosspay < 500 and id_number == 0:
        statetax = 13
        return statetax
    elif grosspay >= 450 and grosspay < 500 and id_number == 1:
        statetax = 10
        return statetax
    elif grosspay >= 450 and grosspay < 500 and id_number == 2:
        statetax = 6
        return statetax
    elif grosspay >= 450 and grosspay < 500 and id_number == 3:
        statetax = 4
        return statetax
    elif grosspay >= 450 and grosspay < 500 and id_number == 4:
        statetax = 3
        return statetax
    elif grosspay >= 450 and grosspay < 500 and id_number == 5:
        statetax = 1
        return statetax
    elif grosspay >= 450 and grosspay < 500 and id_number > 5:
        statetax = 0
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number == 0:
        statetax = 17
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number == 1:
        statetax = 13
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number == 2:
        statetax = 10
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number == 3:
        statetax = 6
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number == 4:
        statetax = 4
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number == 5:
        statetax = 3
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number == 6:
        statetax = 1
        return statetax
    elif grosspay >= 500 and grosspay < 600 and id_number > 6:
        statetax = 0
        return statetax

def federal_tax(grosspay, id_number):
    if grosspay >= 0 and grosspay < 115:
        federaltax = 0
        return federaltax
    elif grosspay >= 115 and grosspay < 120 and id_number == 0:
        federaltax = 2
        return federaltax
    elif grosspay >= 115 and grosspay < 120 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 120 and grosspay < 130 and id_number == 0:
        federaltax = 3
        return federaltax
    elif grosspay >= 120 and grosspay < 130 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 130 and grosspay < 140 and id_number == 0:
        federaltax = 4
        return federaltax
    elif grosspay >= 130 and grosspay < 140 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 140 and grosspay < 150 and id_number == 0:
        federaltax = 5
        return federaltax
    elif grosspay >= 140 and grosspay < 150 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 150 and grosspay < 160 and id_number == 0:
        federaltax = 6
        return federaltax
    elif grosspay >= 150 and grosspay < 160 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 160 and grosspay < 170 and id_number == 0:
        federaltax = 7
        return federaltax
    elif grosspay >= 160 and grosspay < 170 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 170 and grosspay < 180 and id_number == 0:
        federaltax = 8
        return federaltax
    elif grosspay >= 170 and grosspay < 180 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 180 and grosspay < 190 and id_number == 0:
        federaltax = 9
        return federaltax
    elif grosspay >= 180 and grosspay < 190 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 190 and grosspay < 200 and id_number == 0:
        federaltax = 10
        return federaltax
    elif grosspay >= 190 and grosspay < 200 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 200 and grosspay < 210 and id_number == 0:
        federaltax = 11
        return federaltax
    elif grosspay >= 200 and grosspay < 210 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 210 and grosspay < 220 and id_number == 0:
        federaltax = 12
        return federaltax
    elif grosspay >= 210 and grosspay < 220 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 220 and grosspay < 230 and id_number == 0:
        federaltax = 13
        return federaltax
    elif grosspay >= 220 and grosspay < 230 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 230 and grosspay < 240 and id_number == 0:
        federaltax = 14
        return federaltax
    elif grosspay >= 230 and grosspay < 240 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 240 and grosspay < 250 and id_number == 0:
        federaltax = 15
        return federaltax
    elif grosspay >= 240 and grosspay < 250 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 250 and grosspay < 260 and id_number == 0:
        federaltax = 16
        return federaltax
    elif grosspay >= 250 and grosspay < 260 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 260 and grosspay < 270 and id_number == 0:
        federaltax = 17
        return federaltax
    elif grosspay >= 260 and grosspay < 270 and id_number > 0:
        federaltax = 0
        return federaltax
    elif grosspay >= 270 and grosspay < 280 and id_number == 0:
        federaltax = 18
        return federaltax
    elif grosspay >= 270 and grosspay < 280 and id_number == 1:
        federaltax = 1
        return federaltax
    elif grosspay >= 270 and grosspay < 280 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 280 and grosspay < 290 and id_number == 0:
        federaltax = 19
        return federaltax
    elif grosspay >= 280 and grosspay < 290 and id_number == 1:
        federaltax = 2
        return federaltax
    elif grosspay >= 280 and grosspay < 290 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 290 and grosspay < 300 and id_number == 0:
        federaltax = 20
        return federaltax
    elif grosspay >= 290 and grosspay < 300 and id_number == 1:
        federaltax = 3
        return federaltax
    elif grosspay >= 290 and grosspay < 300 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 300 and grosspay < 310 and id_number == 0:
        federaltax = 21
        return federaltax
    elif grosspay >= 300 and grosspay < 310 and id_number == 1:
        federaltax = 4
        return federaltax
    elif grosspay >= 300 and grosspay < 310 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 310 and grosspay < 320 and id_number == 0:
        federaltax = 22
        return federaltax
    elif grosspay >= 310 and grosspay < 320 and id_number == 1:
        federaltax = 5
        return federaltax
    elif grosspay >= 310 and grosspay < 320 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 320 and grosspay < 330 and id_number == 0:
        federaltax = 23
        return federaltax
    elif grosspay >= 320 and grosspay < 330 and id_number == 1:
        federaltax = 6
        return federaltax
    elif grosspay >= 320 and grosspay < 330 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 330 and grosspay < 340 and id_number == 0:
        federaltax = 24
        return federaltax
    elif grosspay >= 330 and grosspay < 340 and id_number == 1:
        federaltax = 7
        return federaltax
    elif grosspay >= 330 and grosspay < 340 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 340 and grosspay < 350 and id_number == 0:
        federaltax = 25
        return federaltax
    elif grosspay >= 340 and grosspay < 350 and id_number == 1:
        federaltax = 8
        return federaltax
    elif grosspay >= 340 and grosspay < 350 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 350 and grosspay < 360 and id_number == 0:
        federaltax = 26
        return federaltax
    elif grosspay >= 350 and grosspay < 360 and id_number == 1:
        federaltax = 9
        return federaltax
    elif grosspay >= 350 and grosspay < 360 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 360 and grosspay < 370 and id_number == 0:
        federaltax = 27
        return federaltax
    elif grosspay >= 360 and grosspay < 370 and id_number == 1:
        federaltax = 10
        return federaltax
    elif grosspay >= 360 and grosspay < 370 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 370 and grosspay < 380 and id_number == 0:
        federaltax = 28
        return federaltax
    elif grosspay >= 370 and grosspay < 380 and id_number == 1:
        federaltax = 11
        return federaltax
    elif grosspay >= 370 and grosspay < 380 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 380 and grosspay < 390 and id_number == 0:
        federaltax = 29
        return federaltax
    elif grosspay >= 380 and grosspay < 390 and id_number == 1:
        federaltax = 12
        return federaltax
    elif grosspay >= 380 and grosspay < 390 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 390 and grosspay < 400 and id_number == 0:
        federaltax = 30
        return federaltax
    elif grosspay >= 390 and grosspay < 400 and id_number == 1:
        federaltax = 13
        return federaltax
    elif grosspay >= 390 and grosspay < 400 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 400 and grosspay < 410 and id_number == 0:
        federaltax = 31
        return federaltax
    elif grosspay >= 400 and grosspay < 410 and id_number == 1:
        federaltax = 14
        return federaltax
    elif grosspay >= 400 and grosspay < 410 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 410 and grosspay < 420 and id_number == 0:
        federaltax = 32
        return federaltax
    elif grosspay >= 410 and grosspay < 420 and id_number == 1:
        federaltax = 15
        return federaltax
    elif grosspay >= 410 and grosspay < 420 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 420 and grosspay < 430 and id_number == 0:
        federaltax = 33
        return federaltax
    elif grosspay >= 420 and grosspay < 430 and id_number == 1:
        federaltax = 16
        return federaltax
    elif grosspay >= 420 and grosspay < 430 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 430 and grosspay < 440 and id_number == 0:
        federaltax = 34
        return federaltax
    elif grosspay >= 430 and grosspay < 440 and id_number == 1:
        federaltax = 17
        return federaltax
    elif grosspay >= 430 and grosspay < 440 and id_number > 1:
        federaltax = 0
        return federaltax
    elif grosspay >= 440 and grosspay < 450 and id_number == 0:
        federaltax = 35
        return federaltax
    elif grosspay >= 440 and grosspay < 450 and id_number == 1:
        federaltax = 18
        return federaltax
    elif grosspay >= 440 and grosspay < 450 and id_number == 2:
        federaltax = 1
        return federaltax
    elif grosspay >= 440 and grosspay < 450 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 450 and grosspay < 460 and id_number == 0:
        federaltax = 36
        return federaltax
    elif grosspay >= 450 and grosspay < 460 and id_number == 1:
        federaltax = 19
        return federaltax
    elif grosspay >= 450 and grosspay < 460 and id_number == 2:
        federaltax = 2
        return federaltax
    elif grosspay >= 450 and grosspay < 460 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 460 and grosspay < 470 and id_number == 0:
        federaltax = 37
        return federaltax
    elif grosspay >= 460 and grosspay < 470 and id_number == 1:
        federaltax = 20
        return federaltax
    elif grosspay >= 460 and grosspay < 470 and id_number == 2:
        federaltax = 3
        return federaltax
    elif grosspay >= 460 and grosspay < 470 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 470 and grosspay < 480 and id_number == 0:
        federaltax = 38
        return federaltax
    elif grosspay >= 470 and grosspay < 480 and id_number == 1:
        federaltax = 21
        return federaltax
    elif grosspay >= 470 and grosspay < 480 and id_number == 2:
        federaltax = 4
        return federaltax
    elif grosspay >= 470 and grosspay < 480 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 480 and grosspay < 490 and id_number == 0:
        federaltax = 39
        return federaltax
    elif grosspay >= 480 and grosspay < 490 and id_number == 1:
        federaltax = 22
        return federaltax
    elif grosspay >= 480 and grosspay < 490 and id_number == 2:
        federaltax = 5
        return federaltax
    elif grosspay >= 480 and grosspay < 490 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 490 and grosspay < 500 and id_number == 0:
        federaltax = 41
        return federaltax
    elif grosspay >= 490 and grosspay < 500 and id_number == 1:
        federaltax = 23
        return federaltax
    elif grosspay >= 490 and grosspay < 500 and id_number == 2:
        federaltax = 6
        return federaltax
    elif grosspay >= 490 and grosspay < 500 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 500 and grosspay < 520 and id_number == 0:
        federaltax = 43
        return federaltax
    elif grosspay >= 500 and grosspay < 520 and id_number == 1:
        federaltax = 25
        return federaltax
    elif grosspay >= 500 and grosspay < 520 and id_number == 2:
        federaltax = 8
        return federaltax
    elif grosspay >= 500 and grosspay < 520 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 520 and grosspay < 540 and id_number == 0:
        federaltax = 46
        return federaltax
    elif grosspay >= 520 and grosspay < 540 and id_number == 1:
        federaltax = 27
        return federaltax
    elif grosspay >= 520 and grosspay < 540 and id_number == 2:
        federaltax = 10
        return federaltax
    elif grosspay >= 520 and grosspay < 540 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 540 and grosspay < 560 and id_number == 0:
        federaltax = 49
        return federaltax
    elif grosspay >= 540 and grosspay < 560 and id_number == 1:
        federaltax = 29
        return federaltax
    elif grosspay >= 540 and grosspay < 560 and id_number == 2:
        federaltax = 12
        return federaltax
    elif grosspay >= 540 and grosspay < 560 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 560 and grosspay < 580 and id_number == 0:
        federaltax = 52
        return federaltax
    elif grosspay >= 560 and grosspay < 580 and id_number == 1:
        federaltax = 31
        return federaltax
    elif grosspay >= 560 and grosspay < 580 and id_number == 2:
        federaltax = 14
        return federaltax
    elif grosspay >= 560 and grosspay < 580 and id_number > 2:
        federaltax = 0
        return federaltax
    elif grosspay >= 580 and grosspay < 600 and id_number == 0:
        federaltax = 55
        return federaltax
    elif grosspay >= 580 and grosspay < 600 and id_number == 1:
        federaltax = 33
        return federaltax
    elif grosspay >= 580 and grosspay < 600 and id_number == 2:
        federaltax = 16
        return federaltax
    elif grosspay >= 580 and grosspay < 600 and id_number > 2:
        federaltax = 0
        return federaltax

def reportquestion():
    screen_report = input("Would you like to see recent hours? ").lower()
    screen_report_answer = screen_report[0]
    if screen_report_answer == 'y':
        create_report(person)
        subprocess.call('pr '+ person+'report.txt' , shell = True)
        print("Scroll up to see the report\n")
        report = input("Would you like to print a physical report? ").lower()
        answer = report[0]
        if answer == 'y':
            subprocess.call('scp '+ person+'report.txt rodeaton@rods-mbp:/Users/rodeaton', shell = True)
            subprocess.call('ssh rodeaton@rods-mbp lpr '+ person + 'report.txt', shell = True)
            subprocess.call('ssh rodeaton@rods-mbp lpr '+ person + 'report.txt', shell = True)
            # opens connection on mac and prints two copies
            print("Printing 2 copies.")
            time.sleep(3)
            os.remove(person+'report.txt')
        else:
            os.remove(person+'report.txt')

    else:
        report = input("Would you like to print a physical report? ").lower()
        answer = report[0]
        if answer == 'y':
            create_report(person)
            subprocess.call('scp '+ person+'report.txt rodeaton@rods-mbp:/Users/rodeaton', shell = True)
            subprocess.call('ssh rodeaton@rods-mbp lpr '+ person + 'report.txt', shell = True)
            print("Printing.")
            time.sleep(3)
            os.remove(person+'report.txt')

def delete_employee():
    employee_name_file = open('employee_firstname_file.py', 'r')
    read_the_file = employee_name_file.readline()
    decode_data = json.loads(read_the_file)
    employee_name_file.close()
    remove_employee = input("Enter the first name of the employee you want to remove:")
    array_length = len(decode_data)
    for name in range(array_length):
        search = decode_data[name]
        if remove_employee == search:
            location = decode_data.index(remove_employee)
            break
    employee_firstname_file = open('employee_firstname_file.py' ,'w')
    decode_data.remove(remove_employee)
    encode_name = json.dumps(decode_data)
    employee_firstname_file.write(encode_name)
    employee_firstname_file.close()
    employee_lastname_file = open('employee_lastname_file.py', 'r')
    read_the_file = employee_lastname_file.readline()
    decode_data = json.loads(read_the_file)
    employee_lastname_file.close()
    remove_item = decode_data[location]
    decode_data.remove(remove_item)
    employee_lastname_file = open('employee_lastname_file.py' , 'w')
    encode_item = json.dumps(decode_data)
    employee_lastname_file.write(encode_item)
    employee_lastname_file.close()
    employee_pay_file = open('employee_pay_file.py' , 'r')
    read_the_file = employee_pay_file.readline()
    decode_data = json.loads(read_the_file)
    employee_pay_file.close()
    remove_item = decode_data[location]
    decode_data.remove(remove_item)
    employee_pay_file = open('employee_pay_file.py' , 'w')
    encode_item = json.dumps(decode_data)
    employee_pay_file.write(encode_item)
    employee_pay_file.close()
    employee_withholding_file = open('employee_withholding_file.py' , 'r')
    read_the_file = employee_withholding_file.readline()
    decode_data = json.loads(read_the_file)
    employee_withholding_file.close()
    remove_item = decode_data[location]
    decode_data.remove(remove_item)
    employee_withholding_file = open('employee_withholding_file.py' , 'w')
    encode_item = json.dumps(decode_data)
    employee_withholding_file.write(encode_item)
    employee_withholding_file.close()
    print(remove_employee.upper()+' ' +'has been removed from the database!')
    time.sleep(2)

def move_files():
    employee_name_file = open("employee_firstname_file.py" , 'r')
    data = employee_name_file.readline()
    decode_the_data = json.loads(data)
    print(decode_the_data)
    length = len(decode_the_data)
    for names in range(length):
        subprocess.call("mv -f " + data[names] + 'inout.txt' , shell = True)
        print(data[names])
        print(data[names] + 'has been moved to /Users/Kyle/Desktop/folder')
        time.sleep(4)

def insert_time():
    insert_time_dict = {}
    employee = input("Enter the firstname of the employee to add the time to.").lower()
    timefile_read = open(employee + "inout.txt", 'r')
    objectsArray = timefile_read.readlines()
    timefile_read.close()
    theLength = len(objectsArray)
    for eachObject in range(theLength):
        print('Index = '+str(eachObject)+'  '+objectsArray[eachObject])
    insert_index = int(input("Enter the index number where you want the new time added: "))
    newtime = input("Enter the date (mm/dd/yyyy): ")
    time_in = input("Enter the time in. (12 hour clock)  (hh:mm)")
    am_or_pm = input("AM or PM?").lower()
    if am_or_pm == 'pm':
        the_in_hours = time_in[0:2]
        if time_in[0]== '0':
            the_in_hours = time_in[1:2]
        if str(the_in_hours) == '12':
            time_in = time_in
        else:
            to_military = eval(the_in_hours)
            military_time = str(to_military + 12)
            minutes_to_add = time_in[2:5]
            time_in = military_time + minutes_to_add

    time_out = input("Enter the time out (12 hour clock)  (hh:mm)")
    am_or_pm = input("AM or PM?").lower()
    if am_or_pm == 'pm':
        the_out_hours = time_out[0:2]
        if time_out[0]== '0':
            the_out_hours = time_out[1:2]
        if str(the_out_hours) == '12':
            time_in = time_in
        else:
            to_military = eval(the_out_hours)
            military_time = str(to_military + 12)
            minutes_to_add = time_out[2:5]
            time_out = military_time + minutes_to_add

    insert_time_dict['OUT'] = time_out
    insert_time_dict['DATE'] = newtime
    insert_time_dict['IN'] = time_in
    timefile = open(employee + "inout.txt", 'w')
    timefile.close()
    timefile = open(employee + "inout.txt", 'a')

    for eachObject in range(theLength):
        if eachObject == insert_index:
            encode_json = json.dumps(insert_time_dict)
            timefile.write(encode_json + '\n')

        timefile.write(objectsArray[eachObject])

    timefile.close()
    print("Time has been inserted to "+employee.upper()+"'s file.")
    time.sleep(3)
    #encode_json = json.dumps(insert_time_dict)

def delete_time():
    delete_time_dict = {}
    employee = input("Enter the firstname of the employee where you want to delete time.").lower()
    timefile_read = open(employee + "inout.txt", 'r')
    objectsArray = timefile_read.readlines()
    timefile_read.close()
    theLength = len(objectsArray)
    for eachObject in range(theLength):
        print('Index = '+str(eachObject)+'  '+objectsArray[eachObject])
    index = int(input("Choose the index."))
    del objectsArray[index]
    timefile = open(employee + "inout.txt", 'w')
    timefile.close()
    timefile = open(employee + "inout.txt", 'a')
    for eachObject in range(theLength-1):
        timefile.write(objectsArray[eachObject])
    timefile.close()

X = True
while X:
    try:
        subprocess.call("tput reset", shell = True)
        employee = input("Please enter your first name: ").lower()
        if employee == 'admin':
            Y = True
            while Y:
                subprocess.call("tput reset", shell = True)
                person = input("Enter firstname of employee to see recent info.\n'add' to add employee. \n'remove' to remove employee.\n'add time' to add time to end\n'insert' to insert time in a specific place\n'hours' for total hours\n'delete' to erase all time files.\n--->").lower()
                if person == 'add':
                    try:
                        add_employee()
                    #except FileNotFoundError:
                    #    add_first_employee()
                    except IOError:
                        add_first_employee()
                elif person == 'remove':
                    delete_employee()
                elif person == 'delete':
                    print("trying")
                    move_files()
                elif person == 'exit':
                    Y = False
                    X = False
                elif person == 'add time':
                    add_time()
                elif person == 'hours':
                    employeeHr = input("Which employee? ")
                    print_total_hours()
                    input()
                elif person == 'insert':
                    insert_time()
                elif person == 'delete time':
                    delete_time()
                else:
                    name_file = open('employee_firstname_file.py', 'r')
                    getnames = name_file.readline()
                    name_file.close()
                    decode_names = json.loads(getnames)
                    array_length = len(decode_names)
                    for name in range(array_length):
                        search = decode_names[name]
                        if person == search:
                            location = decode_names.index(person)
                            lastname_file = open('employee_lastname_file.py', 'r')
                            get_lastname = lastname_file.readline()
                            lastname_file.close()
                            decode_json = json.loads(get_lastname)
                            lastname = decode_json[location]

                            pay_file = open('employee_pay_file.py', 'r')
                            get_pay = pay_file.readline()
                            pay_file.close()
                            decode_pay_json = json.loads(get_pay)
                            pay_string = decode_pay_json[location]
                            pay = eval(pay_string)

                            id_file = open('employee_withholding_file.py', 'r')
                            get_id = id_file.readline()
                            id_file.close()
                            decode_id_json = json.loads(get_id)
                            id_number_string = decode_id_json[location]
                            id_number = eval(id_number_string)
                            reportquestion()
                            break
        else:
            name_file = open('employee_firstname_file.py', 'r')
            getnames = name_file.readline()
            name_file.close()
            decode_names = json.loads(getnames)
            array_length = len(decode_names)
            for name in range(array_length):
                search = decode_names[name]
                if employee == search:
                    checkaction()
                    break

    except KeyboardInterrupt:
        continue
    #except FileNotFoundError:
        #print("Employee has no file on system.")
        #time.sleep(2)
        #continue
    '''except IOError:
        print("Employee has no file on the system.")
        time.sleep(2)
        continue'''
