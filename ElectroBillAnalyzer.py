Industry_single_Time_Unit_Energy_fee = 305.3828 / 100
Industry_Daytime_Period_Units_Energy_fee = 309.1833 / 100
Industry_Peak_Period_Unit_Energy_fee = 490.9037 / 100
Industry_Night_Period_Unit_Energy_fee = 162.5171 / 100
Industry_Unit_distribution_fee = 64.7998 / 100
Industry_ECT_rate = 0.01
Industry_VAT_rate = 0.2
Public_and_Private_Services_Sector_and_Other_Single_low_tariff_fee = 191.2220 / 100
Public_and_Private_Services_Sector_and_Other_Single_High_tariff_fee = 282.8414 / 100
Public_and_Private_Services_Sector_and_Other_Daytime_fee = 285.8616 / 100
Public_and_Private_Services_Sector_and_Other_Peak_period_fee = 458.8843 / 100
Public_and_Private_Services_Sector_and_Other_Night_period_fee = 148.1941 / 100
Public_and_Private_Services_Sector_and_Other_Unit_Distribution_fee = 87.8175 / 100
Public_and_Private_Services_Sector_and_Other_limit = 30 #Public and private services sector and other daily consumption limit
Public_and_Private_Services_Sector_and_Other_ECT_rate = 0.05
Public_and_Private_Services_Sector_and_Other_VAT_rate = 0.2
Residental_limit = 8 #Residential type daily consumption limit
Residential_low_tariff_Single_fee = 48.2187 / 100
Residential_high_tariff_Single_fee = 113.2271 / 100
Residential_Daytime_Period_Units_fee = 115.7700 / 100
Residential_Peak_Period_Unit_fee = 208.3645 / 100
Residential_Night_Period_Unit_fee = 41.7225 / 100
Residential_Unit_Distribution_Fee = 85.8883 / 100
Residental_Family_of_martyrs_and_veterans_fee = 6.1590 / 100
Residental_Family_of_martyrs_and_veterans_Unit_Distribution_fee = 58.2521 / 100
Residental_ECT_rate = 0.05
Residental_VAT_rate = 0.1
Agricultural_Activities_Single_time_fee = 165.3096 / 100
Agricultural_Activities_Daytime_Period_Units_fee = 170.4822 / 100
Agricultural_Activities_Peak_Period_Unit_fee = 280.0325 / 100
Agricultural_Activities_Night_Period_Unit_fee = 77.1882 / 100
Agricultural_Activities_Unit_Distribution_fee = 72.1579 / 100
Agricultural_ECT_rate = 0.05
Agricultural_VAT_rate = 0.1
Lighting_Unit_fee = 259.5835 / 100
Lighting_Unit_Distribution_fee = 84.1099 / 100
Lighting_ECT_rate = 0.05
Lighting_VAT_rate = 0.2
Is_Family_Of_martyrs_and_veterans = 'n' #The reason I define it here is because it returns null in some cases.
Is_multi_time_or_single_time_tariff = 'q' #The reason I define it here is because it returns null in some cases.

