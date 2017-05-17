import pyxnat, os
# connect to xnat instance. Enter server and then username and password or config file)
xnat=pyxnat.Interface(server=server_URL)

# Define project name, subject label
PROJECT='MBAM_TEST'
SUBJECT='0001'
EXPERIMENT='0001_MR1'

proj_obj=xnat.select.project(PROJECT)

# Below will print all the custom variable names (at Subject and Experiment level)
print proj_obj.get_custom_variables() 

# Create subject and experiment objects, and verify they exist
sub_obj=proj_obj.subject(SUBJECT) 
exp_obj=sub_obj.experiment(EXPERIMENT)
print sub_obj.exists()
print exp_obj.exists()

# Below is syntax for setting and retrieving custom variable 'sub_var1' at the Subject level
# Note custom variables are case insensitive, so should always use lower case letters and with underscores
sub_obj.attrs.set("xnat:subjectData/fields/field[name='sub_var1']/field",'150')
val = sub_obj.xpath("/xnat:Subject/xnat:fields/xnat:field[@name='sub_var1']/text()[2]")

# Below command should print out '150'
print val

# Below is syntax for setting and retrieving custom variable 'exp_var1' at the Experiment level
exp_obj.attrs.set("xnat:mrSessionData/fields/field[name='exp_var1']/field",'100')
val = exp_obj.xpath("/xnat:MRSession/xnat:fields/xnat:field[@name='exp_var1']/text()[2]")

# Below should print out '100'
print val
