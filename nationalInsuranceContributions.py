# Computation of National Insurance Contributions (NICs)

#Employee information (example info)
paidWeekly = False #Earning period
paidMonthly = True #Earning period
statePensionAge = 65 #years old
age = 22 #years old - note employees must be a minimum of 16yrs old in the UK
apprentice = True
earnings = 4000 #All earnings received in monetary form
taxableBenefits = 4310
selfEmployed = False
selfEmployedProfits = 8610
selfEmployedTaxableTradingProfits = 8610
smallProfitsThreshold = 6205 #2018/19
class2weekly = 2.95 #2018/19
selfEmployedWeeks = 52

#Thresholds
weeklyPrimaryThreshold = 162 #pounds sterling
monthlyPrimaryThreshold = 702
yearlyPrimaryThreshold = 8424
weeklyUpperEarningsLimit = 892
monthlyUpperEarningsLimit = 3863
yearlyUpperEarningsLimit = 46350

#Class 1 NICs - paid by employees and employers

#Class 1 primary - paid by employees
class1primary = 0
if age >= 16 and age < statePensionAge:
    if paidWeekly == True:
        if earnings < weeklyPrimaryThreshold:
            class1primary = 0
        elif earnings >= weeklyPrimaryThreshold and earnings <= weeklyUpperEarningsLimit:
            class1primary = (earnings - weeklyPrimaryThreshold) * 0.12
        else:
            class1primary = (weeklyUpperEarningsLimit - weeklyPrimaryThreshold) * 0.12 + (earnings - weeklyUpperEarningsLimit) * 0.02
    elif paidMonthly == True:
        if earnings < monthlyPrimaryThreshold:
            class1primary = 0
        elif earnings >= monthlyPrimaryThreshold and earnings <= monthlyUpperEarningsLimit:
            class1primary = (earnings - monthlyPrimaryThreshold) * 0.12
        else:
            class1primary = (monthlyUpperEarningsLimit - monthlyPrimaryThreshold) * 0.12 + (earnings - monthlyUpperEarningsLimit) * 0.02
else:
    class1primary = 0 #Class 1 primary NICs only payable by those between ages 16 and stage pension age
print(f"Class 1 primary contributions payable by the employee are £{round(class1primary)}")

#Class 1 secondary - paid by employers (note an employment allowance of £3k is available to employers to use across total secondary NICs)
class1secondary = 0
if apprentice == False:
    if age >= 21:
        if paidWeekly == True:
            if earnings < weeklyPrimaryThreshold:
                class1secondary = 0
            elif earnings > weeklyPrimaryThreshold:
                class1secondary = (earnings - weeklyPrimaryThreshold) * 0.138
        elif paidMonthly == True:
            if earnings < monthlyPrimaryThreshold:
                class1secondary = 0
            elif earnings > monthlyPrimaryThreshold:
                class1secondary = (earnings - monthlyPrimaryThreshold) * 0.138
    elif age < 21:
        if paidWeekly == True:
            if earnings < weeklyUpperEarningsLimit:
                class1secondary = 0
            elif earnings >= weeklyUpperEarningsLimit:
                class1secondary = (earnings - weeklyUpperEarningsLimit) * 0.138
        elif paidMonthly == True:
            if earnings < monthlyUpperEarningsLimit:
                class1secondary = 0
            elif earnings >= monthlyUpperEarningsLimit:
                class1secondary = (earnings - monthlyUpperEarningsLimit) * 0.138
elif apprentice == True and age < 25:
    if paidWeekly == True:
        if earnings < weeklyUpperEarningsLimit:
            class1secondary = 0
        elif earnings >= weeklyUpperEarningsLimit:
            class1secondary = (earnings - weeklyUpperEarningsLimit) * 0.138
    elif paidMonthly == True:
        if earnings < monthlyUpperEarningsLimit:
            class1secondary = 0
        elif earnings >= monthlyUpperEarningsLimit:
            class1secondary = (earnings - monthlyUpperEarningsLimit) * 0.138
print(f"Class 1 secondary contributions payable by the employer are £{round(class1secondary)}")

#Class 1A NICs - paid by employers on employees' taxable benefits
class1A = taxableBenefits * 0.138
print(f"Class 1A NICs payable by the employer on employees' taxable benefits are £{round(class1A)}")

#Class 2 NICs - paid by self-employed at a fixed weekly rate
class2 = 0
if selfEmployed == True and age >= 16 and age < statePensionAge:
    if selfEmployedProfits < smallProfitsThreshold:
        class2 = 0
    else:
        class2 = selfEmployedWeeks * class2weekly
print(f"Class 2 NICs payable by the self employed are £{round(class2)}")

#Class 4  NICs - paid by self-employed on their taxable trading profit
class4 = 0
if selfEmployed == True and age >= 16 and age < statePensionAge:
    if selfEmployedTaxableTradingProfits < yearlyPrimaryThreshold:
        class4 = 0
    elif selfEmployedTaxableTradingProfits >= yearlyPrimaryThreshold and selfEmployedTaxableTradingProfits < yearlyUpperEarningsLimit:
        class4 = (selfEmployedTaxableTradingProfits - yearlyPrimaryThreshold) * 0.09
    else:
        class4 = (yearlyUpperEarningsLimit - yearlyPrimaryThreshold) * 0.09 + (selfEmployedTaxableTradingProfits - yearlyUpperEarningsLimit) * 0.02
print(f"Class 4 NICs payable by the self employed are £{round(class4)}")