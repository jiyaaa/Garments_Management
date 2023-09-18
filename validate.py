check_counter=0
warn = ""

if register_name.get() == "":
   warn = "Name can't be empty"
else:
    check_counter += 1
check_counter=0
        
if register_email.get() == "":
    warn = "Email can't be empty"
else:
    check_counter += 1

if register_mobile.get() == "":
   warn = "Contact can't be empty"
else:
    check_counter += 1
    
if  var.get() == "":
    warn = "Select Gender"
else:
    check_counter += 1

if variable.get() == "":
   warn = "Select Country"
else:
    check_counter += 1

if register_pwd.get() == "":
    warn = "Password can't be empty"
else:
    check_counter += 1

if pwd_again.get() == "":
    warn = "Re-enter password can't be empty"
else:
    check_counter += 1