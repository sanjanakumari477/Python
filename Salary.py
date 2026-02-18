# Program to calculate Net Salary
basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA (House Rent Allowance): "))
da = float(input("Enter DA (Dearness Allowance): "))
allowances = float(input("Enter Other Allowances: "))
tax = float(input("Enter Tax Deduction: "))
pf = float(input("Enter PF (Provident Fund) Deduction: "))

# Gross Salary = Basic + HRA + DA + Other Allowances

gross_salary = basic_salary + hra + da + allowances

# Net Salary = Gross Salary - (Tax + PF)

net_salary = gross_salary - (tax + pf)

# Output
print("\n----- Salary Details -----")
print(f"Gross Salary : {gross_salary}")
print(f"Net Salary   : {net_salary}")