Count_Industry_consumer = 0
Total_Industry_Consumption = 0
Count_Public_consumer = 0
Total_Public_Consumption = 0
Count_Residential_consumer = 0
Total_Residential_Consumption = 0
Count_Agricultural_consumer = 0
Total_Agricultural_Consumption = 0
Count_Lighting_consumer = 0
Total_Lighting_Consumption = 0
Total_Consumers = 0
Total_Consumption = 0 #Total consumption of all consumers
Count_Public_multi_consumer = 0
Count_Public_single_consumer = 0
Total_Public_days = 0 #Total days of all entered periods
Count_Industry_fee_or_consumption_over_10k = 0
Residential_Highest_daily_consumer_no = 0
Residential_Highest_daily_invoice_fee = 0
Residential_Highest_Daily_Consumption = 0
Highest_invoice_fee = 0
Highest_invoice_consumer_no = 0
Highest_invoice_consumer_type = 't'
Highest_invoice_consumption_amount_daily_avr = 0
GDZ_Corporation_total_revenue_amount = 0
The_Municipality_total_revenue_amount = 0
The_State_total_revenue_amount = 0
Count_who_made_loss = 0 # Number of consumers who made a loss despite choosing multi-time tariff
Total_count_Multi_time_prefered = 0 # Number of all consumers who prefered multi-time tariff
def Get_invoice_Information(): #Getting invoice informations
    global Is_Family_Of_martyrs_and_veterans
    global Is_multi_time_or_single_time_tariff
    global Consumer_no
    Is_Family_Of_martyrs_and_veterans = 'n' #I wrote it so that it is reset every time a consumer is logged in.
    while(Consumer_no < 0):
        print("Invalid Consumer No!")
        Consumer_no = int(input("Enter your Consumer No: "))
   
    Consumer_Type_Code = input("Enter your Consumer Type Code (I,i,P,p,R,r,A,a,L,l): ")
    
    while(not Consumer_Type_Code in ['I','i','P','p','R','r','A','a','L','l']):
        print("Invalid Consumer Type!")
        Consumer_Type_Code = input("Enter your Consumer Type Code (I,i,P,p,R,r,A,a,L,l): ")

    if(Consumer_Type_Code == 'R' or Consumer_Type_Code == 'r'): #Consumer type Residential check if the consumer is family of martyrs or veterans
        Is_Family_Of_martyrs_and_veterans = input("Are you Family Of martyrs or veterans? (y/n) ")
        while(not Is_Family_Of_martyrs_and_veterans in ['Y','y','N','n']):      
            print("Invalid input!")
            Is_Family_Of_martyrs_and_veterans = input("Are you Family Of martyrs or veterans? (y/n) ")
        if(Is_Family_Of_martyrs_and_veterans in ['N','n']): #If the consumer is not family of martyrs or veterans take tariff selection
            Is_multi_time_or_single_time_tariff = input("Which tariff do you prefer single time or multi time (S/s/m/M): ")
            while( not Is_multi_time_or_single_time_tariff in ['S','s','M','m']):
                print("Invalid Input!")
                Is_multi_time_or_single_time_tariff = input("Which tariff do you prefer single time or multi time (S/s/m/M): ")
        
    if(Consumer_Type_Code in ['I','i','P','p','A','a']): #If consumer type Industry or public or agricultural take tariff selection
        Is_multi_time_or_single_time_tariff = input("Which tariff do you prefer single time or multi time (S/s/m/M): ")
        while( not Is_multi_time_or_single_time_tariff in ['S','s','M','m']):
            print("Invalid Input!")
            Is_multi_time_or_single_time_tariff = input("Which tariff do you prefer single time or multi time (S/s/m/M): ")
    #Taking daytime,peak and night periods consumption
    Previous_daytime_period_meter_value = int(input("Enter Previous daytime period meter value: "))
    while(Previous_daytime_period_meter_value < 0):
        print("Invalid Daytime Period Meter Value!")
        Previous_daytime_period_meter_value = int(input("Enter Previous daytime period meter value: "))
    
    Current_daytime_period_meter_value = int(input("Enter Current daytime period meter value: "))
    while(Current_daytime_period_meter_value < Previous_daytime_period_meter_value):
        print("Current daytime period meter value should be greater than previous daytime period meter value!(or equal)")
        Current_daytime_period_meter_value = int(input("Enter Current daytime period meter value: "))

    Previous_peak_period_meter_value = int(input("Enter Previous peak period meter value: "))
    while(Previous_peak_period_meter_value < 0):
        print("Invalid Peak Period Meter Value!")
        Previous_peak_period_meter_value = int(input("Enter Previous peak period meter value: "))
    
    Current_peak_period_meter_value = int(input("Enter Current peak period meter value: "))
    while(Current_peak_period_meter_value < Previous_peak_period_meter_value):
        print("Current peak period meter value should be greater than previous peak period meter value!(or equal)")
        Current_peak_period_meter_value = int(input("Enter Current peak period meter value: "))

    Previous_night_period_meter_value = int(input("Enter Previous night period meter value: "))
    while(Previous_night_period_meter_value < 0):
        print("Invalid Night Period Meter Value!")
        Previous_night_period_meter_value = int(input("Enter Previous night period meter value: "))
    
    Current_night_period_meter_value = int(input("Enter Current night period meter value: "))
    while(Current_night_period_meter_value < Previous_night_period_meter_value):
        print("Current night period meter value should be greater than previous night period meter value(or equal)")
        Current_night_period_meter_value = int(input("Enter Current night period meter value: "))

    Number_of_days_between_previous_and_current_meter_reading_dates = int(input("Enter Number of days between previous and current meter reading dates: "))
    while(Number_of_days_between_previous_and_current_meter_reading_dates <= 0):
        print("Invalid input!")
        Number_of_days_between_previous_and_current_meter_reading_dates = int(input("Enter Number of days between previous and current meter reading dates: "))
    
    Total_amount_of_electricity_Until_this_period = int(input("Enter Total amount of electricity consumption in the current year until this period: ")) #Total electricity consumption in this year
    while(Total_amount_of_electricity_Until_this_period < 0):
        print("Invalid input!")
        Total_amount_of_electricity_Until_this_period = int(input("Enter Total amount of electricity consumption in the current year until this period: "))
    
    Daytime_period_electricity_consumption_amount = Current_daytime_period_meter_value - Previous_daytime_period_meter_value
    Peak_period_electricity_consumption_amount = Current_peak_period_meter_value - Previous_peak_period_meter_value
    Night_period_electricity_consumption_amount = Current_night_period_meter_value - Previous_night_period_meter_value
    Total_electricity_consumption_amount = Daytime_period_electricity_consumption_amount + Peak_period_electricity_consumption_amount + Night_period_electricity_consumption_amount
        
        
    
    return Consumer_no,Consumer_Type_Code,Is_Family_Of_martyrs_and_veterans,Daytime_period_electricity_consumption_amount,Peak_period_electricity_consumption_amount,Night_period_electricity_consumption_amount,Total_electricity_consumption_amount,Number_of_days_between_previous_and_current_meter_reading_dates,Total_amount_of_electricity_Until_this_period,Is_multi_time_or_single_time_tariff

