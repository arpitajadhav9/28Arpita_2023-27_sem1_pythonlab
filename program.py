#WAP TO CALCULATE PARKING CHARGES OF A VEHICLE.ENTER THE TYPE OF VEHICLE AS A CHARACTER (C FOR CAR , B FOR BUS,ETC).
# AND NO OF HOURS , THEN CALCULATE CHARGES AS GIVEN BELOW:
# TRUCK/BUS = 20 Rs per hr
# CAR = 10 Rs per hr
# SCOOTER/CYCLE/BIKE = 5 Rs per hr.
#MODIFY THE ABOVE PROGRAM



# vehicle_type = ['truck','bus','scooter','car','cycle','bike']
# print(vehicle_type)

# vehicle_type = str(input("Enter the type of vehicle: "))




# no_of_hours = int(input("Enter the number of hours: "))


# charge1 = 20 * no_of_hours
# charge2 = 10 * no_of_hours
# charge3 = 5 * no_of_hours

# if vehicle_type == 'truck' or vehicle_type == 'bus':
#     print("Parking charges = ","₹",charge1)
    
# elif vehicle_type == 'car':
#     print("Parking charge = ","₹",charge2)

# elif vehicle_type == 'scooter' or vehicle_type == 'cycle' or vehicle_type == 'bike':
#     print("Parking charge = ","₹" ,charge3)
# else:
#     print("NOT VALID")



# MODIFIED PROGRAM:
car_no = int(input("Enter the car no: "))

vehicle = ['truck','bus','scooter','car','cycle','bike']
print(vehicle)

vehicle = str(input("Enter the type of vehicle: ")).lower()

entry_time = float(input("Enter the entry time:" ))
exit_time = float(input("Enter the exit time: "))


hours = (exit_time - entry_time)


charge1 = 20 * hours
charge2 = 10 * hours
charge3 = 5 * hours


if vehicle == 'truck' or vehicle == 'bus':
        if hours<3:
         print("Parking charges = ","₹",charge1)
        elif hours >=3:
         total=charge1+30
         print("Parking charges = ","₹",total)
    
elif vehicle == 'car':
    if hours<3:
       print("Parking charge = ","₹",charge2)
    elif hours>=3:
        total=charge2+20
        print("Parking charge = ","₹",total)


elif vehicle == 'scooter' or vehicle == 'cycle' or vehicle == 'bike':
    if hours<3:
     print("Parking charge = ","₹" ,charge3)
    elif hours>=3:
       total=charge3+10
       print("Parking charge = ","₹" ,total)
      
else:
    print("NOT VALID")

print("-------------CAR RECIEPT------------")
print("| VEHICLE NUMBER: ",   car_no )  
print("| VEHICLE TYPE: ",     vehicle)
print("| ENTRY TIME: ",       entry_time)
print("| EXIT TIME: ",        exit_time)
print("| TOTAL NO OF HOURS: ",hours)
print("| PARKING CHARGE:₹",total)
print("-------------------------------")
