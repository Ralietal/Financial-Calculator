# a import math function is imported to enable mathematical applications
import math
# This program provides a user with a financial calculators options of investment and bond repayment

# The program does not take into account the capitalisation of inputs letters,this is ensured by a use of the.lower()function from phython


landing_page = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n investment - to calculate the amount of interest you'll earn on interest \n bond       - to calculate the amount you'll have to pay on a home loan")

calculator_choice = input("Choose (investment or bond) \n")

if calculator_choice.lower() == "bond":
    present_value_of_the_house = float(input("Enter the value of the present house \n"))
    interest_rate = float(input("Enter the interest rate without % sign:eg 8 and not8% \n"))
    interest_rate = float((interest_rate/100)/12)
    pay_down_period = float(input("Enter the number of months you want to repay the bond \n"))
    bond_monthly_repayment = round((interest_rate*present_value_of_the_house)/(1-math.pow((1+interest_rate),(-(pay_down_period)))))
    print("Your monthly repayment is R"  + str(bond_monthly_repayment))
    
elif calculator_choice.lower() == "investment":
    investment_amount = float(input("Enter the amount you want to invest \n"))
    interest_rate = float(input("Enter the interest rate without % sign:eg 8 and not 8% \n"))
    interest_rate =interest_rate/100
    investment_period = float(input("Enter the number of years you want to invest \n"))
    interest = input("Please choose between (simple or compound) \n")
    
#an additional if statement is included in this section and indendent because there are two options on interest type to be chosen
    
    if interest == "simple":  
    
        payout_on_simple_interest = investment_amount*(1+((interest_rate)*investment_period))
        print("Your payout on Simple Interest is R " + str(payout_on_simple_interest))
    
    else:  
        payout_on_compound_interest =round(investment_amount*math.pow((1+(interest_rate)),investment_period))
    
        print("Your payout on Compound Interest is R " + str(payout_on_compound_interest))       
    
else:
    print("Error message:You did not choose the valid option")