def invoice_calculation (Consumer_no,Consumer_Type_Code,Is_Family_Of_martyrs_and_veterans,Daytime_period_electricity_consumption_amount,Peak_period_electricity_consumption_amount,Night_period_electricity_consumption_amount,Total_electricity_consumption_amount,Number_of_days_between_previous_and_current_meter_reading_dates,Total_amount_of_electricity_Until_this_period,Is_multi_time_or_single_time_tariff):
    global Count_Industry_consumer
    global Total_Industry_Consumption
    global Count_Public_consumer
    global Total_Public_Consumption
    global Count_Residential_consumer
    global Total_Residential_Consumption
    global Count_Agricultural_consumer
    global Total_Agricultural_Consumption
    global Count_Lighting_consumer
    global Total_Lighting_Consumption
    global Total_Consumers
    global Total_Consumption
    global Count_Public_multi_consumer
    global Count_Public_single_consumer
    global Count_Industry_fee_or_consumption_over_10k
    global Residential_Highest_daily_consumer_no
    global Residential_Highest_Daily_Consumption
    global Residential_Highest_daily_invoice_fee
    global Highest_invoice_consumer_type
    global Highest_invoice_consumer_no
    global Highest_invoice_consumption_amount_daily_avr
    global Highest_invoice_fee
    global GDZ_Corporation_total_revenue_amount
    global The_Municipality_total_revenue_amount
    global The_State_total_revenue_amount
    global Total_Public_days

    if(Consumer_Type_Code == 'I' or Consumer_Type_Code == 'i'):#Industry type
        Count_Industry_consumer += 1 #Counting the number of industry consumers
        Total_Industry_Consumption += Total_electricity_consumption_amount #Total industry consumption of all consumers
        Daytime_period_fee = Daytime_period_electricity_consumption_amount * Industry_Daytime_Period_Units_Energy_fee
        Peak_period_fee = Peak_period_electricity_consumption_amount * Industry_Peak_Period_Unit_Energy_fee
        Night_period_fee = Night_period_electricity_consumption_amount * Industry_Night_Period_Unit_Energy_fee
        Distribution_fee = Total_electricity_consumption_amount * Industry_Unit_distribution_fee
        Multi_time_fee = Daytime_period_fee + Peak_period_fee + Night_period_fee
        Single_time_fee = Total_electricity_consumption_amount * Industry_single_Time_Unit_Energy_fee
        ECT_Amount_Single = Single_time_fee * Industry_ECT_rate
        ECT_Amount_Multi = Multi_time_fee * Industry_ECT_rate
        VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Industry_VAT_rate
        VAT_Amount_Multi = (Multi_time_fee + ECT_Amount_Multi + Distribution_fee) * Industry_VAT_rate
        if(Total_electricity_consumption_amount > 10000 or (Single_time_fee + Distribution_fee + ECT_Amount_Single + VAT_Amount_Single) > 100000 or (Multi_time_fee + Distribution_fee + ECT_Amount_Multi + VAT_Amount_Multi) > 100000):
            Count_Industry_fee_or_consumption_over_10k += 1 #Counting the number of whose industry invoice fee above 100000 tl or whose electricity consumption above 10000 kWh
    elif(Consumer_Type_Code == 'P' or Consumer_Type_Code == 'p'): #Public and private services sector and other type
        Count_Public_consumer += 1 #Counting the number of Public and private services sector and other consumers
        Total_Public_Consumption += Total_electricity_consumption_amount #Total Public and private services sector and other consumption of all consumers
        Total_Public_days += Number_of_days_between_previous_and_current_meter_reading_dates #Total days of all entered periods
        if(Is_multi_time_or_single_time_tariff in ['M','m']):
            Count_Public_multi_consumer += 1 #Total consumers who prefered Multi time tariff
        else:
            Count_Public_single_consumer += 1 #Total consumers who prefered Single time tariff   
        if(Public_and_Private_Services_Sector_and_Other_limit < Total_electricity_consumption_amount / Number_of_days_between_previous_and_current_meter_reading_dates): #Checking Daily consumption limit
            #Calculating fee's amounts daily consumption above daily limit
            Single_time_fee = Public_and_Private_Services_Sector_and_Other_Single_low_tariff_fee * Public_and_Private_Services_Sector_and_Other_limit + (Total_electricity_consumption_amount / Number_of_days_between_previous_and_current_meter_reading_dates - Public_and_Private_Services_Sector_and_Other_limit) * Public_and_Private_Services_Sector_and_Other_Single_High_tariff_fee
            Daytime_period_fee = Daytime_period_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Daytime_fee
            Peak_period_fee = Peak_period_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Peak_period_fee
            Night_period_fee = Night_period_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Night_period_fee
            Distribution_fee = Total_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Unit_Distribution_fee
            Multi_time_fee = Daytime_period_fee + Peak_period_fee + Night_period_fee
            ECT_Amount_Single = Single_time_fee * Public_and_Private_Services_Sector_and_Other_ECT_rate
            ECT_Amount_Multi = Multi_time_fee * Public_and_Private_Services_Sector_and_Other_ECT_rate
            VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Public_and_Private_Services_Sector_and_Other_VAT_rate
            VAT_Amount_Multi = (Multi_time_fee + ECT_Amount_Multi + Distribution_fee) * Public_and_Private_Services_Sector_and_Other_VAT_rate
        else:
            #Calculating fee's amounts daily consumption under daily limit
            Single_time_fee = Total_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Single_low_tariff_fee
            Daytime_period_fee = Daytime_period_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Daytime_fee
            Peak_period_fee = Peak_period_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Peak_period_fee
            Night_period_fee = Night_period_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Night_period_fee
            Distribution_fee = Total_electricity_consumption_amount * Public_and_Private_Services_Sector_and_Other_Unit_Distribution_fee
            Multi_time_fee = Daytime_period_fee + Peak_period_fee + Night_period_fee
            ECT_Amount_Single = Single_time_fee * Public_and_Private_Services_Sector_and_Other_ECT_rate
            ECT_Amount_Multi = Multi_time_fee * Public_and_Private_Services_Sector_and_Other_ECT_rate
            VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Public_and_Private_Services_Sector_and_Other_VAT_rate
            VAT_Amount_Multi = (Multi_time_fee + ECT_Amount_Multi + Distribution_fee) * Public_and_Private_Services_Sector_and_Other_VAT_rate   

    elif(Consumer_Type_Code == 'R' or Consumer_Type_Code == 'r'):#Residential type
        Count_Residential_consumer += 1 #Counting the number of Residential consumers
        Total_Residential_Consumption += Total_electricity_consumption_amount #Total Residential consumption of all consumers

        if(Is_Family_Of_martyrs_and_veterans == 'Y' or Is_Family_Of_martyrs_and_veterans == 'y'): #Checking if family of martyrs or veterans
            Single_time_fee = Total_electricity_consumption_amount * Residental_Family_of_martyrs_and_veterans_fee
            Distribution_fee = Total_electricity_consumption_amount * Residental_Family_of_martyrs_and_veterans_Unit_Distribution_fee
            ECT_Amount_Single = Single_time_fee * Residental_ECT_rate
            VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Residental_VAT_rate
            Multi_time_fee = 0 #The reason I put it here is because it returns the value none
            ECT_Amount_Multi = 0 #The reason I put it here is because it returns the value none
            VAT_Amount_Multi = 0 #The reason I put it here is because it returns the value none           
        
        elif(Residental_limit < Total_electricity_consumption_amount / Number_of_days_between_previous_and_current_meter_reading_dates): #Checking Daily consumption limit
            Single_time_fee = Residential_low_tariff_Single_fee * Residental_limit + (Total_electricity_consumption_amount / Number_of_days_between_previous_and_current_meter_reading_dates - Residental_limit) * Residential_high_tariff_Single_fee
            Daytime_period_fee = Daytime_period_electricity_consumption_amount * Residential_Daytime_Period_Units_fee
            Peak_period_fee = Peak_period_electricity_consumption_amount * Residential_Peak_Period_Unit_fee
            Night_period_fee = Night_period_electricity_consumption_amount * Residential_Night_Period_Unit_fee
            Distribution_fee = Total_electricity_consumption_amount * Residential_Unit_Distribution_Fee
            Multi_time_fee = Daytime_period_fee + Peak_period_fee + Night_period_fee
            ECT_Amount_Single = Single_time_fee * Residental_ECT_rate
            ECT_Amount_Multi = Multi_time_fee * Residental_ECT_rate
            VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Residental_VAT_rate
            VAT_Amount_Multi = (Multi_time_fee + ECT_Amount_Multi + Distribution_fee) * Residental_VAT_rate 
        else:
            Single_time_fee = Residential_low_tariff_Single_fee * Total_electricity_consumption_amount
            Daytime_period_fee = Daytime_period_electricity_consumption_amount * Residential_Daytime_Period_Units_fee
            Peak_period_fee = Peak_period_electricity_consumption_amount * Residential_Peak_Period_Unit_fee
            Night_period_fee = Night_period_electricity_consumption_amount * Residential_Night_Period_Unit_fee
            Distribution_fee = Total_electricity_consumption_amount * Residential_Unit_Distribution_Fee
            
            Multi_time_fee = Daytime_period_fee + Peak_period_fee + Night_period_fee
            ECT_Amount_Single = Single_time_fee * Residental_ECT_rate
            ECT_Amount_Multi = Multi_time_fee * Residental_ECT_rate
            VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Residental_VAT_rate
            VAT_Amount_Multi = (Multi_time_fee + ECT_Amount_Multi + Distribution_fee) * Residental_VAT_rate       
        if(Residential_Highest_Daily_Consumption < Total_electricity_consumption_amount / Number_of_days_between_previous_and_current_meter_reading_dates): #Cheking Daily consumption limit to find the highest daily consumption 
            Residential_Highest_Daily_Consumption = Total_electricity_consumption_amount / Number_of_days_between_previous_and_current_meter_reading_dates #Changing if the condition is met
            Residential_Highest_daily_consumer_no = Consumer_no #Changing if the condition is met
            if(Is_multi_time_or_single_time_tariff in ['M','m']): #Checking Multi time tariff
                Residential_Highest_daily_invoice_fee = Multi_time_fee + Distribution_fee + ECT_Amount_Multi + VAT_Amount_Multi #Calculating Multi time fee and changing
            else:
                Residential_Highest_daily_invoice_fee = Single_time_fee + Distribution_fee + ECT_Amount_Single + VAT_Amount_Single #Calculating Single time fee and changing

    elif(Consumer_Type_Code == 'A' or Consumer_Type_Code == 'a'): #Agricultural type
        Count_Agricultural_consumer += 1
        Total_Agricultural_Consumption += Total_electricity_consumption_amount
        Daytime_period_fee = Daytime_period_electricity_consumption_amount * Agricultural_Activities_Daytime_Period_Units_fee
        Peak_period_fee = Peak_period_electricity_consumption_amount * Agricultural_Activities_Peak_Period_Unit_fee
        Night_period_fee = Night_period_electricity_consumption_amount * Agricultural_Activities_Night_Period_Unit_fee
        Distribution_fee = Total_electricity_consumption_amount * Agricultural_Activities_Unit_Distribution_fee
        Single_time_fee = Total_electricity_consumption_amount * Agricultural_Activities_Single_time_fee                           
        Multi_time_fee = Daytime_period_fee + Peak_period_fee + Night_period_fee
        ECT_Amount_Single = Single_time_fee * Agricultural_ECT_rate
        ECT_Amount_Multi = Multi_time_fee * Agricultural_ECT_rate
        VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Agricultural_VAT_rate
        VAT_Amount_Multi = (Multi_time_fee + ECT_Amount_Multi + Distribution_fee) * Agricultural_VAT_rate
    
    elif(Consumer_Type_Code == 'L' or Consumer_Type_Code == 'l'): #Lighting type
        Count_Lighting_consumer += 1 
        Total_Lighting_Consumption += Total_electricity_consumption_amount
        Single_time_fee = Total_electricity_consumption_amount * Lighting_Unit_fee
        Distribution_fee = Total_electricity_consumption_amount * Lighting_Unit_Distribution_fee
        ECT_Amount_Single = Single_time_fee * Lighting_ECT_rate
        VAT_Amount_Single = (Single_time_fee + ECT_Amount_Single + Distribution_fee) * Lighting_VAT_rate
        Multi_time_fee = 0 #The reason I put it here is because it returns the value none
    
    Total_Consumers = Count_Industry_consumer + Count_Agricultural_consumer + Count_Lighting_consumer + Count_Public_consumer + Count_Residential_consumer #Calculating the number of consumers of all types 
    Total_Consumption = Total_Agricultural_Consumption + Total_Industry_Consumption + Total_Lighting_Consumption + Total_Public_Consumption + Total_Residential_Consumption #Calculating the number of consumption amount of all types
    if(Is_multi_time_or_single_time_tariff in ['M','m']): #Checking Multi-time and single-time , Calculating revenue amounts
        GDZ_Corporation_total_revenue_amount += (Multi_time_fee - Distribution_fee)
        The_Municipality_total_revenue_amount += ECT_Amount_Multi
        The_State_total_revenue_amount += VAT_Amount_Multi
    else:
        GDZ_Corporation_total_revenue_amount += (Single_time_fee - Distribution_fee)
        The_Municipality_total_revenue_amount += ECT_Amount_Single
        The_State_total_revenue_amount += VAT_Amount_Single    
    
    if(Is_multi_time_or_single_time_tariff in ['M','m']):
        invoice_fee = Multi_time_fee + Distribution_fee + ECT_Amount_Multi + VAT_Amount_Multi
    else:
        invoice_fee = Single_time_fee + Distribution_fee + ECT_Amount_Single + VAT_Amount_Single
    
    if(not Consumer_Type_Code in ['R','r']): #Finding the highest invoice amount not including Residential type
        if(Highest_invoice_fee < invoice_fee):
            Highest_invoice_fee = invoice_fee
            Highest_invoice_consumer_no = Consumer_no
            Highest_invoice_consumer_type = Consumer_Type_Code
            Highest_invoice_consumption_amount_daily_avr = Total_electricity_consumption_amount / Number_of_days_between_previous_and_current_meter_reading_dates
        
    
    def invoice_printing():
        global Count_who_made_loss
        global Total_count_Multi_time_prefered
        
        print(f"Consumer No:{Consumer_no}")
        
        if(Consumer_Type_Code in ['I','i']):
            print("Consumer Type: Industry")
        elif(Consumer_Type_Code in ['P','p']):
            print("Consumer Type: Public and Private Services Sector and Other")
        elif(Consumer_Type_Code in ['R','r']):
            print("Consumer Type: Residental")
        elif(Consumer_Type_Code in ['A','a']):
            print("Consumer Type: Agricultural Activities")
        else:
            print("Consumer Type: Lighting")                
        
        print(f"Daytime period electricity consumption amount in {Number_of_days_between_previous_and_current_meter_reading_dates} days = {Daytime_period_electricity_consumption_amount}kWh")
        print(f"Peak period electricity consumption amount in {Number_of_days_between_previous_and_current_meter_reading_dates} days = {Peak_period_electricity_consumption_amount}kWh")
        print(f"Night period electricity consumption amount in {Number_of_days_between_previous_and_current_meter_reading_dates} days = {Night_period_electricity_consumption_amount}kWh")
        print(f"Total electricity consumption amount in {Number_of_days_between_previous_and_current_meter_reading_dates} days = {Total_electricity_consumption_amount}kWh")
        if(Is_multi_time_or_single_time_tariff == 'M' or Is_multi_time_or_single_time_tariff == 'm'):
            print(f"Total electricity consumption fee in{Number_of_days_between_previous_and_current_meter_reading_dates} days = {Multi_time_fee: .2f}TL")
            print(f"ECT amount to be transferred to the municipality in{Number_of_days_between_previous_and_current_meter_reading_dates} days = {ECT_Amount_Multi: .2f}TL")
            print(f"VAT amount to be transferred to the state in{Number_of_days_between_previous_and_current_meter_reading_dates} days = {VAT_Amount_Multi: .2f}TL")
            print(f"Total invoice amount for {Number_of_days_between_previous_and_current_meter_reading_dates} days = {Multi_time_fee + Distribution_fee + ECT_Amount_Multi + VAT_Amount_Multi: .2f}")
        else:
            print(f"Total electricity consumption fee in {Number_of_days_between_previous_and_current_meter_reading_dates} days = {Single_time_fee: .2f}TL")
            print(f"ECT amount to be transferred to the municipality in {Number_of_days_between_previous_and_current_meter_reading_dates} days = {ECT_Amount_Single: .2f}TL")
            print(f"VAT amount to be transferred to the state in {Number_of_days_between_previous_and_current_meter_reading_dates} days = {VAT_Amount_Single: .2f}TL")
            print(f"Total invoice amount for {Number_of_days_between_previous_and_current_meter_reading_dates} days = {Single_time_fee + Distribution_fee + ECT_Amount_Single + VAT_Amount_Single: .2f}")
        if(not Consumer_Type_Code in ['L','l'] and not Is_Family_Of_martyrs_and_veterans in ['Y','y']):
            Total_count_Multi_time_prefered += 1
            print(f"Single time amount - Multi time amount = {Single_time_fee-Multi_time_fee: .2f}TL")
            if(Single_time_fee > Multi_time_fee):
                print("Multi time tariff is profitable")
            elif(Multi_time_fee > Single_time_fee):
                Count_who_made_loss += 1
                print("Single time is profitable")
            else:
                print("equal")
        if(Total_amount_of_electricity_Until_this_period >= 1000):
            print("Congratulations! Your Right to Become a Free Consumer Has Been Gained")
        else:
            print("Unfortunately You Did Not Win The Right To Be Free Consumer")
    invoice_printing()                           

