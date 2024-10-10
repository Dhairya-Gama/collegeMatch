import csv


def get_college_stats(str_name):
     
    list = []
    final_list = []
    ans = ""
    with open('college.csv', 'r', encoding='utf-8') as file:
        csv_file = csv.DictReader(file)

        for i in csv_file:
            if str_name.lower() in i["Institution Name"].lower():
                list.append(i)


    if len(list) > 25:
        return "Too many results. Please make the search more specified"

    elif len(list) > 1:
        for i in range (len(list)):
            print("[" + str(i +1) + "] " + list[i]["Institution Name"])

            print("")
            new_num = input("Select [1-" + str(len(list)) + "]" + "\n")
        

        if int(new_num) < 1 or int(new_num) > len(list):
            return "Error. Selected number not in list bounds"
        
        else:
            final_list.append(list[int(new_num)-1]) 
    
    else:
        final_list.append(list[0]) 



        resultName = final_list[0]["Institution Name"]
        ans = "Here are the average stats for " + resultName + ": \n Average SAT score for males: " + final_list[0]["Average SAT for males"]  + ": \n Average SAT score for females: " + final_list[0]["Average SAT for females"] + ": \n Average GPA for males: " + final_list[0]["Average GPA for males"] + ": \n Average GPA for females: " + final_list[0]["Average GPA for females"] + ": \n Average AP classes for males: " + final_list[0]["Average number of AP Classes as male"] + ": \n Average AP classes for females: " + final_list[0]["Average number of AP Classes as female"] + ": \n Average Number of Extracurriculars: " + final_list[0]["Average number of Extracurriculars"]
        return ans



def specific_college(name, gender, sat_score, gpa, num_ap, num_ec):
    list = []
    col_list = []
    ans = ""
    with open('college.csv', 'r', encoding='utf-8') as file:
        csv_file = csv.DictReader(file)

        for i in csv_file:
            if name.lower() in i["Institution Name"].lower():
                col_list.append(i)

        if (len(col_list) > 1 or len(col_list) == 0):
            return "Please give us the exact college name."
    
        else:
        
            if (gender.lower() == "male"):
                if(int(col_list[0]["Average SAT for males"]) > int(sat_score)):
                    list.append("No")
                else:
                    list.append("Yes")

                if(float(col_list[0]["Average GPA for males"]) > float(gpa)):
                    list.append("No")
                else:
                    list.append("Yes")

                if(int(col_list[0]["Average number of AP Classes as male"]) > int(num_ap)):
                    list.append("No")
                else:
                    list.append("Yes")
                
            else:
                if(int(col_list[0]["Average SAT for females"]) > int(sat_score)):
                    list.append("No")
                else:
                    list.append("Yes")

                if(float(col_list[0]["Average GPA for females"]) > float(gpa)):
                    list.append("No")
                else:
                    list.append("Yes")

                if(int(col_list[0]["Average number of AP Classes as female"]) > int(num_ap)):
                    list.append("No")
                else:
                    list.append("Yes")
            
            if (int(col_list[0]["Average number of Extracurriculars"]) > int(num_ec)):
                list.append("No")
            else:
                list.append("Yes")

            ans = "Here are your results: \n" + "Is your SAT higher than the average: " + list[0] + "\n Is your GPA higher than the average: " + list[1] + "\n Is the number of AP classes you have taken higher than the average: " + list[2] + "\n Is the number of your extracurriculars higher than the average: " + list[3]

            return ans





def list_colleges(gender, sat_score, gpa, num_ap, num_ec):
    list = []
    col_list = []
    ans = ""
    with open('college.csv', 'r', encoding='utf-8') as file:
        csv_file = csv.DictReader(file)

        
        if gender.lower() == "male":
            for i in csv_file:
                if( int(i["Average SAT for males"]) < int(sat_score) and float(i["Average GPA for males"]) < float(gpa) and int(i["Average number of AP Classes as male"]) < int(num_ap) and int(i["Average number of Extracurriculars"]) < int(num_ec)):
                    col_list.append(i)

                for x in range(len(col_list)):
                    temp = x+1
                    ans += "[" + str(temp) + "]" + col_list[x]["Institution Name"] + "\n"
                
        
            else:
                for i in csv_file:
                    if( int(i["Average SAT for females"]) < int(sat_score) and float(i["Average GPA for females"]) < float(gpa) and int(i["Average number of AP Classes as female"]) < int(num_ap) and int(i["Average number of Extracurriculars"]) < int(num_ec)):
                        col_list.append(i)

                    for x in range(len(col_list)):
                        temp = x+1
                        ans += "[" + str(temp) + "]" + col_list[x]["Institution Name"] + "\n"
    
    return ans




               
        






















num_choice = input("Choose 1 of the following: \n [1] Get average stats for a specific college \n [2] See if your stats are above average for a specific college \n [3] Get a list of colleges where you are above average \n")

if (int(num_choice) == 1):
    name =  input("Enter the name of the university you're interested in: ")
   
    print(get_college_stats(name))

elif (int(num_choice) == 2):
    name =  input("Enter the exact name of the university you're interested in: ")
    gender = input("Male or Female: ")
    

    
    sat_score = input("What was your SAT score: ")
   
    
    gpa = input("What is your gpa: ")
    num_ap = input("How many AP Classes have you taken: ")
    num_ec = input("How many extracurriculars are you involved in: ")

    print(specific_college(name, gender, sat_score, gpa, num_ap, num_ec))







elif (int(num_choice) == 3):
    
    gender = input("Male or Female: ")
    sat_score = input("What was your SAT score: ")
   
    
    gpa = input("What is your gpa: ")
    num_ap = input("How many AP Classes have you taken: ")
    num_ec = input("How many extracurriculars are you involved in: ")

    print(list_colleges(gender, sat_score, gpa, num_ap, num_ec))