while True:
    Consumer_no = int(input("Enter your Consumer No: "))
    if(Consumer_no == 0): #The program is terminated when the consumer number becomes 0.
        break
    Consumer_no,Consumer_Type_Code,Is_Family_Of_martyrs_and_veterans,Daytime_period_electricity_consumption_amount,Peak_period_electricity_consumption_amount,Night_period_electricity_consumption_amount,Total_electricity_consumption_amount,Number_of_days_between_previous_and_current_meter_reading_dates,Total_amount_of_electricity_Until_this_period,Is_multi_time_or_single_time_tariff = Get_invoice_Information()

    invoice_calculation(Consumer_no,Consumer_Type_Code,Is_Family_Of_martyrs_and_veterans,Daytime_period_electricity_consumption_amount,Peak_period_electricity_consumption_amount,Night_period_electricity_consumption_amount,Total_electricity_consumption_amount,Number_of_days_between_previous_and_current_meter_reading_dates,Total_amount_of_electricity_Until_this_period,Is_multi_time_or_single_time_tariff)

print(f"Bornova's total electricity consumption amount = {Total_Consumption} kWh")
print(f"Industry: Total consumers = {Count_Industry_consumer} Percentage = %{Count_Industry_consumer / Total_Consumers * 100: .2f} Total Electricity Consumption Amount = {Total_Industry_Consumption} kWh ",end='')
if(Count_Industry_consumer != 0):
    print(f"Average Electricity Consumption Amount = {Total_Industry_Consumption / Count_Industry_consumer: .2f} kWh")
else:
    print(f"Average Electricity Consumption Amount = 0 kWh")  

print(f"Public: Total consumers = {Count_Public_consumer} Percentages = %{Count_Public_consumer / Total_Consumers * 100: .2f} Total Electricity Consumption Amount = {Total_Public_Consumption} kWh ",end='')
if(Count_Public_consumer != 0):
    print(f"Average Electricity Consumption Amount = {Total_Public_Consumption / Count_Public_consumer: .2f} kWh")
else:
    print(f"Average Electricity Consumption Amount = 0 kWh")

print(f"Residential: Total consumers = {Count_Residential_consumer} Percentages = %{Count_Residential_consumer / Total_Consumers * 100: .2f} Total Electricity Consumption Amount = {Total_Residential_Consumption} kWh",end='')
if(Count_Residential_consumer != 0):
    print(f"Average Electricity Consumption Amount = {Total_Residential_Consumption / Count_Residential_consumer: .2f} kWh ")
else:
    print(f"Average Electricity Consumption Amount = 0 kWh")

print(f"Agricultural Activities: Total consumers = {Count_Agricultural_consumer} Percentages = %{Count_Agricultural_consumer / Total_Consumers * 100: .2f} Total Electricity Consumption Amount = {Total_Agricultural_Consumption} kWh ",end='')
if(Count_Agricultural_consumer != 0):
    print(f"Average Electricity Consumption Amount = {Total_Agricultural_Consumption / Count_Agricultural_consumer: .2f} kWh ")
else:
    print(f"Average Electricity Consumption Amount = 0 kWh")

print(f"Lighting: Total consumers = {Count_Lighting_consumer} Percentages = %{Count_Lighting_consumer / Total_Consumers * 100: .2f} Total Electricity Consumption Amount = {Total_Lighting_Consumption} kWh ",end='')
if(Count_Lighting_consumer != 0):
    print(f"Average Electricity Consumption Amount = {Total_Lighting_Consumption / Count_Lighting_consumer: .2f} kWh")
else:
    print(f"Average Electricity Consumption Amount = 0 kWh")
if(Count_Public_single_consumer != 0):
    print(f"Public and Private Services Sector and Other: Number of consumers who prefer single-time and multi-time tariffs = {Count_Public_multi_consumer + Count_Public_single_consumer} Percentages  = %{Count_Public_single_consumer / Count_Public_consumer * 100: .2f} Single %{Count_Public_multi_consumer / Count_Public_consumer * 100: .2f} Multi ")
else:
    print("Public and Private Services Sector and Other: Number of consumers who prefer single-time and multi-time tariffs = 0 Percentages = Single %0 Multi %0 ")    
if(Total_Public_days == 0):
    print("average daily electricity consumption amounts in this period = ",end='')
    print("We cannot display this data because there is no consumer of type Public and Private Services Sector and Other.")
else:
    print(f"Average daily electricity consumption amounts in this period = {Total_Public_Consumption / Total_Public_days: .2f}")

print(f"The number of industry type consumers whose electricity consumption amount is more than 10000 kWh or whose electricity bill is more than 100000 TL = {Count_Industry_fee_or_consumption_over_10k} ",end='')
if(Count_Industry_consumer != 0):
    print(f"Percentage = %{Count_Industry_fee_or_consumption_over_10k / Count_Industry_consumer * 100: .2f}")
else:
    print(f"Percentage = %0")

print("Residential type consumer with the highest daily average electricity consumption ",end='')
print(f"Consumer No: {Residential_Highest_daily_consumer_no} Daily consumption amount: {Residential_Highest_Daily_Consumption} kWh Invoice fee amount: {Residential_Highest_daily_invoice_fee}TL")

print(f"Information about the highest invoice fee amount: Consumer No : {Highest_invoice_consumer_no} ",end='')
if(Highest_invoice_consumer_type in ['I','i']):
    print("Consumer Type : Industry")
elif(Highest_invoice_consumer_type in ['P','p']):
    print("Consumer Type : Public and Private Services Sector and Other")
elif(Highest_invoice_consumer_type in ['A','a']):
    print("Consumer Type : Agricultural Activities")
else:
    print("Consumer Type : Lighting")
print(f"Average Daily Consumption Amount = {Highest_invoice_consumption_amount_daily_avr: .2f} kWh Invoice fee amount = {Highest_invoice_fee: .2f}TL")

print(f"Total revenue amounts obtained by the GDZ corporation,the municipality,the state = {GDZ_Corporation_total_revenue_amount: .2f},{The_Municipality_total_revenue_amount: .2f},{The_State_total_revenue_amount: .2f}")

if(Total_count_Multi_time_prefered == 0):
    print("the percentage of those who made a loss despite choosing multi-time tariff in the relevant period = 0")
else:
    print(f"the percentage of those who made a loss despite choosing multi-time tariff in the relevant period = %{Count_who_made_loss / Total_count_Multi_time_prefered * 100: .2f}")
